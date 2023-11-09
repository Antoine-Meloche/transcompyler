from transcompyler.generator import Generator
from transcompyler.grammar import Grammar
from transcompyler.lexer import Lexer
from transcompyler.utils.errors import TranscompylerError


class Transcompiler:
    def __init__(self,
                 lexer: Lexer | None = None,
                 grammar: Grammar | None = None,
                 generator: Generator | None = None
                 ) -> None:
        self.lexer: Lexer | None = lexer
        self.grammar: Grammar | None = grammar
        self.generator: Generator | None = generator

    def transcompile(self,
                     input_str: str,
                     file_name: str = "",
                     save: bool = False
                     ) -> str:
        if not self.lexer:
            raise TranscompylerError("Lexer must be set before transcompiling \
                    code.")
        if not self.grammar:
            raise TranscompylerError("Grammar must be set before \
                    transcompiling code.")
        if not self.generator:
            raise TranscompylerError("Generator must be set before \
                    transcompiling code.")

        self.lexer.lex(input_str)
        self.grammar.translate(self.lexer.tokens)
        self.generator.generate(self.grammar.output_tokens)

        if not save:
            return self.generator.output

        self.save_to_file(self.generator.output, file_name)

    def save_to_file(self, input_str: str, file_path: str) -> None:
        try:
            with open(file_path, "w") as f:
                f.write(self.transcompile(input_str))
        except FileNotFoundError:
            raise TranscompylerError(f"File '{file_path}' \
                    could not be written to")
