class LexerError(Exception):
    def __init__(self, val: str, line: int) -> None:
        self.val: str = val
        self.line: int = line
    
    def __str__(self):
        return f"\033[91m[ERR]\033[0m Invalid token: '{self.val}' at line {self.line}"


class GrammarError(Exception):
    def __init__(self, tokens: str, line: int) -> None:
        self.tokens: str = tokens
        self.line: int = line
    
    def __str__(self):
        return f"\033[91m[ERR]\033[0m Invalid syntax: '{self.tokens}' at line {self.line}"
    

class GeneratorError(Exception):
    def __init__(self, token_type: str) -> None:
        self.token_type: str = token_type

    def __str__(self):
        return f"\033[91m[ERR]\033[0m Invalid token: '{self.token_type}'"


class TranscompylerError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg: str = msg
    
    def __str__(self):
        return f"\033[91m[ERR]\033[0m {self.msg}"