import unittest
from transcompyler.lexer import Lexer
from transcompyler.token import Token
from utils.compare_tokens import compare_tokens
from utils.create_token_str import create_token_str


class TestLexer(unittest.TestCase):
    def test_lexer(self) -> None:
        lexicon = [
            ["NUMBER", r"\d+"],
            ["ADD", r"\+"],
            ["SUB", r"\-"],
            ["MUL", r"\*"],
            ["DIV", r"\/"],
            ["LPAREN", r"\("],
            ["RPAREN", r"\)"],
        ]

        input_tokens = [
            Token("NUMBER", "3", 1),
            Token("ADD", "+", 1),
            Token("NUMBER", "2", 1),
            Token("MUL", "*", 1),
            Token("NUMBER", "2", 1),
        ]

        input_text = create_token_str(input_tokens)

        lexer = Lexer(lexicon)
        lexer.lex(input_text)

        self.assertEqual(compare_tokens(lexer.tokens, input_tokens), True)


if __name__ == "__main__":
    unittest.main()

