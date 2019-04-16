class Erro(object):

    def __init__(self, linha, coluna, caractere, descricao = None):
        self.linha = linha + 1
        self.coluna = coluna + 1
        self.caractere = caractere
        self.descricao = self.setDescricao(descricao)

    def setDescricao(self,descricao):
        if(descricao == 0):
            self.descricao = "Letra após digito"
        elif(descricao == 1):
            self.descricao = "Caractere inválido após ponto de separação do número flutuante"
        elif(descricao == 2):
            self.descricao = "Caractere não pertence a linguagem"
        elif(descricao == 3):
            self.descricao = "Comentário não foi fechado"
        elif(descricao == 4):
            self.descricao = "Exclamação não é reconhecido pela linguagem. Talvez você quis dizer !="

        return self.descricao
        
        
        