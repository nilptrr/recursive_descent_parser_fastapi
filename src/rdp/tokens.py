class Token:
    '''
    Supported kinds of tokens:
        - digits: 0-9
        - unary operators: -
        - binary operators: +, -, *, /,
        - parenthesis: (, )
        - floating point: .
    '''
    def __init__(self, kind, value = 0) -> None:
        self.kind: str = kind               # kind of token
        self.value: int = value             # for digits: a value

    def __repr__(self) -> str:
        if self.kind == 'n':
            return str(self.value)               # for digit
        else:
            return str(self.kind)


class TokenStream:
    def __init__(self, tokens) -> None:
        self.tokens = tokens

    def peek(self):
        try:
            return self.tokens[0]
        except IndexError:
            return False

    def next(self):
        try:
            return self.tokens.popleft()
        except IndexError:
            return None
