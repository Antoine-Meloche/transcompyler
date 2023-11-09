from transcompyler.token import Token


def create_token_str(token_list: list[Token]) -> str:
    return " ".join([token.val for token in token_list])
