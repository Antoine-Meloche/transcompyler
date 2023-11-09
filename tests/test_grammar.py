import unittest
from transcompyler.token import Token
from transcompyler.grammar import Grammar
from utils.compare_tokens import compare_tokens


class TestGrammar(unittest.TestCase):
    def test_grammar(self) -> None:
        translation_grammar: list = [
            ["NUMBER ADD NUMBER", "PRINT PARENL NUMBER ADD NUMBER PARENR",
             [-1, -1, 0, 1, 2, -1]],

            ["NUMBER SUB NUMBER", "PRINT PARENL NUMBER SUB NUMBER PARENR",
             [-1, -1, 0, 1, 2, -1]],

            ["NUMBER MUL NUMBER", "PRINT PARENL NUMBER MUL NUMBER PARENR",
             [-1, -1, 0, 1, 2, -1]],

            ["NUMBER DIV NUMBER", "PRINT PARENL NUMBER DIV NUMBER PARENR",
             [-1, -1, 0, 1, 2, -1]],

            ["NUMBER", "PRINT PARENL NUMBER PARENR",
             [-1, -1, 0, -1]],
        ]

        grammar = Grammar(translation_grammar)

        input_tokens = [
            Token("NUMBER", "3", 1),
            Token("ADD", "+", 1),
            Token("NUMBER", "2", 1),
        ]

        grammar.translate(input_tokens)

        expected_tokens = [
            Token("PRINT", "", 1),
            Token("PARENL", "", 1),
            Token("NUMBER", "3", 1),
            Token("ADD", "+", 1),
            Token("NUMBER", "2", 1),
            Token("PARENR", "", 1),
        ]

        self.assertEqual(
                compare_tokens(grammar.output_tokens,
                               expected_tokens),
                True
                )


if __name__ == "__main__":
    unittest.main()

