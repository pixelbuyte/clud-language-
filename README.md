# Clud

**Sal! Ti esta Klud, lang nove po tu et mi.**
*Hi! This is Clud, a new language for you and me.*

Clud (say "klood") is a small constructed language made for a human and an AI to talk in.
It's designed to be learned in an afternoon:

- *Small.* 41 little grammar words and about 160 roots, with zero exceptions.
- *Easy to type.* Plain a–z with no accents, spelled exactly as it sounds.
- *Easy to read.* A word's length and last letter tell you its job.
- *Made for human–AI talk.* Every sentence can say how sure the speaker is (**ve** sure, **pa** probably, **ga** guessing), and any missing word can be borrowed in [brackets].

## The whole grammar on one card

1. *Say what you see.* Each of the 21 letters has one sound. Vowels are as in Spanish or Italian. Stress goes on the first syllable.
2. *Two-letter words are grammar.* Longer words carry meaning.
3. *The last vowel shows the job.* A root ends in a consonant, and you add one vowel:

   | | | |
   |---|---|---|
   | **kod** | (none) | code, a thing |
   | **koda** | -a | codes, is coding |
   | **kodi** | -i | coded |
   | **kodo** | -o | will code |
   | **kodu** | -u | would code |
   | **kode** | -e | describing: code-ish |

4. *Subject, verb, object*, as in English: **Mi lova kaf.** I love coffee.
5. *Describers come after, little words come before:* **kat bone** (good cat), but **mu bone** (very good), **no bone** (not good), **po tu** (for you).
6. *Questions:* put **ka** in front for yes/no, or put **ke** where the answer goes: **Ka tu bona?** Are you good? **Tu vola ke?** What do you want?
7. *No exceptions, ever.* If you're missing a word, borrow it in [brackets].

The rest is in [GRAMMAR.md](GRAMMAR.md).

## A first conversation

| Clud | English |
|---|---|
| **Sal! Ka tu bona?** | Hi! How are you? |
| **Ya, mi bona, dank! Et tu?** | Yes, I'm good, thanks! And you? |
| **Mi mu hapa. Tu maka ke?** | I'm very happy. What are you doing? |
| **Mi lerna Klud. Ti lang fasa!** | I'm learning Clud. This language is easy! |
| **Pa tu lerno kwike.** | You'll probably learn quickly. |
| **Ka tu pova helpa mi po fiksa bug in kod mi?** | Can you help me fix a bug in my code? |
| **Ve ya! Pe mosa fil po mi.** | Of course! Please show me the file. |

## How we'll talk

I'll write in Clud and put the English underneath. As you get comfortable, adjust the mix:

- **Pe utila le Angl.** Please use less English.
- **Pe utila mo Angl.** Please use more English.
- **[word] siga ke?** What does [word] mean?
- If you're stuck mid-sentence, borrow the English word in [brackets] and keep going. **Mi vola [refactor] ti kod.**

## Files

| File | What it is |
|---|---|
| [GRAMMAR.md](GRAMMAR.md) | The complete grammar, with examples |
| [PHRASEBOOK.md](PHRASEBOOK.md) | Ready-made sentences for chatting and coding together |
| [LEXICON.md](LEXICON.md) | The dictionary, Clud → English and English → Clud (generated) |
| [lexicon.txt](lexicon.txt) | The source list of every word |
| [clud.py](clud.py) | A small tool to gloss sentences, look up words, and check the docs |

## The `clud.py` tool

```
$ python3 clud.py gloss "Ka tu vola lerna Klud?"
Ka     ka         (yes/no question)
tu     tu         you
vola   vol+a      want, wish  (doing, now)
lerna  lern+a     learn  (doing, now)
Klud   Klud       Clud, our language

$ python3 clud.py find coffee
kaf      thing     coffee
```

`python3 clud.py check` confirms that the lexicon follows the word-shape rules and that every bold Clud example in
these docs uses real words and has a verb where it needs one. `python3 -m unittest discover -s tests` runs the tests.

## Growing the language

Clud will grow as we use it. To add a word, add a line to `lexicon.txt`, then run
`python3 clud.py dict > LEXICON.md` and `python3 clud.py check`.
