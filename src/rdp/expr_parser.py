from .tokens import TokenStream


class Parser:
    '''
    Grammar:
    expr: term | expr "+" term | expr "-" term
    term: factor | term "*" factor | term "/" factor
    factor: NUM | "-" NUM | "(" expr ")"
    '''
    def __init__(self, ts: TokenStream) -> None:
        self.ts = ts

    def parse(self):
        result = self._expr()
        return result

    def _expr(self):
        left = self._term()

        while self.ts.peek() and self.ts.peek().kind in '+-':
            op = self.ts.next()

            if op.kind == '+':
                left += self._term()

            elif op.kind == '-':
                left -= self._term()

            else:
                break

        return left

    def _term(self):
        left = self._factor()

        while self.ts.peek() and self.ts.peek().kind in '*/':
            op = self.ts.next()

            if op.kind == '*':
                left *= self._factor()

            elif op.kind == '/':
                divisible = self._factor()
                if divisible == 0:
                    raise ZeroDivisionError

                left = float(left) / float(divisible)

            else:
                break

        return left

    def _factor(self):
        left = self.ts.next()

        if left is None:
            return None

        elif left.kind == 'n':
            return left.value

        elif left.kind == '-':

            if self.ts.peek():
                t = self.ts.next()
                return -t.value

        elif left.kind == '+':
            if self.ts.peek():
                t = self.ts.next()
                return t.value            

        elif left.kind == '(':
            left = self._expr()

            if self.ts.peek():
                t = self.ts.next()

                if t.kind != ')':
                    raise ValueError(') required.')

            return left
