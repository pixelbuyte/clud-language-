#!/usr/bin/env python3
"""recon.py — lightweight pentest reconnaissance toolkit.

Run from YOUR machine (not a sandbox) against a domain you own or have
written authorization to test.

Usage:
    python3 recon.py example.com          # full recon
    python3 recon.py example.com --dns    # DNS only
    python3 recon.py example.com --http   # HTTP headers only
    python3 recon.py example.com --tls    # TLS/cert only
    python3 recon.py example.com --paths  # common path probe
    python3 recon.py example.com --sub    # subdomain bruteforce
    python3 recon.py example.com -o report.json  # save JSON report

Requires: Python 3.8+, no external packages (stdlib only).
"""

import argparse
import json
import socket
import ssl
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed


def banner(section):
    print(f"\n{'='*60}")
    print(f"  {section}")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# DNS
# ---------------------------------------------------------------------------

def dns_lookup(domain):
    banner("DNS Enumeration")
    results = {}
    try:
        ips = socket.getaddrinfo(domain, None)
        unique = sorted({addr[4][0] for addr in ips})
        results["a_aaaa"] = unique
        print(f"  A/AAAA records: {', '.join(unique)}")
    except socket.gaierror as e:
        results["a_aaaa"] = []
        print(f"  DNS resolution failed: {e}")

    for name in [f"www.{domain}", f"mail.{domain}", f"ftp.{domain}",
                 f"webmail.{domain}", f"smtp.{domain}", f"pop.{domain}"]:
        try:
            ip = socket.gethostbyname(name)
            results.setdefault("common_subdomains", {})[name] = ip
            print(f"  {name} -> {ip}")
        except socket.gaierror:
            pass

    try:
        import subprocess
        for rtype in ["MX", "NS", "TXT", "SOA", "CNAME"]:
            try:
                out = subprocess.run(
                    ["nslookup", "-type=" + rtype, domain],
                    capture_output=True, text=True, timeout=10
                )
                if out.stdout.strip():
                    results[rtype.lower()] = out.stdout.strip()
                    print(f"\n  {rtype} records:")
                    for line in out.stdout.strip().splitlines():
                        print(f"    {line}")
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
    except ImportError:
        pass

    return results


# ---------------------------------------------------------------------------
# HTTP Headers
# ---------------------------------------------------------------------------

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Resource-Policy",
    "Cross-Origin-Embedder-Policy",
]

INFO_HEADERS = [
    "Server",
    "X-Powered-By",
    "X-AspNet-Version",
    "X-Generator",
    "Via",
]


def http_headers(domain):
    banner("HTTP Header Analysis")
    results = {"security": {}, "info_leak": {}, "redirects": [], "status": None}

    for scheme in ["https", "http"]:
        url = f"{scheme}://{domain}/"
        try:
            req = urllib.request.Request(url, method="HEAD")
            req.add_header("User-Agent", "Mozilla/5.0 (recon/1.0)")
            resp = urllib.request.urlopen(req, timeout=10)
            results["status"] = resp.status
            headers = dict(resp.headers)
            results["all_headers"] = headers

            print(f"  {url} -> {resp.status}")
            print(f"\n  Security headers:")
            for h in SECURITY_HEADERS:
                val = headers.get(h)
                status = "PRESENT" if val else "MISSING"
                marker = "+" if val else "-"
                results["security"][h] = val or "MISSING"
                print(f"    [{marker}] {h}: {val or 'MISSING'}")

            print(f"\n  Information disclosure:")
            for h in INFO_HEADERS:
                val = headers.get(h)
                if val:
                    results["info_leak"][h] = val
                    print(f"    [!] {h}: {val}")

            if not results["info_leak"]:
                print(f"    None found")

            break
        except urllib.error.HTTPError as e:
            results["status"] = e.code
            print(f"  {url} -> HTTP {e.code}")
            break
        except Exception as e:
            print(f"  {url} -> {e}")

    return results


# ---------------------------------------------------------------------------
# TLS / Certificate
# ---------------------------------------------------------------------------

def tls_check(domain):
    banner("TLS / Certificate Analysis")
    results = {}
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(10)
            s.connect((domain, 443))
            cert = s.getpeercert()
            cipher = s.cipher()
            version = s.version()

            results["protocol"] = version
            results["cipher"] = cipher
            results["subject"] = dict(x[0] for x in cert.get("subject", ()))
            results["issuer"] = dict(x[0] for x in cert.get("issuer", ()))
            results["not_before"] = cert.get("notBefore")
            results["not_after"] = cert.get("notAfter")
            results["san"] = [
                v for t, v in cert.get("subjectAltName", ()) if t == "DNS"
            ]

            print(f"  Protocol: {version}")
            print(f"  Cipher:   {cipher[0]} ({cipher[2]} bits)")
            print(f"  Subject:  {results['subject']}")
            print(f"  Issuer:   {results['issuer']}")
            print(f"  Valid:    {results['not_before']} — {results['not_after']}")
            print(f"  SANs:     {', '.join(results['san'])}")

            if version in ("TLSv1", "TLSv1.1"):
                print(f"  [!] WEAK: {version} is deprecated")
                results["warning"] = f"{version} is deprecated"

    except ssl.SSLCertVerificationError as e:
        results["error"] = f"Certificate verification failed: {e}"
        print(f"  [!] {results['error']}")
    except Exception as e:
        results["error"] = str(e)
        print(f"  Error: {e}")

    return results


# ---------------------------------------------------------------------------
# Common Path Probing
# ---------------------------------------------------------------------------

