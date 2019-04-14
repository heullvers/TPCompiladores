class Erro(object):

    def __init__(self, linha, coluna, caractere, descricao = None):
        self.linha = linha
        self.coluna = coluna
        self.caractere = caractere
        self.descricao = self.setDescricao(descricao)

    def setDescricao(self,descricao):
        if(descricao == 0):
            descricao = "Letra após digito"
        elif(descricao == 1):
            descricao = "Caractere inválido após ponto de separação do número flutuante"
        elif(descricao == 2):
            descricao = "Caractere não pertence a linguagem"
        
        
        