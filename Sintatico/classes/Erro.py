class Erro(object):

    def __init__(self, linha, descricao = None):
        self.linha = linha
        self.descricao = self.setDescricao(descricao)

    def setDescricao(self,descricao):
        if(descricao == 0):
            self.descricao = "Erro declaracao_lista"
        elif(descricao == 1):
            self.descricao = "Erro declaracao"
        elif(descricao == 2):
            self.descricao = "Caractere não pertence a linguagem"
        elif(descricao == 3):
            self.descricao = "Comentário não foi fechado"
        elif(descricao == 4):
            self.descricao = "Exclamação não é reconhecido pela linguagem. Talvez você quis dizer !="

        return self.descricao
        
        
        