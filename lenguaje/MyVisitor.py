from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = { }
        
    #Definimos la assignacion
    def visitAssing(self,ctx):
        name=ctx.ID().getText()#obtenemos id
        value=self.visit(ctx.expr())#obtenemos el valor que se le quiere asignar al id
        self.memory[name]=value
    #definimos la assignacion
    def visitPrintExpr(self,ctx):
        value=self.visit(ctx.expr())
        print(value) 