from antlr4 import*
from language.GrammarLexer import GrammarLexer
from language.GrammarParser import GrammarParser
import io
import sys
from language.MyVisitor import MyVisitor

def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()
    
    #Capturan la salida 
    old_stdout=sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf
    
    #creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    #visitamos el arbol con nuestro visitor
    visitor.visit(tree)
    #capturamos la salida
    output=buf.getvalue()
    
    return output