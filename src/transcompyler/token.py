class Token(object):
    def __init__(self, _type: str, val: str, line: int) -> None:
        self._type = _type
        self.val = val
        self.line = line

    def __str__(self) -> str:
        return f"[{self.line}]: {self._type} = {self.val}"


def list_to_str_list(token_list: list[Token]) -> list[str]:
    token_str_list = []

    for token in token_list:
        token_str_list.append(token._type)

    return token_str_list
