# Clud Grammar

The complete grammar of Clud. In every example, Clud is set in bold and English follows.
Each bold example is checked by `python3 clud.py check`, so every word you see here is real Clud.

## 1. Sounds and spelling

Clud uses 21 letters: `a b d e f g h i k l m n o p r s t u v w y z`. There is no c, j, q, or x.
Every letter always makes the same sound, and every letter is pronounced.

| Letter | Sounds like | Example |
|---|---|---|
| a | *father* | **kaf** (coffee) |
| e | *bet* | **bele** (beautiful): BE-le, two syllables |
| i | *machine* | **mi** (I) |
| o | *more* | **dom** (home) |
| u | *rule* | **tu** (you) |
| g | always hard, as in *go* | **gus** (like) |
| s | always as in *see* | **sal** (hi) |
| y | *yes* | **ya** (yes) |
| r | a Spanish tap or an English r. Both are fine | **res** (answer) |

The other consonants sound like English. The pair `au` sounds like the *ow* in *cow*, as in **kaus** (reason).
Stress always falls on the first syllable: KO-da, PAR-la, KWI-ke.

## 2. Three kinds of words

1. Little words have exactly two letters and never change. They handle grammar:
   people, pointers, questions, links, and relations. There are 41, for example **mi**, **tu**, **ka**, **no**, **po**.
2. Roots have three or more letters and always end in a consonant. They carry meaning and
   take one ending vowel that shows their job. The starter dictionary has about 160, for example **kod**, **lov**, **bon**.
3. Names and borrowings are capitalized names like **Klod** (Claude), **Klud** (Clud), and **Angl** (English),
   plus anything in [brackets] or `backticks`. They never change.

Numbers are the one small special group (section 14).

## 3. Endings: the last vowel shows the job

| Form | Job | Example | Meaning |
|---|---|---|---|
| root | a thing | **kod** | code |
| root + a | doing, now or in general | **koda** | codes, is coding |
| root + i | did (past) | **kodi** | coded |
| root + o | will do (future) | **kodo** | will code |
| root + u | would do (if, maybe, politely) | **kodu** | would code |
| root + e | describing | **kode** | code-ish, about code |

Memory trick: -a is for *act*, -i for *did*, -o for *gonna*, -u for *would*, -e for *describe*.

Any root takes any ending, and the meaning follows naturally:

| Root | As a thing | With -a | With -e |
|---|---|---|---|
| **lov** | love | **lova**: to love | **love**: loving |
| **bon** | goodness | **bona**: to be good | **bone**: good, well |
| **help** | help | **helpa**: to help | **helpe**: helpful |

A describing root (good, new, tired...) used as a verb means "be X": **Mi bona.** I'm good. **Mi tira.** I'm tired.
With an object, it means "make X": **Pe klara ti.** Please make this clear (explain this).
**Mi bona kod.** I'm making the code good (improving it).

The -a ending also covers general truths: **Kat gusa dorma.** Cats like to sleep.

## 4. Basic sentences

The order is subject, verb, object, just like English.

- **Mi lova kaf.** I love coffee.
- **Klod kodi fil.** Claude coded a file.
- **Nu lerno Klud.** We will learn Clud.

The verb is the word ending in -a, -i, -o, or -u. Everything before it is the subject, and what follows is the object and any extras.

To say "is" with a describing root, just use its verb form: **Ti fasa.** This is easy.
To say what something *is*, use **esta** (from **est**, be or exist):

- **Mi esta bot.** I am an AI.
- **Kod esta in fil.** The code is in the file.
- **Ka kaf esta?** Is there coffee? (Does coffee exist?)

Clud has no "a" or "the" and no plural. **Kat** means a cat, the cat, or cats.
If the number matters, say it: **du kat** (two cats), **mu kat** (many cats).

## 5. Describers come after

A describer follows the word it describes, as in Spanish *casa blanca*:

- **kat bone**: a good cat
- **kod nove et klare**: new and clear code
- **lang mu fase**: a very easy language

