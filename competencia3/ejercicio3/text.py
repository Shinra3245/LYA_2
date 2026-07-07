from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

entrada = input("Codigo: ");
lexer = ExprLexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
    print("El codigo es correcto")
    print("Arbol sintactico:")

    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo tiene errores de sintaxis")
print("ola, pero no ola de mar, ola de saludo")
