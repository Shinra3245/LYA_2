from antlr4 import *
from ExprLexer import ExprLexer
import sys


input_stream = FileStream(sys.argv[1])


lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for tokens in tokens.tokens:
    print("Texto ", tokens.text)
    print("Línea ", tokens.line)
    print("Columna ", tokens.column)
    nombre_token = lexer.symbolicNames[tokens.type]
    print("Tipo ", nombre_token)
    
    print("--------")