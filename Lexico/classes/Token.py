class Token(object):

    indiceTs = None
    def __init__(self, nome, lexema, indiceTS = None):
        self.tipo = nome
        self.lexema = lexema
        if(indiceTS is not None):
            self.indiceTs = indiceTS
        