# Zorlun Grammar

Zorlun ("origin-tongue") is an a priori constructed language — no roots are borrowed from any existing language. It has its own alphabet and a grammar unlike Clud's.

## 1. The Zor alphabet

20 glyphs, one sound each. Written left to right, words separated by `·` in script (spaces when typed).

### Vowels

| Letter | Sound | Glyph shape |
|---|---|---|
| a | *father* | horizontal bar, dot above |
| e | *bet* | upward cup |
| i | *machine* | single vertical stroke |
| o | *more* | full circle |
| u | *rule* | downward cup |

### Consonants

| Letter | Sound | Glyph shape |
|---|---|---|
| m | m | double-hump |
| n | n | single hump |
| p | p | stroke with flag |
| t | t | plus sign |
| k | k | stroke with prongs |
| b | b | stroke, bottom loop |
| d | d | stroke, top loop |
| g | g (hard) | hooked spiral |
| s | s (see) | snake curve |
| z | z | zigzag |
| l | l | right-angle corner |
| r | r | stroke, small circle on top |
| v | v | downward wedge |
| h | h | two verticals, middle bar |
| w | w | double wedge |

No c, j, q, x, or y. Every letter has one sound. Stress falls on the first syllable.

## 2. Word order: Subject–Object–Verb

Zorlun is SOV. The verb comes last.

- **Om-im id-un ole-a.** I (subj) you (obj) see (now). = I see you.
- **Nel-im es-un nu-il.** Friend (subj) water (obj) give (past). = The friend gave water.

## 3. Case suffixes

Glued to nouns to show their role in the sentence.

| Suffix | Role | Example |
|---|---|---|
| -im | subject | **om-im** (I, as subject) |
| -un | object | **veka-un** (website, as object) |
| -el | to, for | **om-el** (to me, for me) |
| -os | of, belonging to | **kesh-os** (of security) |
| -ko | with, using | **tula-ko** (with a tool) |
| -ta | in, at | **nema-ta** (in the network) |

## 4. Verb endings

| Suffix | Time | Example |
|---|---|---|
| -a | now, present | **skan-a** (scans) |
| -il | past | **skan-il** (scanned) |
| -o | future | **skan-o** (will scan) |
| -u | would, conditional | **skan-u** (would scan) |
| -i | infinitive / linking | **skan-i** (to scan) |

## 5. Negation and questions

- **vai** before the verb = not: **Om-im vai zen-a.** I don't know.
- **ne** at the end = yes/no question: **Id-im kepa-a ne?** Do you understand?
- **kel** = what/which (in place of the unknown): **Id-im kel-un mun-a?** What do you want?

## 6. Certainty markers (sentence-initial)

| Word | Meaning |
|---|---|
| **tol** | I'm sure, verified |
| **mip** | probably |
| **ket** | guessing |

**Tol om-im auta-un vali-il.** I am sure I verified authorization.

## 7. Linking words

| Word | Meaning |
|---|---|
| **mo** | and |
| **wu** | or |
| **ba** | but |

**Om-im vuln-un find-il mo findi-un repo-a.** I found a vulnerability and am reporting the finding.

## 8. Plurals

Add **-zu** to pronouns: **omzu** (we), **idzu** (you all), **urzu** (they).

For nouns, context or a number suffices: **re veka** (two websites), **alla vuln** (all vulnerabilities).

## 9. Compounds

Main word first, modifier after:

- **kesh rav** = security check
- **veka pran** = website pentest
- **nema skan** = network scan

## 10. Canonical cybersecurity phrases

| Zorlun | English |
|---|---|
| **Ni veka-un pran-a.** | Pentest this site. |
| **Ni veka-un kesh rav-a.** | Security-check this site. |
| **Bota-un tak-a.** | Do both. |
| **Ni veka-un skan-a.** | Scan this website. |
| **Ni ruma-un auda-a.** | Audit this web application. |
| **Auta-un vali-a.** | Verify authorization. |
| **Vuln-un find-a.** | Find vulnerabilities. |
| **Findi-un repo-a.** | Report the finding. |
| **Fiks-un veri-a.** | Verify the fix. |
| **Ni veka-un retes-a.** | Retest this site. |
| **Risk-un ases-a.** | Assess the risk. |
| **Loga-un anal-a.** | Analyze the logs. |
| **Traf-un insp-a.** | Inspect the traffic. |
| **Auth-un rav-a.** | Test authentication. |
| **Aces-un rav-a.** | Test access control. |
| **Apik-un rav-a.** | Test the API. |

## 11. Extension rule

For new vocabulary: prefer a short pronounceable root of 1–3 syllables, assign one primary meaning, avoid reusing an existing root, and record it in `lexicon.txt` before using it. Acronym-like roots (HTTP, TLS, DNS) may stay recognizable; Zorlun-native concepts use invented roots.
