class Token(object):

    indiceTs = None
    def __init__(self, nome, lexema, linha, coluna, indiceTS = None):
        self.tipo = nome
        self.lexema = lexema
        self.linha = linha + 1
        self.coluna = self.setColuna(lexema, coluna)
        if(indiceTS is not None):
            self.indiceTs = indiceTS
        self.imprimirToken()

    def setColuna(self, lexema, coluna):
        if(lexema != 'identInvalido'):
            self.coluna = coluna - len(lexema) + 1
        else:
            self.coluna = coluna

        return self.coluna

    def imprimirToken(self):
        print('Lexema:', self.lexema, ', Tipo:', self.tipo.name, ', Linha:' , self.linha, ' Posição: ', self.coluna)
