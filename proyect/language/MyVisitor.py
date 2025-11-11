from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    #Definimos la memoria o el entorno
    def __init__(self):
        self.memory = { }
        
    #Definimos la assignacion
    def visitAssing(self,ctx):
        #se obtiene el id o nombre de la variable
        name=ctx.ID().getText()#obtenemos id
        #se obtiene el valor, ya sea un valor numerico o una expresion
        value=self.visit(ctx.expr())#obtenemos el valor que se le quiere asignar al id
        #Se almacena en memoria a partir del nombre y el valor
        self.memory[name]=value
        
    #definimos la assignacion
    def visitPrintExpr(self,ctx):
        #Definimos la expresion que se desea mostrar 
        value=self.visit(ctx.expr())
        # imprime el valor 
        print(value) 
        
    #efinimos la parte de las expresiones
    def visitExpr(self,ctx):
        #Busca si existen ID'S
        if ctx.ID():
            #Obtiene del contexto el nombre de la variable
            name=ctx.ID().getText()
            # si el nombre de la variable no esta, lanza un error
            if name not in self.memory:
                raise NameError(f"Variable'{name}' no definida")
            #Si existe el nombre retorna la variable
            return self.memory[name]
        #Busca el operador
        elif ctx.op:
            # Visita y obtiene lado izquierdo 
            left=self.visit(ctx.expr(0))
            # Visita y obtiene lado derecho 
            right=self.visit(ctx.expr(1))
            #evalua la operacion a realizar
            if ctx.op.text=="+":
                return left + right
            if ctx.op.text=="-":
                return left - right
            if ctx.op.text=="*":
                return left * right
            if ctx.op.text=="/":
                #Verifica la division de cero
                if right==0:
                    raise ValueError("Division por cero")
                return left / right