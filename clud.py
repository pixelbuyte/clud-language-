#!/usr/bin/env python3
"""Clud toolkit: gloss sentences, look up words, and keep the docs honest.

    python3 clud.py gloss "Ka tu vola lerna Klud?"   # word-by-word meaning
    python3 clud.py find coffee                      # English -> Clud
    python3 clud.py check                            # lexicon rules + every **bold** example in the docs
    python3 clud.py dict > LEXICON.md                # regenerate the dictionary
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEXICON_FILE = HERE / "lexicon.txt"
DICTIONARY_FILE = HERE / "LEXICON.md"
DOCS = ["README.md", "GRAMMAR.md", "PHRASEBOOK.md"]

ALPHABET = set("abdefghiklmnoprstuvwyz")
VOWELS = set("aeiou")
ENDINGS = {
    "a": "doing, now",
    "i": "did (past)",
    "o": "will do (future)",
    "u": "would do",
    "e": "describing",
}
VERB_ENDINGS = set("aiou")

LITTLE_GROUPS = {
    "people": "People",
    "pointer": "Pointers",
    "amount": "Amounts",
    "starter": "Sentence starters",
    "reaction": "Reactions",
    "link": "Links",
    "relation": "Relations",
}
ROOT_GROUPS = {
    "beings": "Beings",
    "mind": "Mind and feelings",
    "talk": "Talk",
    "action": "Action",
    "quality": "Qualities",
    "thing": "Things, places, and time",
}
# Words that may open a clause before the subject: ka, pe, ve, ya, et, se, ...
CLAUSE_OPENERS = {"starter", "reaction", "link"}

TOKEN = re.compile(r"\[[^\]]*\]|`[^`]*`|[A-Za-z]+")
BOLD = re.compile(r"\*\*(.+?)\*\*")
CLAUSE_BREAK = re.compile(r"[.,!?;:]")


@dataclass
class Entry:
    word: str
    group: str
    gloss: str
    hint: str
    line: int

    @property
    def kind(self):
        if self.group in LITTLE_GROUPS:
            return "little"
        if self.group in ROOT_GROUPS:
            return "root"
        if self.group in ("number", "name"):
            return self.group
        return "unknown"


@dataclass
class Word:
    text: str
    role: str  # little, number, name, borrowed, thing, verb, describing, unknown
    parts: str
    gloss: str
    group: str = ""


class Lexicon:
    def __init__(self, path=LEXICON_FILE):
        self.entries = []
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip() or line.startswith("#"):
                continue
            fields = [field.strip() for field in line.split("|")]
            if len(fields) != 4:
                raise ValueError(f"{path.name}:{number}: expected 4 fields separated by '|'")
            self.entries.append(Entry(*fields, line=number))
        self.by_word = {entry.word.lower(): entry for entry in self.entries}

    def problems(self):
        """Every way the lexicon breaks Clud's word-shape rules."""
        found, seen = [], {}
        for entry in self.entries:
            where, word = f"lexicon.txt:{entry.line}", entry.word.lower()
            if word in seen:
                found.append(f"{where}: '{entry.word}' already defined on line {seen[word]}")
            seen[word] = entry.line
            if entry.kind == "unknown":
                found.append(f"{where}: unknown group '{entry.group}'")
            if not set(word) <= ALPHABET:
                found.append(f"{where}: '{entry.word}' uses letters outside the Clud alphabet")
            if entry.kind == "little" and len(word) != 2:
                found.append(f"{where}: little word '{entry.word}' must have exactly 2 letters")
            if entry.kind == "root" and (len(word) < 3 or word[-1] in VOWELS):
                found.append(f"{where}: root '{entry.word}' must have 3+ letters and end in a consonant")
            if entry.kind == "name" and not entry.word[0].isupper():
                found.append(f"{where}: name '{entry.word}' must be capitalized")
        return found

    def analyze(self, token):
        """Work out what one token is: a little word, a root plus ending, a name..."""
        if token[0] in "[`":
            return Word(token, "borrowed", token, "borrowed as-is")
        word = token.lower()
        entry = self.by_word.get(word)
        if entry:
            role = "thing" if entry.kind == "root" else entry.kind
            return Word(token, role, entry.word, entry.gloss, entry.group)
        if len(word) >= 4 and word[-1] in ENDINGS:
            root = self.by_word.get(word[:-1])
            if root and root.kind == "root":
                role = "verb" if word[-1] in VERB_ENDINGS else "describing"
                return Word(token, role, f"{root.word}+{word[-1]}", root.gloss, root.group)
        if token[0].isupper():
            return Word(token, "unknown", "name?", "not in the lexicon")
        return Word(token, "unknown", "?", "not in the lexicon")

    def gloss(self, text):
        return [self.analyze(token) for token in TOKEN.findall(text)]

    def problems_in(self, text):
        """Unknown words, plus clauses with a subject (or 'pe') but no verb."""
        found = []
        for clause in CLAUSE_BREAK.split(text):
            words = self.gloss(clause)
            found += [f"unknown word '{w.text}'" for w in words if w.role == "unknown"]
            openers = []
            while words and words[0].group in CLAUSE_OPENERS:
                openers.append(words.pop(0).parts)
            asks = "pe" in openers
            has_subject = bool(words) and words[0].group == "people"
            has_root = any(w.role in ("thing", "describing", "verb") for w in words)
            if (asks or has_subject) and has_root and not any(w.role == "verb" for w in words):
                found.append(f"no verb in '{clause.strip()}' (missing -a/-i/-o/-u?)")
        return found

    def find(self, query):
        query = query.lower()
        pattern = re.compile(rf"\b{re.escape(query)}")
        return [e for e in self.entries if e.word.lower() == query or pattern.search(e.gloss.lower())]

    def dictionary(self):
        return render_dictionary(self)


