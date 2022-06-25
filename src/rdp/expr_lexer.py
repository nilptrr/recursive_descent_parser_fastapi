from collections import deque


def lexer(math_expr: str, Token):
    '''
    The lexical analyzer translates lexemes into tokens.
    '''
    tokens = deque()
    math_expr = deque(math_expr)


    while math_expr:
        c = math_expr.popleft()

        if c in '0123456789':
            nums = []
            nums.append(c)

            if not math_expr:
                t = Token('n', float(''.join(nums)))
                tokens.append(t)
                break

            c = math_expr.popleft()

            while c in '0123456789':
                nums.append(c)

                if not math_expr:
                    break

                c = math_expr.popleft()

            if c == '.':                            # for float nums
                nums.append(c)

                if not math_expr:
                    break

                c = math_expr.popleft()

                if c not in '0123456789':           # "2. / 1." case is not supported yet :(
                    nums.append('0')

                    if not math_expr:
                        break

                    c = math_expr.popleft()

                else:
                    while c in '0123456789':
                        nums.append(c)

                        if not math_expr:
                            break

                        c = math_expr.popleft()

                t = Token('n', float(''.join(nums)))
                tokens.append(t)
                math_expr.appendleft(c)

            else:
                math_expr.appendleft(c)
                t = Token('n', float(''.join(nums)))
                tokens.append(t)
                continue

        elif c in '+-*/()':
            t = Token(c)
            tokens.append(t)

        elif c == ' ':
            continue

        else:
            raise ValueError('Bad token.')

    return tokens