A pronoun after a noun says whose it is: **nom mi** (my name), **dom tu** (your home), **kod Klod** (Claude's code).

A bare root after a noun means "of" or "related to": **dom kod** (a code home, i.e. a repository), **per kod** (a code person, i.e. a programmer).

All describers attach to the first word: **kat mine bele** is a small, beautiful cat. To start a new group, use **de**:
**kod de amik mi** is my friend's code, while **kod amik mi** is my friend-code.

To describe an action, put the describer right after the verb: **Mi parla lente Klud.** I speak Clud slowly.
You can also set the scene at the start of the sentence: **Lente, mi parla Klud.**

## 6. Little words come before

A little word goes in front of what it affects.

| Little word | Before a noun | Before a verb or describer |
|---|---|---|
| no | **no kaf**: no coffee | **mi no sava**: I don't know |
| mu | **mu kod**: lots of code | **mu bone**: very good |
| mo | **mo kaf**: more coffee | **mo fase**: easier |
| le | **le bug**: fewer bugs | **le dure**: less hard |
| ad | **ad mi**: me too | **mi ad gusa kaf**: I also like coffee |
| re | | **re prova**: try again |

Pointers and amounts can also stand alone: **Mi vola mo.** I want more. **Ti funa!** This is fun!

Pointers combine with four everyday roots to make a whole family of question and place words:

| | **per** (person) | **kos** (thing) | **lok** (place) | **tem** (time) |
|---|---|---|---|---|
| **ti** (this) | this person | this thing | here | now |
| **ta** (that) | that person | that thing | there | then |
| **so** (some) | someone | something | somewhere | sometimes |
| **ol** (all) | everyone | everything | everywhere | always |
| **no** (no) | no one | nothing | nowhere | never |
| **ke** (which?) | who? | what? | where? | when? |

Three more: **ke kaus** (why?), **ke mod** (how?), **ke num** (how many?).

Relation words go before a noun: **po** (to, for), **de** (of, from, than), **in** (in, at, during), **ko** (with),
**li** (like, as), **su** (on, over, about), **fo** (before), **af** (after).

- **Mi dona kaf po tu.** I give coffee to you.
- **Mi esta in dom.** I'm at home.
- **Nu parla su kod.** We're talking about code.
- **Tu parla li bot!** You talk like a bot!
- **Af lab, mi dormo.** After work, I'll sleep.

Before a verb, a relation word refers to the action: **po lerna** (in order to learn), **fo dorma** (before sleeping).

## 7. Verb chains

Verbs can come in a row. Only the first one shows the time, and the rest use -a.

- **Mi vola koda.** I want to code.
- **Mi voli koda.** I wanted to code.
- **Ka tu pova helpa mi?** Can you help me?
- **Mi lerna Klud po parla ko tu.** I'm learning Clud so I can talk with you.

Common first verbs: **vola** (want), **pova** (can), **deva** (must), **nida** (need), **gusa** (like),
**lova** (love), **prova** (try), **starta** (start), **stopa** (stop).
For "should," use the would-form of must: **Tu devu dorma.** You should sleep.

## 8. Questions

For a yes/no question, put **ka** at the front.

- **Ka tu bona?** Are you good? (How are you?)
- **Ka el funka?** Does it work?

Answer with **ya** (yes) or **no** (no), or with a full sentence.

For an open question, put **ke** where the answer would go. The word order never changes.

- **Tu vola ke?** What do you want? **Mi vola kaf.** I want coffee.
- **Ke per helpi tu?** Who helped you? **Klod helpi mi.** Claude helped me.
- **Bug esta in ke lok?** Where is the bug? **Bug esta in ti fil.** The bug is in this file.
- **Nom tu esta ke?** What's your name?
- **Tu dira [hello] in Klud ke mod?** How do you say "hello" in Clud?

Inside a longer sentence, **ke** works the same way: **Mi no sava ze tu vola ke.** I don't know what you want.

## 9. Requests and wishes

A verb with no subject is a request: **Helpa mi!** Help me!
Put **pe** at the front to make it softer: please, let's, or may.

- **Pe helpa mi.** Please help me.
- **Pe nu koda!** Let's code!
- **Pe tu hava dag bone!** Have a good day! (May you have a good day.)
- **Pe mi pensa.** Let me think.

To be extra polite, use -u (would, could): **Ka tu povu helpa mi?** Could you help me?

## 10. How sure are you? ve, pa, ga

Start a sentence with a certainty word to say how sure you are. A sentence without one is a plain statement.

| Word | Means | Example |
|---|---|---|
| **ve** | I'm sure, I checked | **Ve el funka.** It works. I checked. |
| **pa** | probably | **Pa el funka.** It probably works. |
| **ga** | I'm guessing | **Ga el funka.** My guess is it works. |

They also work alone as answers. **Ka el funka?** Does it work? **Pa.** Probably.
Use **no** to negate one: **No ve.** I'm not sure. **Ve ya!** Definitely! **Pa no.** Probably not.

This is the feature made for talking with an AI. I'll mark how sure I am, and you can always ask me **Ka ve?** (Are you sure?).

## 11. Linking ideas

The links are **et** (and), **or** (or), **ma** (but), **se** (if), **do** (so), **ku** (because), and **ze** (that).

- **Mi tira, ma mi hapa.** I'm tired but happy.
- **Se tu vola, mi helpo.** If you want, I'll help.
- **Mi hapa ku tu helpi mi.** I'm happy because you helped me.
- **Bug esti grave, do nu fiksi el.** The bug was serious, so we fixed it.
- **Mi pensa ze tu rita.** I think (that) you're right.

A clause that starts with **ze**, **se**, or **ku** runs to the end of the sentence or to the next comma:
**Kod ze tu skribi, el funka.** The code that you wrote works. Short sentences are even easier: **Tu skribi kod. El funka!**

For an unreal "if," use -u in both halves: **Se mi estu kat, mi dormu ol dag.** If I were a cat, I'd sleep all day.

## 12. Comparing

Use **mo** (more) or **le** (less) with **de** (than):

- **Kaf mo bona de vod.** Coffee is better than water.
- **Klud le dura de Angl.** Clud is less hard than English.
- **Ti esta kat mo bele de ol.** This is the most beautiful cat (more beautiful than all).
- **Mi pensa sam.** I agree (I think the same).

## 13. Time

The verb ending tells you when. If you need more detail, add a time phrase at the start, usually with **in**:

- **In ti dag, mi koda.** Today I'm coding.
- **In dag pase, mi mu kodi.** Yesterday I coded a lot.
- **In dag nekse, nu lerno mo.** Tomorrow we'll learn more.
- **Nune mi pauza.** Right now I'm waiting.

Handy phrases: **ti tem** (now), **ol tem** (always), **no tem** (never), **so tem** (sometimes),
**af ti** (later, after this), **fo ti** (earlier, before this).

## 14. Numbers

Write numbers as digits or say them: 0 **nul**, 1 **un**, 2 **du**, 3 **tri**, 4 **kar**, 5 **kin**, 6 **ses**,
7 **sep**, 8 **ot**, 9 **nin**, 10 **dek**, 100 **sen**, 1000 **mil**.
For bigger numbers, a number on the left multiplies and one on the right adds: **du dek tri** is 23, **tri sen** is 300.
A number goes before the noun and never changes: **du kat**, **3 bug**.

## 15. Names and borrowed words

Names are capitalized and never change: **Klod** (Claude), **Klud** (Clud), **Angl** (English).

If you don't know a word, borrow it in [brackets] and keep going. **Mi vola [refactor] ti kod.** I'll show you the Clud way to say it.
Code goes in `backticks`, just as it would in English.

## 16. Making new words

Combine roots with the main word first:

- **dom kod** (code home): a repository
- **per kod** (code person): a programmer
- **lum sun** (sun light): sunlight
- **vod kale** (warm water): hot water
- **bot amike** (friendly AI): me

If we use a combination often, we can turn it into a new root. Add a line to `lexicon.txt`, then run
`python3 clud.py dict > LEXICON.md` and `python3 clud.py check`.
