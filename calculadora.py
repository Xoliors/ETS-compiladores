import sys
from analizador_lexico import Lexer
from analizador_sintactico import Parser


def main():
    while True:
        input_text = input('')
        if input_text.lower() == 'salir':
            break

        lexer = Lexer(input_text)
        while True:
            token = lexer.next_token()
            if token.type == 'EOF':
                break
            print(f"Lexema: {token.type}   Valor: {token.value}")

        lexer = Lexer(input_text)
        parser = Parser(lexer)

        result = parser.parse()
        print("Resultado:", result)


if __name__ == '__main__':
    main()

