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
            print('erro sintatico oficial declaracao')
            return tudoCerto

        print('declaracao tudo certo')
        return tudoCerto

    def var_declaracao(self):
        tudoCerto = True
        if(not self.tipo_especificador()):
            print('erro sintatico var_declaracao 1')
            tudoCerto = False
            return tudoCerto
        print('var_declaracao correto 1')
        if(not self.ident()):
            print('erro sintatico var_declaracao 2')
            tudoCerto = False
            return tudoCerto
        print('var_declaracao correto 2')
        if(proximo() == ';'):
            self.match(';')
            print('var_declaracao correto 3')
        elif(self.abre_colchete()):
            if(not self.num_int()):
                print('erro sintatico var_declaracao 3')
                tudoCerto = False
                return tudoCerto
            if(not self.fecha_colchete()):
                print('erro sintatico var_declaracao 4')
                tudoCerto = False
                return tudoCerto
            if(not self.match(';')):
                print('erro sintatico var_declaracao 5')
                tudoCerto = False
                return tudoCerto
        else:
            print('erro sintatico oficial var_declaracao')
            tudoCerto = False
            return tudoCerto
        
        print('var_declaracao tudo certo ')
        return tudoCerto

    def tipo_especificador(self):
        tudoCerto = True
        if(self.proximo() == 'int'):
            self.match('int')
            print('tipo_especificador correto 1')
        elif(self.proximo() == 'float'):
            self.match('float')
            print('tipo_especificador correto 2')
        elif(self.proximo() == 'void'):
            self.match('void')
            print('tipo_especificador correto 3')
        elif(self.proximo() == 'struct):
            self.match('struct')
            print('tipo_especificador struct')
            if(not self.ident()):
                print('erro sintatico tipo_especificador 1')
                tudoCerto = False
                return tudoCerto
            if(not self.abre_chave()):
                print('erro sintatico tipo_especificador 2')
                tudoCerto = False
                return tudoCerto
            if(not self.atributos_declaracao()):
                print('erro sintatico tipo_especificador 3')
                tudoCerto = False
                return tudoCerto
            if(not self.fecha_chave()):
                print('erro sintatico tipo_especificador 4')
                tudoCerto = False
                return tudoCerto
        else:
            print('erro sintatico oficial tipo_especificador')
            tudoCerto = False
            return tudoCerto
        
        return tudoCerto

    def atributos_declaracao(self):
        return self.var_declaracao()

    def fun_declaracao(self):
        tudoCerto = True
        if(not self.tipo_especificador()):
            tudoCerto = False
            print('erro sintatico fun_declaracao 1')
            return tudoCerto
        if(not self.ident()):
            tudoCerto = False
            print('erro sintatico fun_declaracao 2')
            return tudoCerto
        if(not self.match('(')):
            tudoCerto = False
            print('erro sintatico fun_declaracao 3')
            return tudoCerto
        if(not self.params()):
            tudoCerto = False
            print('erro sintatico fun_declaracao 4')
            return tudoCerto
        if(not self.match(')')):
            tudoCerto = False
            print('erro sintatico fun_declaracao 5')
            return tudoCerto
        if(not self.composto_decl()):
            tudoCerto = False
            print('erro sintatico fun_declaracao 6')
            return tudoCerto
        
        print('fun_declaracao tudo certo')
        return tudoCerto

    def params(self):
        if(self.proximo() == 'void'):
            self.match('void')
            print('params correto 1')
            tudoCerto = True
            return tudoCerto
        elif(self.param_lista()):
            print('params correto 2')
            tudoCerto = True
            return tudoCerto
        else:
            print('erro sintatico oficial params')
            tudoCerto = False
            return tudoCerto

    def param_lista(self):
        self.param()
        while(self.proximo() == ','):
            self.param()

    def param(self):
        self.tipo_especificador()
        self.ident()

    def abre_colchete(self):
        return self.match('[')

    #def analisar(self):