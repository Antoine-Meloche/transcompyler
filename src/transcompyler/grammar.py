import transcompyler.token as token
from transcompyler.token import Token
from .utils.errors import GrammarError


class Grammar:
    def __init__(self, translation_grammar: list) -> None:
        self.translation_grammar: list = translation_grammar
        self.output_tokens: list[Token] = []

    def translate(self, input_tokens: list[Token]) -> None:
        self.input_tokens: list[Token] = input_tokens

        while self.input_tokens:
            self.check_all_rules()

    def check_all_rules(self) -> None:
        for rule in self.translation_grammar:
            self.check_rule(rule)
        else:
            if self.input_tokens:
                raise GrammarError(
                        " ".join(token.list_to_str_list(self.input_tokens)),
                        self.input_tokens[0].line
                        )

    def check_rule(self, rule: list) -> None:
        rule_types: list[str] = rule[0].split(" ")
        input_types: list[str] = token.list_to_str_list(self.input_tokens)

        if input_types[:len(rule_types)] == rule_types:
            self.apply_rule(rule)

    def apply_rule(self, rule: list) -> None:
        for i, otoken in enumerate(rule[1].split(" ")):
            in_index: int = rule[2][i]
            if in_index != -1:
                self.output_tokens.append(self.input_tokens[in_index])
            else:
                self.output_tokens.append(
                        Token(otoken,
                              "",
                              self.input_tokens[0].line
                              )
                        )

        self.input_tokens = self.input_tokens[len(rule[0].split(" ")):]

