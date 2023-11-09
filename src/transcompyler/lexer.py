from .token import Token
import re
from typing import Union, Match
from .utils.errors import LexerError


class Lexer(object):
    def __init__(self, lexicon: list[list[str]]) -> None:
        self.lexicon: list[list[str]] = lexicon

    def lex(self, code: str) -> None:
        self.code: str = code
        self.tokens: list[Token] = []

        def add(token_type: str, value: str, line: int) -> None:
            token: Token = Token(token_type, value, line)
            self.tokens.append(token)

        line: int = 1
        while self.code:
            if re.match(r"^\n", self.code):
                line += 1
                continue
            elif re.match(r"^\s", self.code):
                self.code = self.code[1:]
                continue

            for token_type in self.lexicon:
                pattern: str = f"^{token_type[1]}"
                match: Union[Match[str], None] = re.match(pattern, self.code)

                if match:
                    add(token_type[0], match.group(0), line)
                    self.code = self.code[len(match.group(0)):]
                    break
            else:
                raise LexerError(self.code[0], line)

