import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import clud  # noqa: E402


class LexiconTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexicon = clud.Lexicon()

    def test_lexicon_follows_the_word_shape_rules(self):
        self.assertEqual(self.lexicon.problems(), [])

    def test_root_plus_ending(self):
        word = self.lexicon.analyze("Kodi")
        self.assertEqual((word.role, word.parts, word.gloss), ("verb", "kod+i", "code, program"))
        self.assertEqual(self.lexicon.analyze("bone").role, "describing")
        self.assertEqual(self.lexicon.analyze("kod").role, "thing")

    def test_little_words_names_and_borrowings(self):
        self.assertEqual(self.lexicon.analyze("mi").gloss, "I, me")
        self.assertEqual(self.lexicon.analyze("Klod").role, "name")
        self.assertEqual(self.lexicon.analyze("[refactor]").role, "borrowed")
        self.assertEqual(self.lexicon.analyze("blorp").role, "unknown")

    def test_short_words_never_parse_as_verbs(self):
        # 'tri' (3) ends in -i but is a number, not the past tense of a root.
        self.assertEqual(self.lexicon.analyze("tri").role, "number")

    def test_clause_with_subject_needs_a_verb(self):
        self.assertTrue(self.lexicon.problems_in("Mi lov tu."))
        self.assertTrue(self.lexicon.problems_in("Pe mos fil po mi."))
        self.assertEqual(self.lexicon.problems_in("Pe mosa fil po mi."), [])
        self.assertEqual(self.lexicon.problems_in("Ya, mi bona, dank! Et tu?"), [])

    def test_docs_only_use_real_clud(self):
        self.assertEqual(clud.check_docs(self.lexicon), [])


if __name__ == "__main__":
    unittest.main()