def check_docs(lexicon, root=HERE):
    """Check every **bold** span in the docs: bold is reserved for Clud."""
    found = []
    for name in DOCS:
        path = root / name
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for span in BOLD.findall(line):
                found += [f"{name}:{number}: {problem}" for problem in lexicon.problems_in(span)]
    if not DICTIONARY_FILE.exists() or DICTIONARY_FILE.read_text(encoding="utf-8") != lexicon.dictionary():
        found.append("LEXICON.md is out of date: run python3 clud.py dict > LEXICON.md")
    return found


def table(rows, header):
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return lines


def render_dictionary(lexicon):
    entries = lexicon.entries
    count = lambda kind: sum(1 for e in entries if e.kind == kind)
    out = [
        "# Clud Dictionary",
        "",
        "_Generated from `lexicon.txt` by `python3 clud.py dict`. Edit `lexicon.txt`, not this file._",
        "",
        f"{count('little')} little words, {count('root')} roots, "
        f"{count('number')} numbers, and {count('name')} names.",
        "",
        "## Little words",
        "",
        "Exactly two letters. They do the grammar and never change.",
    ]
    for group, title in LITTLE_GROUPS.items():
        rows = [(f"`{e.word}`", e.gloss, e.hint) for e in entries if e.group == group]
        out += ["", f"### {title}", ""] + table(rows, ["Clud", "English", "Remember it by"])
    out += [
        "",
        "## Roots",
        "",
        "Three or more letters, always ending in a consonant. Bare, a root names a thing.",
        "Add one ending to give it a job: `-a` doing (now), `-i` did, `-o` will do,",
        "`-u` would do, `-e` describing. Example: `kod` code, `koda` codes, `kodi` coded.",
    ]
    for group, title in ROOT_GROUPS.items():
        rows = [(f"`{e.word}`", e.gloss, e.hint) for e in entries if e.group == group]
        out += ["", f"### {title}", ""] + table(rows, ["Clud", "English", "Remember it by"])
    for kind, title in (("number", "Numbers"), ("name", "Names")):
        rows = [(f"`{e.word}`", e.gloss, e.hint) for e in entries if e.kind == kind]
        out += ["", f"## {title}", ""] + table(rows, ["Clud", "English", "Remember it by"])
    index = {}
    for e in entries:
        if e.kind in ("little", "root", "name"):
            for sense in re.split(r"[,;]", e.gloss):
                sense = sense.strip()
                if sense.startswith("(") and sense.endswith(")"):
                    sense = sense[1:-1]
                if sense:
                    index.setdefault(sense, []).append(f"`{e.word}`")
    rows = [(sense, ", ".join(words)) for sense, words in sorted(index.items(), key=lambda kv: kv[0].lower())]
    out += ["", "## English → Clud", ""] + table(rows, ["English", "Clud"])
    return "\n".join(out) + "\n"


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    command, args = argv[1], argv[2:]
    lexicon = Lexicon()
    if command == "gloss":
        words = lexicon.gloss(" ".join(args) if args else sys.stdin.read())
        width = max((len(w.text) for w in words), default=0)
        for w in words:
            note = f"  ({ENDINGS[w.parts[-1]]})" if w.role in ("verb", "describing") else ""
            print(f"{w.text:<{width}}  {w.parts:<10} {w.gloss}{note}")
        return 1 if any(w.role == "unknown" for w in words) else 0
    if command == "find":
        matches = lexicon.find(" ".join(args))
        for e in matches:
            print(f"{e.word:<8} {e.group:<9} {e.gloss}")
        return 0 if matches else 1
    if command == "check":
        problems = lexicon.problems() + check_docs(lexicon)
        print("\n".join(problems) if problems else "All good: every word follows the rules.")
        return 1 if problems else 0
    if command == "dict":
        sys.stdout.write(lexicon.dictionary())
        return 0
    print(f"unknown command '{command}'\n\n{__doc__.strip()}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
