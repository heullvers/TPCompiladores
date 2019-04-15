class Erro(object):

    def __init__(self, linha, coluna, caractere, descricao = None):
        self.linha = linha
        self.coluna = coluna
        self.caractere = caractere
        self.descricao = self.setDescricao(descricao)

    def setDescricao(self,descricao):
        if(descricao == 0):
            self.descricao = "Letra após digito"
        elif(descricao == 1):
            self.descricao = "Caractere inválido após ponto de separação do número flutuante"
        elif(descricao == 2):
            self.descricao = "Caractere não pertence a linguagem"
        return self.descricao
        
        
        