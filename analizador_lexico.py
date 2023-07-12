class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value


class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.current_pos = 0
        self.current_char = input_text[self.current_pos]

    def advance(self):
        self.current_pos += 1
        if self.current_pos < len(self.input_text):
            self.current_char = self.input_text[self.current_pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_number(self):
        number = ""
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return int(number)

    def next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token('NUMBER', self.get_number())

            if self.current_char == '/':
                self.advance()
                return Token('DIVIDE', '/')

            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')

            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return Token('MULTIPLY', '*')

            raise SyntaxError("Invalid token: " + self.current_char)

        return Token('EOF')
