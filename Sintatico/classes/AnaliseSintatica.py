class AnaliseSintatica:
    def __init__(self, tokens):
        print('sinatico')
        self.arrayTokens = tokens
        self.posicao = 0

    def setPosicao(self):
        self.posicao += 1

    def match(self, esperado):
        if(esperado == arrayTokens[self.posicao].lexema):
            return True
        else:
            return False

    def analisar(self):
        

        
