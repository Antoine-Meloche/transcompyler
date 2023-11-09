from transcompyler.token import Token


def compare_tokens(
        token_list_1: list[Token],
        token_list_2: list[Token]
        ) -> bool:
    result = True

    for token_1, token_2 in zip(token_list_1, token_list_2):
        result &= token_1._type == token_2._type
        result &= token_1.val == token_2.val
        result &= token_1.line == token_2.line

    return result

