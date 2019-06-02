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
        if(self.param()):
            tudoCerto = True
            print('param_lista correto 1')
        else:
            tudoCerto = False
            return tudoCerto
        while(self.proximo() == ','):
            self.match(',')
            print('param_lista correto 2')
            if(not self.param()):
                tudoCerto = False
                return tudoCerto
        return tudoCerto

    def param(self):
        tudoCerto = True
        if(not self.tipo_especificador()):
            tudoCerto = False
            print('erro sintatico param 1')
            return tudoCerto
        if(not self.ident()):
            tudoCerto = False
            print('erro sintatico param 2')
            return tudoCerto
        if(self.abre_colchete()):
            print('tudo certo param 1')
            if(not self.fecha_colchete()):
                tudoCerto = False
                print('erro sintatico param 3')
                return tudoCerto
        else:
            print('implementar aqui')

        return tudoCerto

    def composto_decl(self):
        tudoCerto = True
        if(not self.abre_chave()):
            tudoCerto = False
            print('erro sintatico composto_decl 1')
            return tudoCerto
        if(not self.local_declaracoes()):
            tudoCerto = False
            print('erro sintatico composto_decl 2')
            return tudoCerto
        if(not self.comando_lista()):
            tudoCerto = False
            print('erro sintatico composto_decl 3')
            return tudoCerto
        if(not self.fecha_chave()):
            tudoCerto = False
            print('erro sintatico composto_decl 4')
            return tudoCerto

        return tudoCerto

    def local_declaracoes(self): #verificar com calma aqui depois
        tudoCerto = False
        while(self.var_declaracao()):
            print('tudo certo local_declaracoes 1')
            tudoCerto = True
        return tudoCerto

    def comando_lista(self): #verificar com calma aqui depois
        tudoCerto = False
        while(self.comando()):
            print('tudo certo local_declaracoes 1')
            tudoCerto = True
        return tudoCerto

    def comando(self):
        if(self.expressao_decl()):
            print('tudo certo comando 1')
            tudoCerto = True
        elif(self.composto_decl()):
            print('tudo certo comando 2')
            tudoCerto = True
        elif(self.selecao_decl()):
            print('tudo certo comando 3')
            tudoCerto = True
        elif(self.iteracao_decl()):
            print('tudo certo comando 4')
            tudoCerto = True
        elif(self.retorno_decl()):
            print('tudo certo comando 5')
            tudoCerto = True
        else:
            print('erro sintatico oficial comando')
            tudoCerto = False
        
        return tudoCerto

    def expressao_decl(self):
        if(self.proximo() == ';'):
            self.match(';')
            tudoCerto = True
            print('tudo certo expressao_decl 1')
        elif(self.expressao()):
            tudoCerto = self.match(';')
            print('tudo certo expressao_decl 2')
        else:
            tudoCerto = False
            print('erro sintatico oficial expressao_decl')

        return tudoCerto

    def selecao_decl(self):
        tudoCerto = True
        if(not self.match('if')):
            tudoCerto = False
            print('erro sintatico selecao_decl 1')
            return tudoCerto
        if(not self.match('(')):
            print('erro sintatico selecao_decl 2')
            tudoCerto = False
            return tudoCerto
        if(not self.expressao()):
            print('erro sintatico selecao_decl 3')
            tudoCerto = False
            return tudoCerto
        if(not self.match(')')):
            print('erro sintatico selecao_decl 4')
            tudoCerto = False
            return tudoCerto
        if(not self.comando()):
            print('erro sintatico selecao_decl 5')
            tudoCerto = False
            return tudoCerto
        if(self.proximo() == 'else'):
            self.match('else')
            print('tudo certo selecao_decl 1')
            if(not self.comando()):
                tudoCerto = False
                print('erro sintatico selecao_decl 6')
                return tudoCerto
        else:
            print('implementar aqui')

    def iteracao_decl(self):
        tudoCerto = True
        if(not self.match('while')):
            tudoCerto = False
            print('erro sintatico iteracao_decl 1')
            return tudoCerto
        if(not self.match('(')):
            tudoCerto = False
            print('erro sintatico iteracao_decl 2')
            return tudoCerto
        if(not self.expressao()):
            tudoCerto = False
            print('erro sintatico iteracao_decl 3')
            return tudoCerto
        if(not self.match(')')):
            tudoCerto = False
            print('erro sintatico iteracao_decl 4')
            return tudoCerto
        if(not self.comando()):
            tudoCerto = False
            print('erro sintatico iteracao_decl 5')
            return tudoCerto
        return tudoCerto

    def retorno_decl(self):
        tudoCerto = True
        if(not self.match('return')):
            print('erro sintatico retorno_decl 1')
            tudoCerto = False
            return tudoCerto
        if(self.proximo() == ';'):
            self.match(';')
            print('tudo certo retorno_decl 1')
            tudoCerto = True
            return tudoCerto
        elif(self.expressao()):
            if(not self.match(';')):
                print('erro sintatico retorno_decl 2')
                tudoCerto = False
                return tudoCerto
        else:
            print('erro sintatico oficial retorno_decl')
            tudoCerto = False
            return tudoCerto

        return tudoCerto

    def expressao(self):
        tudoCerto = True
        if(self.var()):
            print('tudo certo expressao 1')
            if(not self.match('=')):
                tudoCerto = False
                print('erro sintatico expressao 1')
                return tudoCerto
            if(not self.expressao()):
                tudoCerto = False
                print('erro sintatico expressao 2')
                return tudoCerto
        elif(self.expressao_simples()):
            print('tudo certo expressao 2')
            tudoCerto = True
            return tudoCerto
        else:
            print('erro sintatico oficial expressao')
            tudoCerto = False
            return tudoCerto

    return tudoCerto

    def var(self):
        tudoCerto = True
        if(self.ident()):
            print('tudo certo var 1')
            if(not self.abre_colchete()):
                print('erro sintatico var 1')
                tudoCerto = False
                return tudoCerto
            if(not self.expressao()):
                tudoCerto = False
                print('erro sintatico var 2')
                return tudoCerto
            if(not self.fecha_colchete()):
                print('erro sintatico var 3')
                tudoCerto = False
                return tudoCerto
        else:
            print('erro sintatico oficial var')
            tudoCerto = False
        
        return tudoCerto

    def expressao_simples(self):
        tudoCerto = True
        if(self.expressao_soma()):
            print('tudo certo expressao_simples')
            if(not self.relacional()):
                print('erro sintatico expressao_simples 1')
                tudoCerto = False
                return tudoCerto
            if(not self.expressao_soma()):
                print('erro sintatico expressao_simples 2')
                tudoCerto = False
                return tudoCerto
        else:
            tudoCerto = False
            print('erro sintatico oficial expressao_simples')
            return tudoCerto
        return tudoCerto


    def abre_colchete(self):
        return self.match('[')

    #def analisar(self):