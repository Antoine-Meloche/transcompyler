from transcompyler.token import Token
from .utils.errors import GeneratorError


class Generator:
    def __init__(self,
                 rev_lexicon: dict[str, str],
                 start_code: str = "",
                 end_code: str = ""
                 ) -> None:
        self.rev_lexicon: dict[str, str] = rev_lexicon
        self.start_code: str = start_code
        self.end_code: str = end_code

    def generate(self, tokens: list[Token]) -> None:
        self.tokens: list[Token] = tokens

        self.output: str = ""

        self.output += self.start_code

        for token in tokens:
            if token.val != "":
                self.output += token.val
            else:
                try:
                    self.output += self.rev_lexicon[token._type]
                except Exception:
                    raise GeneratorError(token._type)

        self.output += self.end_code