COMMON_PATHS = [
    "/robots.txt",
    "/sitemap.xml",
    "/.well-known/security.txt",
    "/.env",
    "/.git/HEAD",
    "/.git/config",
    "/wp-login.php",
    "/wp-admin/",
    "/admin/",
    "/login",
    "/api/",
    "/api/v1/",
    "/graphql",
    "/.htaccess",
    "/server-status",
    "/server-info",
    "/phpinfo.php",
    "/info.php",
    "/debug/",
    "/actuator/health",
    "/swagger-ui.html",
    "/api-docs",
    "/.DS_Store",
    "/backup/",
    "/config.json",
    "/package.json",
    "/composer.json",
    "/web.config",
    "/crossdomain.xml",
    "/.svn/entries",
]


def probe_path(domain, path):
    url = f"https://{domain}{path}"
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "Mozilla/5.0 (recon/1.0)")
        resp = urllib.request.urlopen(req, timeout=5)
        return path, resp.status, len(resp.read()) if resp.status == 200 else 0
    except urllib.error.HTTPError as e:
        if e.code not in (404, 403, 405):
            return path, e.code, 0
    except Exception:
        pass
    return None


def path_probe(domain):
    banner("Common Path Probing")
    results = {}
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(probe_path, domain, p): p for p in COMMON_PATHS}
        for f in as_completed(futures):
            hit = f.result()
            if hit:
                path, status, size = hit
                results[path] = {"status": status, "size": size}
                flag = "[!]" if status == 200 else "[?]"
                print(f"  {flag} {path} -> {status}")

    if not results:
        print("  No interesting paths found")
    return results


# ---------------------------------------------------------------------------
# Subdomain Bruteforce (small wordlist)
# ---------------------------------------------------------------------------

SUBDOMAIN_WORDS = [
    "www", "mail", "ftp", "admin", "blog", "shop", "store", "api",
    "dev", "staging", "test", "beta", "demo", "app", "portal",
    "webmail", "smtp", "pop", "imap", "ns1", "ns2", "dns",
    "vpn", "remote", "cdn", "media", "static", "assets", "img",
    "docs", "wiki", "git", "gitlab", "jenkins", "ci", "cd",
    "monitor", "grafana", "kibana", "elastic", "prometheus",
    "sentry", "status", "health", "backup", "db", "mysql",
    "postgres", "redis", "mongo", "mq", "rabbit", "kafka",
    "auth", "sso", "login", "oauth", "id", "iam",
    "crm", "erp", "hr", "jira", "confluence", "slack",
    "m", "mobile", "internal", "intranet", "extranet",
    "stg", "uat", "qa", "sandbox", "preview",
]


def resolve_sub(domain, word):
    name = f"{word}.{domain}"
    try:
        ip = socket.gethostbyname(name)
        return name, ip
    except socket.gaierror:
        return None


def subdomain_enum(domain):
    banner("Subdomain Enumeration (mini wordlist)")
    results = {}
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(resolve_sub, domain, w): w for w in SUBDOMAIN_WORDS}
        for f in as_completed(futures):
            hit = f.result()
            if hit:
                name, ip = hit
                results[name] = ip
                print(f"  [+] {name} -> {ip}")

    if not results:
        print("  No subdomains found with mini wordlist")
    print(f"\n  Found {len(results)} subdomains. For deeper coverage, use")
    print(f"  subfinder, amass, or a larger wordlist.")
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Recon toolkit")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--dns", action="store_true", help="DNS only")
    parser.add_argument("--http", action="store_true", help="HTTP headers only")
    parser.add_argument("--tls", action="store_true", help="TLS/cert only")
    parser.add_argument("--paths", action="store_true", help="Path probe only")
    parser.add_argument("--sub", action="store_true", help="Subdomain enum only")
    parser.add_argument("-o", "--output", help="Save JSON report to file")
    args = parser.parse_args()

    domain = args.domain.replace("https://", "").replace("http://", "").strip("/")
    run_all = not any([args.dns, args.http, args.tls, args.paths, args.sub])

    print(f"\n  Target: {domain}")
    print(f"  Time:   {datetime.now(timezone.utc).isoformat()}")
    print(f"  Scope:  {'full recon' if run_all else 'selected modules'}")

    report = {"target": domain, "timestamp": datetime.now(timezone.utc).isoformat()}

    if run_all or args.dns:
        report["dns"] = dns_lookup(domain)
    if run_all or args.http:
        report["http"] = http_headers(domain)
    if run_all or args.tls:
        report["tls"] = tls_check(domain)
    if run_all or args.paths:
        report["paths"] = path_probe(domain)
    if run_all or args.sub:
        report["subdomains"] = subdomain_enum(domain)

    banner("Summary")
    findings = []
    sec = report.get("http", {}).get("security", {})
    for h, v in sec.items():
        if v == "MISSING":
            findings.append(f"Missing security header: {h}")
    for h, v in report.get("http", {}).get("info_leak", {}).items():
        findings.append(f"Info leak: {h}: {v}")
    tls = report.get("tls", {})
    if tls.get("warning"):
        findings.append(f"TLS: {tls['warning']}")
    if tls.get("error"):
        findings.append(f"TLS: {tls['error']}")
    for path, info in report.get("paths", {}).items():
        if info["status"] == 200:
            findings.append(f"Exposed path: {path}")
    sub_count = len(report.get("subdomains", {}))
    if sub_count:
        findings.append(f"{sub_count} subdomains resolved")

    if findings:
        for i, f in enumerate(findings, 1):
            print(f"  {i}. {f}")
    else:
        print("  No obvious findings. Consider deeper tools (nmap, nikto, burp).")

    report["findings"] = findings

    if args.output:
        with open(args.output, "w") as fh:
            json.dump(report, fh, indent=2, default=str)
        print(f"\n  Report saved to {args.output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
