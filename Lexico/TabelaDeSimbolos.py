from Simbolo import *
class TabelaDeSimbolos(object):

    def __init__(self, tokens):
        self.tabela = self.setTabela(tokens)

    def setTabela(self,tokens):
        tabela = {}
        for token in tokens:
            if((token.tipo.value == 2) or (token.tipo.value == 3) or (token.tipo.value == 24)): #número inteiro, número flutuante e identificador
                tabela[token.indiceTs] = Simbolo(token.lexema, token.indiceTs)
        return tabela
    


        
        