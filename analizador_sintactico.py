class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            raise SyntaxError(f"Invalid token: {self.current_token.type}")

    def factor(self):
        token = self.current_token
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            expr_value = self.expr()
            self.eat('RPAREN')
            return expr_value
        elif token.type == 'NUMBER':
            self.eat('NUMBER')
            return token.value
        else:
            raise SyntaxError(f"Token Invalido: {token.type}")

    def term(self):
        value = self.factor()

        while self.current_token.type in ['MULTIPLY', 'DIVIDE']:
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                value *= self.factor()
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
                denominator = self.factor()
                if denominator == 0:
                    raise ZeroDivisionError("Division by zero")
                value /= denominator

        return value

    def expr(self):
        value = self.term()

        while self.current_token.type in ['PLUS', 'MINUS']:
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                value += self.term()
            elif token.type == 'MINUS':
                self.eat('MINUS')
                value -= self.term()

        return value

    def parse(self):
        return self.expr()
