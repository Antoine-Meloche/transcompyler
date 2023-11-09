import unittest
from transcompyler.generator import Generator
from transcompyler.token import Token


class TestGeneraator(unittest.TestCase):
    def test_generator(self) -> None:
        rev_lexicon: dict[str, str] = {
            "PRINT": "print",
            "PARENL": "(",
            "PARENR": ")",
        }

        input_tokens: list[Token] = [
            Token("PRINT", "", 1),
            Token("PARENL", "", 1),
            Token("NUMBER", "3", 1),
            Token("ADD", "+", 1),
            Token("NUMBER", "2", 1),
            Token("PARENR", "", 1),
        ]

        generator = Generator(rev_lexicon)

        expexted_output: str = "print(3+2)"

        generator.generate(input_tokens)

        self.assertEqual(generator.output, expexted_output)


if __name__ == "__main__":
    unittest.main()

