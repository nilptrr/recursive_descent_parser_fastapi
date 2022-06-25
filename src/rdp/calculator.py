from .tokens import Token, TokenStream
from . import expr_parser
from . import expr_lexer


def calculate(expr: str):
    tokens = expr_lexer.lexer(expr, Token)
    ts = TokenStream(tokens)
    parser = expr_parser.Parser(ts)

    try:
        expr_result = parser.parse()        

    except Exception:
        raise

    else:
        return round(expr_result, 3)
