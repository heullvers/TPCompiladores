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
        print('chamei programa')
        self.declaracao_lista()
        print('voltei programa')

    def declaracao_lista(self):
        print('chamei declaracao_lista')
        self.declaracao()
        print('voltei declaracao_lista')

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
        self.arg_lista():
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

    
    def digito(self):
        tudoCerto = True
        if(self.proximo() == '0'):
            self.match('0')
        elif(self.proximo() == '1'):
            self.match('1')
        elif(self.proximo() == '2'):
            self.match('2')
        elif(self.proximo() == '3'):
            self.match('3')
        elif(self.proximo() == '4'):
            self.match('4')
        elif(self.proximo() == '5'):
            self.match('5')
        elif(self.proximo() == '6'):
            self.match('6')
        elif(self.proximo() == '7'):
            self.match('7')
        elif(self.proximo() == '8'):
            self.match('8')
        elif(self.proximo() == '9'):
            self.match('9')
        else:
            tudoCerto = False
        
        return tudoCerto

    def ident(self):
        tudoCerto = True
        if(self.letra()):
            print('tudo certo ident 1')
            while((self.letra()) or (self.digito())):
                print('tudo certo ident 2')
                tudoCerto = True
        else:
            print('erro sintatico oficial ident')
            tudoCerto = False

    
    def digito(self):
        tudoCerto = True
        if(self.proximo() == 'a'):
            self.match('a')
            print('tudo certo digito 1')
        elif(self.proximo() == 'b'):
            self.match('b')
            print('tudo certo digito 2')
        elif(self.proximo() == 'c'):
            self.match('c')
            print('tudo certo digito 3')
        elif(self.proximo() == 'd'):
            self.match('d')
            print('tudo certo digito 4')
        elif(self.proximo() == 'e'):
            self.match('e')
            print('tudo certo digito 5')
        elif(self.proximo() == 'f'):
            self.match('f')
            print('tudo certo digito 6')
        elif(self.proximo() == 'g'):
            self.match('g')
            print('tudo certo digito 7')
        elif(self.proximo() == 'h'):
            self.match('h')
            print('tudo certo digito 8')
        elif(self.proximo() == 'i'):
            self.match('i')
            print('tudo certo digito 9')
        elif(self.proximo() == 'j'):
            self.match('j')
            print('tudo certo digito 10')
        elif(self.proximo() == 'k'):
            self.match('k')
            print('tudo certo digito 11')
        elif(self.proximo() == 'l'):
            self.match('l')
            print('tudo certo digito 12')
        elif(self.proximo() == 'm'):
            self.match('m')
            print('tudo certo digito 13')
        elif(self.proximo() == 'n'):
            self.match('n')
            print('tudo certo digito 14')
        elif(self.proximo() == 'o'):
            self.match('o')
            print('tudo certo digito 15')
        elif(self.proximo() == 'p'):
            self.match('p')
            print('tudo certo digito 16')
        elif(self.proximo() == 'q'):
            self.match('q')
            print('tudo certo digito 17')
        elif(self.proximo() == 'r'):
            self.match('r')
            print('tudo certo digito 18')
        elif(self.proximo() == 's'):
            self.match('s')
            print('tudo certo digito 19')
        elif(self.proximo() == 't'):
            self.match('t')
            print('tudo certo digito 20')
        elif(self.proximo() == 'u'):
            self.match('u')
            print('tudo certo digito 21')
        elif(self.proximo() == 'v'):
            self.match('v')
            print('tudo certo digito 22')
        elif(self.proximo() == 'w'):
            self.match('w')
            print('tudo certo digito 23')
        elif(self.proximo() == 'x'):
            self.match('x')
            print('tudo certo digito 24')
        elif(self.proximo() == 'y'):
            self.match('y')
            print('tudo certo digito 25')
        elif(self.proximo() == 'z'):
            self.match('z')
            print('tudo certo digito 26')
        else:
            tudoCerto = False
            print('erro sintatico oficial digito')

        return tudoCerto
        
    def abre_chave(self):
        return self.match('{')

    def fecha_chave(self):
        return self.match('}')

    def abre_colchete(self):
        return self.match('[')

    def fecha_colchete(self):
        return self.match(']')