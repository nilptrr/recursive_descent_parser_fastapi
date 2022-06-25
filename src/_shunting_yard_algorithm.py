from collections import deque


# Принять строку
# Преобразовать в постфиксную форму
# Распарсить постфиксную форму и вычислить


def main(math_exprs):
    for expr in math_exprs:
        postfix_expr = infix_to_postfix_convert(expr)
        result = calc(postfix_expr)
        return result


def calc(tokens:deque):
    operand_stack = deque()
    operators = '+-*/'

    for token in tokens:

        if token in '0123456789':
            operand_stack.append(int(token))

        elif token == '.':
            b = int(operand_stack.pop())
            a = int(tokens.pop())
            number = a + (b * 0.1)

            operand_stack.append(number)

        elif token in operators:
            b = operand_stack.pop()
            a = operand_stack.pop()

            if token == '+':
                res = a + b

            elif token == '-':      # may be unary or binary
                # TODO the unary operator not supported
                res = a - b

            elif token == '*':
                res = a * b

            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError
                res = a / b

            operand_stack.append(res)

    return res


def infix_to_postfix_convert(infix_expr: str):
    # tokens = infix_expr.split()
    print(infix_expr.split())
    tokens = deque(infix_expr.split())

    rpn = []                # Reverse Polish notation

    operationPriority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '~': 4
    }

    operators_stack = deque()

    while tokens:
        token = tokens.pop()

        if token in '0123456789' or token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            rpn.append(token)

        elif token == '(':
            operators_stack.append(token)

        elif token == ')':
            top_token = operators_stack.pop()

            while top_token != '(':
                rpn.append(top_token)
                top_token = operators_stack.pop()

        elif token == '.':
            b = int(rpn.pop())
            a = int(tokens.pop())
            num = a + (b * 0.1)
            rpn.append(num)

        else:
            while operators_stack and (operationPriority[operators_stack[-1]] >= operationPriority[token]):
                rpn.append(operators_stack.pop())

            operators_stack.append(token)

    while operators_stack:
        rpn.append(operators_stack.pop())

    return ' '.join(rpn)
