class AnaliseSintatica:
    def __init__(self, tokens):
        print('sinatico')
        self.arrayTokens = tokens
        self.qntTokens = len(self.arrayTokens)
        self.posicao = 0
        self.programa()

    def setPosicao(self):
        self.posicao += 1

    def match(self, esperado):
        print('chamei match')
        print('esperado', esperado)
        if(self.posicao < self.qntTokens):
            if(esperado == self.arrayTokens[self.posicao].lexema):
                self.setPosicao()
                print('deu match')
                return True
        print('nao deu match')
        return False
    
    def proximo(self):
        print('tamanho', len(self.arrayTokens))
        print('posicao', self.posicao)
        if(self.posicao < self.qntTokens):
            return self.arrayTokens[self.posicao].lexema
    
    def programa(self):
        print('chamei programa')
        print('programa', self.declaracao_lista())

    def declaracao_lista(self):
        print('chamei declaracao_lista')
        if(not self.declaracao()):
            tudoCerto = False
            return tudoCerto
        else:
            tudoCerto = True
        
        print('terminei primeira declaracao')
        print(self.proximo())
        
        while(self.declaracao() and (self.posicao < self.qntTokens)):
            tudoCerto = True

        print('declaracoes realizadas')
        return tudoCerto

    def declaracao(self):
        print('chamei declaracao')
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
        print('chamei var_declaracao')
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
        if(self.proximo() == ';'):
            print('entrei')
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
        print('chamei tipo especificador')
        tudoCerto = True
        print('proximo', self.proximo())
        if(self.proximo() == 'int'):
            self.match('int')
            print('tipo_especificador correto 1')
        elif(self.proximo() == 'float'):
            self.match('float')
            print('tipo_especificador correto 2')
        elif(self.proximo() == 'void'):
            self.match('void')
            print('tipo_especificador correto 3')
        elif(self.proximo() == 'struct'):
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
        print('chamei fun_declaracao')
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
        #else:
            #print('implementar aqui')

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

    def local_declaracoes(self):
        tudoCerto = True
        while(tudoCerto):
            if(not self.var_declaracao()):
                tudoCerto = False
                return tudoCerto
        return tudoCerto

    def comando_lista(self): 
        tudoCerto = True
        while(tudoCerto):
            if(not self.comando()):
                tudoCerto = False
                return tudoCerto
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
            print('erro sintatico selecao_decl 2')
            tudoCerto = False        
            return tudoCerto
        if(not self.match(')')):        
            print('erro sintatico selecao_decl 2')
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

        return tudoCerto
        #else:
            #print('implementar aqui')

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
        else:
            print('erro sintatico oficial var')
            tudoCerto = False

        if(self.abre_colchete()):
            if(not self.expressao()):
                tudoCerto = False
                print('erro sintatico var 1')
                return tudoCerto
            if(not self.fecha_colchete()):
                print('erro sintatico var 2')
                tudoCerto = False
                return tudoCerto
        
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

    def relacional(self):
        tudoCerto = True
        if(self.proximo() == '<='):
            print('tudo certo relacional 1')
            self.match('<=')
        elif(self.proximo() == '<'):
            print('tudo certo relacional 2')
            self.match('<')
        elif(self.proximo() == '>'):
            print('tudo certo relacional 3')
            self.match('>')
        elif(self.proximo() == '>='):
            print('tudo certo relacional 4')
            self.match('>=')
        elif(self.proximo() == '=='):
            print('tudo certo relacional 5')
            self.match('==')
        elif(self.proximo() == '!='):
            print('tudo certo relacional 6')
            self.match('!=')
        else:
            print('erro sintatico oficial relacional')
            tudoCerto = False

        return tudoCerto

    def expressao_soma(self):
        tudoCerto = True
        if(not self.termo()):
            print('erro sintatico expressao_soma 1')
            tudoCerto = False
            return tudoCerto

        while(self.soma()):
            if(not self.termo()):
                print('erro sintatico expressao_soma 2')
                tudoCerto = False
                return tudoCerto
        
        print('tudo certo expressao_soma 1')
        return tudoCerto

    def soma(self):
        tudoCerto = True
        if(self.proximo() == '+'):
            self.match('+')
            print('tudo certo soma 1')
        elif(self.proximo() == '-'):
            self.match('-')
            print('tudo certo soma 2')
        else:
            tudoCerto = False
            print('erro sintatico oficial soma')
            return tudoCerto


    def termo(self):
        tudoCerto = True
        if(not self.fator()):
            tudoCerto = False
            print('erro sintatico termo 1')
            return tudoCerto

        while(self.mult()):
            if(not self.fator()):
                print('erro sintatico termo 2')
                tudoCerto = False
                return tudoCerto

        return tudoCerto

    def mult(self):
        tudoCerto = True
        if(self.proximo() == '*'):
            print('tudo certo mult 1')
            self.match('*')
        elif(self.proximo() == '/'):
            print('tudo certo mult 2')
            self.match('/')
        else:
            print('erro sintatico oficial mult 1')
            tudoCerto = False

        return tudoCerto

    def fator(self):
        tudoCerto = True
        if(self.proximo() == '('):
            self.match('(')
            print('tudo certo fator 1')
            if(not self.expressao()):
                print('erro sintatico fator 1')
                tudoCerto = False
                return tudoCerto
            if(self.proximo() == ')'):
                self.match(')')
                print('tudo certo fator 2')
            else:
                print('erro sintatico fator 2')
                tudoCerto = False
                return tudoCerto
        elif(self.var()):
            print('tudo certo fator 3')
            return tudoCerto
        elif(self.ativacao()):
            print('tudo certo fator 4')
            return tudoCerto
        elif(self.num()):
            print('tudo certo fator 5')
            return tudoCerto
        elif(self.num_int()):
            print('tudo certo fator 6')
            return tudoCerto
        else:
            print('erro sintatico oficial fator')
            tudoCerto = False
            return tudoCerto

    def ativacao(self):
        tudoCerto = True
        if(not self.ident()):
            print('erro sintatico ativacao 1')
            tudoCerto = False
            return tudoCerto

        if(self.proximo() == '('):
            self.match('(')
            print('tudo certo ativacao 1')
            if(not self.args()):
                print('erro sintatico ativacao 2')
                tudoCerto = False
                return tudoCerto
            if(self.proximo() == ')'):
                print('tudo certo ativaca 2')
                self.match(')')
            else:
                print('erro sintatico ativacao 3')
                tudoCerto = False
        else:
            print('erro sintatico oficial ativacao')
            tudoCerto = False

        return tudoCerto

    def args(self):
        #opcional
        self.arg_lista()
        return True

    def arg_lista(self):
        if(self.expressao()):
            tudoCerto = True
            print('arg_lista correto 1')
        else:
            print('erro sintatico oficial arg_lista')
            tudoCerto = False
            return tudoCerto
        while(self.proximo() == ','):
            self.match(',')
            print('arg_lista correto 2')
            if(not self.expressao()):
                print('erro sintatico arg_lista 1')
                tudoCerto = False
                return tudoCerto
        return tudoCerto

    def num(self):
        tudoCerto = True
        if(self.proximo() == '+'):
            self.match('+')
            print('tudo certo num 1')
            while(self.digito()):
                print('tudo certo num 2')
                if(self.proximo() == '.'):
                    self.match('.')
                    print('tudo certo num 3')
                    if(not self.digito()):
                        print('erro sintatico num 1')
                        tudoCerto = False
                        return tudoCerto
                    else:
                        print('tudo certo num 4')
                        while(self.digito()):
                            print('tudo certo num 5')
                            tudoCerto = True
        elif(self.proximo() == '-'):
            print('tudo certo num 6')
            self.match('-')
            while(self.digito()):
                print('tudo certo num 7')
                if(self.proximo() == '.'):
                    print('tudo certo num 8')
                    self.match('.')
                    if(not self.digito()):
                        print('erro sintatico num 2')
                        tudoCerto = False
                        return tudoCerto
                    else:
                        print('tudo certo num 9')
                        while(self.digito()):
                            tudoCerto = True
        elif(self.digito()):
            print('tudo certo num 10')
            while(self.digito()):
                print('tudo certo num 11')
                if(self.proximo() == '.'):
                    print('tudo certo num 12')
                    self.match('.')
                    if(not self.digito()):
                        print('erro sintatico num 3')
                        tudoCerto = False
                        return tudoCerto
                    else:
                        print('tudo certo num 13')
                        while(self.digito()):
                            tudoCerto = True
        else:
            print('erro sintatico oficial num')
            tudoCerto = False
        return tudoCerto


    def num_int(self):
        tudoCerto = True
        if(self.digito()):
            while(self.digito()):
                tudoCerto = True
        else:
            tudoCerto = False
            return False

        return tudoCerto

    
    def digito(self, digito):
        print('chamei digito')
        tudoCerto = True
        digitos = ['0','1','2','3','4','5','6','7','8','9']
        if digito not in digitos:
            print('erro sintatico oficial digito')
            tudoCerto = False
            return tudoCerto
            
        print('tudo certo digito')
        return tudoCerto

    def ident(self):
        print('chamei ident')
        tudoCerto = True

        print('proximo', self.proximo())
        print('tipo', type(self.proximo()))
        caracteres = list(self.proximo())
        contador = 0
        print('caracteres', caracteres)
        if(self.letra(caracteres[contador])):
            print('tudo certo ident 1')
            contador += 1
            while(((self.letra(caracteres[contador])) or (self.digito(caracteres[contador]))) and (contador < len(caracteres) - 1)):
                contador += 1
                print('tudo certo ident 2')
                tudoCerto = True
        else:
            print('erro sintatico oficial ident')
            tudoCerto = False

        print('tudo certo ident')
        self.setPosicao() #match do identificador
        return tudoCerto

    
    def letra(self, caractere):
        tudoCerto = True
        letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        print('caractere', caractere)
        if caractere not in letras:
            tudoCerto = False
            print('erro sintatico oficial letra')
            return tudoCerto
        print('tudo certo letra')
        return tudoCerto
        
    def abre_chave(self):
        return self.match('{')

    def fecha_chave(self):
        return self.match('}')

    def abre_colchete(self):
        return self.match('[')

    def fecha_colchete(self):
        return self.match(']')