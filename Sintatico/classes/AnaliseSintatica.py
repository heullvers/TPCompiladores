class AnaliseSintatica:
    def __init__(self, tokens):
        print('sinatico')
        self.arrayTokens = tokens
        self.posicao = 0
        self.programa()

    def setPosicao(self):
        self.posicao += 1

    def match(self, esperado):
        if(esperado == self.arrayTokens[self.posicao].lexema):
            self.setPosicao()
            print('deu match')
            return True
        else:
            self.setPosicao()
            print('nao deu match')
            return False
    
    def proximo(self):
        return self.arrayTokens[self.posicao + 1].lexema
    
    def programa(self):
        self.declaracao_lista()

    def declaracao_lista(self):
        self.declaracao()

    def declaracao(self):
        if(self.var_declaracao()):
            print('var_declaracao tudo certo')
            tudoCerto = True
        elif(self.fun_declaracao()):
            print('fun_declaracao tudo certo')
            tudoCerto = True
        else:
            tudoCerto = False
            print('erro sintatico declaracao')
        return tudoCerto

    def var_declaracao(self):
        tudoCerto = True
        contador = 0
        while(tudoCerto and contador < 1): #enquanto não foi encotrado erro e será executado apenas uma vez até o final
            if(not self.tipo_especificador()):
                print('erro sintatico var_declaracao 1')
                tudoCerto = False
                break
            if(not self.ident()):
                print('erro sintatico var_declaracao 2')
                tudoCerto = False
                break
            if(proximo() == ';'):
                self.match(';')
            elif(self.abre_colchete()):
                if(not self.num_int()):
                    print('erro sintatico var_declaracao 3')
                    tudoCerto = False
                    break
                if(not self.fecha_colchete()):
                    print('erro sintatico var_declaracao 4')
                    tudoCerto = False
                    break
                if(not self.match(';')):
                    print('erro sintatico var_declaracao 5')
                    tudoCerto = False
                    break
            else:
                print('erro sintatico oficial var_declaracao')
                tudoCerto = False
                break
            contador += 1
        
        return tudoCerto
    
    def abre_colchete(self):
        return self.match('[')

    def tipo_especificador(self):
        if(self.proximo() == 'int'):
            self.match('int')
        elif(self.proximo() == 'float'):
            self.match('float')
        elif(self.proximo() == 'void'):
            self.match('void')
        elif(self.proximo() == 'struct):
            self.match('struct')
            self.ident()
            self.abre_chave()
            self.atributos_declaracao()
            self.fecha_chave()
        else:
            print('erro sintatico tipo_especificador')
            return False
        
        print('tipo_especificador')
        return False

    def atributos_declaracao(self):
        self.var_declaracao()

    def fun_declaracao(self):
        self.tipo_especificador()
        self.ident()
        self.match('(')
        self.params()
        self.match(')')
        self.composto_decl()

    def params(self):
        if(self.proximo() == 'void'):
            self.match('void')
        else:
            self.param_lista()

    def param_lista(self):
        self.param()
        while(self.proximo() == ','):
            self.param()

    def param(self):
        self.tipo_especificador()
        self.ident()

    #def analisar(self):
'''
    def chamada(self):
        print(self.segundaChamada())
        print('chamada')

    def segundaChamada(self):
        return self.terceiraChamada()
        print('segunda chamada')
    
    def terceiraChamada(self):
        print('terceira chamada')
        return True
'''