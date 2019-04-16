class Token(object):

    indiceTs = None
    def __init__(self, nome, lexema, linha, coluna, indiceTS = None):
        self.tipo = nome
        self.lexema = lexema
        self.linha = linha + 1
        self.coluna = coluna - len(lexema) + 1
        if(indiceTS is not None):
            self.indiceTs = indiceTS
        self.imprimirToken()

    def imprimirToken(self):
        print('Lexema:', self.lexema, ', Tipo:', self.tipo.name, ', Linha:' , self.linha, ' Coluna: ', self.coluna, ' Indice:', self.indiceTs)
