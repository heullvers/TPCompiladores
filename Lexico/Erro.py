class Erro(object):

    def __init__(self, linha, coluna, caractere, descricao = None):
        self.linha = linha
        self.coluna = coluna
        self.caractere = caractere
        self.descricao = descricao
        