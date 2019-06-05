from Sintatico.classes.Erro import *
class AnaliseSintatica:
    def __init__(self, tokens):
        print('sinatico')
        self.arrayTokens = tokens
        self.qntTokens = len(self.arrayTokens)
        self.posicao = 0
        self.erros = []
        self.tokensPorLinha = self.calculaSomatorioTokensPorLinha()
        self.programa()
        self.imprimirErros()

    def calculaSomatorioTokensPorLinha(self):
        linhaAtual = 1
        i = 0
        qntTokensLinha = 0
        arrayTokensPorLinha = {}
        for token in self.arrayTokens:
            if(token.linha == linhaAtual):
                qntTokensLinha += 1
            else:
                arrayTokensPorLinha[linhaAtual] = qntTokensLinha
                linhaAtual += 1
                qntTokensLinha += 1
            
            #ultimo token analisado
            i += 1
            if(i == self.qntTokens):
                arrayTokensPorLinha[linhaAtual] = qntTokensLinha

        return arrayTokensPorLinha
            
    def setPosicao(self):
        self.posicao += 1

    def backPosicao(self, posicoes):
        self.posicao = self.posicao - posicoes

    def match(self, esperado):
        print('CHAMEI match')
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
            

    def retornaLinhaToken(self):
        return self.arrayTokens[self.posicao - 1].linha

    def imprimirErros(self):
        print('ERROS:')
        if(len(self.erros) > 0):
            for erro in self.erros:
                print('Linha:', erro.linha, 'Descrição:', erro.descricao)
        else:
            print('Não foi encontrado erros sintáticos')
    
    def programa(self):
        print('CHAMEI programa')
        print('programa', self.declaracao_lista())

    def declaracao_lista(self):
        print('CHAMEI declaracao_lista')
        if(not self.declaracao()):
            print('erro sintatico oficial declaracao_lista 1')
            erro = Erro(self.retornaLinhaToken(), 0)
            self.erros.append(erro)
            tudoCerto = False
            return tudoCerto
        else:
            tudoCerto = True
        
        print('terminei primeira declaracao')

        #qntTokensAteALinha = self.tokensPorLinha[self.retornaLinhaToken()]
        
        while((self.posicao < self.qntTokens)):

            if(self.declaracao()):
                tudoCerto = True
                print('declaracao_lista ok')
            else:
                tudoCerto = False
                print('erro sintatico oficial declaracao_lista 2')
                erro = Erro(self.retornaLinhaToken(), 0)
                self.erros.append(erro)
                return tudoCerto
            '''elif(self.posicao < qntTokensAteALinha):
                print('acabou a linha')
                tudoCerto = True
            '''
            

        print('declaracoes realizadas')
        return tudoCerto

    def declaracao(self):
        print('CHAMEI declaracao')
        if(self.var_declaracao()):
            print('var_declaracao tudo certo')
            tudoCerto = True
        elif(self.fun_declaracao()):
            print('fun_declaracao tudo certo')
            tudoCerto = True
        else:
            tudoCerto = False
            erro = Erro(self.retornaLinhaToken(), 1)
            self.erros.append(erro)
            print('erro sintatico oficial declaracao')
            return tudoCerto

        print('declaracao tudo certo')
        return tudoCerto

    def var_declaracao(self):
        print('CHAMEI var_declaracao')
        voltarPosicao = 0
        tudoCerto = True
        if(not self.tipo_especificador()):
            print('erro sintatico var_declaracao 1')
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        print('var_declaracao correto 1')
        if(not self.ident()):
            print('erro sintatico var_declaracao 2')
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
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

            qntTokensAteALinha = self.tokensPorLinha[self.retornaLinhaToken()]
            
            while(self.posicao < qntTokensAteALinha):
                if(self.proximo() != ';'):
                    if(not self.abre_colchete()):
                        print('erro sintatico var_declaracao 6')
                        tudoCerto = False
                        return tudoCerto
                    if(not self.num_int()):
                        print('erro sintatico var_declaracao 7')
                        tudoCerto = False
                        return tudoCerto
                    if(not self.fecha_colchete()):
                        print('erro sintatico var_declaracao 8')
                        tudoCerto = False
                        return tudoCerto
                else:

                    break

            if(not self.match(';')):
                print('erro sintatico var_declaracao 5')
                tudoCerto = False
                return tudoCerto
        else:
            self.backPosicao(voltarPosicao)
            print('erro sintatico oficial var_declaracao')
            tudoCerto = False
            return tudoCerto
        
        print('var_declaracao tudo certo ')
        return tudoCerto

    def tipo_especificador(self):
        print('CHAMEI tipo especificador')
        tudoCerto = True
        voltarPosicao = 0
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
            voltarPosicao += 1
            self.match('struct')
            print('tipo_especificador struct')
            if(not self.ident()):
                print('erro sintatico tipo_especificador 1')
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.abre_chave()):
                print('erro sintatico tipo_especificador 2')
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.atributos_declaracao()):
                print('erro sintatico tipo_especificador 3')
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.fecha_chave()):
                print('erro sintatico tipo_especificador 4')
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
        else:
            print('erro sintatico oficial tipo_especificador')
            tudoCerto = False
            return tudoCerto
        
        return tudoCerto

    def atributos_declaracao(self):
        print('CHAMEI atributos_declaracao')
        return self.var_declaracao()

    def fun_declaracao(self):
        print('CHAMEI fun_declaracao')
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
        print('aqui')
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
        print('CHAMEI params')
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
        print('CHAMEI param_lista')
        if(self.param()):
            tudoCerto = True
            print('param_lista correto 1')
        else:
            tudoCerto = False
            return tudoCerto
        print('testei aqui param_lista')
        while(self.proximo() == ','):
            self.match(',')
            print('param_lista correto 2')
            if(not self.param()):
                tudoCerto = False
                return tudoCerto
        return tudoCerto

    def param(self):
        print('CHAMEI param')
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

        return tudoCerto

    def composto_decl(self):
        print('CHAMEI composto_decl')
        tudoCerto = True
        if(not self.abre_chave()):
            tudoCerto = False
            print('erro sintatico composto_decl 1')
            return tudoCerto
        if(not self.local_declaracoes()):
            tudoCerto = False
            print('erro sintatico composto_decl 2')
            return tudoCerto
        '''
        print('CHAMEI COMANDO LISTA POR AQUIIIIIIIIIIIIIIII 2')
        if(not self.comando_lista()):
            tudoCerto = False
            print('erro sintatico composto_decl 3')
            return tudoCerto
        '''

        if(not self.fecha_chave()):
            tudoCerto = False
            print('erro sintatico composto_decl 4')
            return tudoCerto

        return tudoCerto

    def local_declaracoes(self):
        print('CHAMEI local_declaracoes')
        tudoCerto = True
        #qntTokensAteALinha = self.tokensPorLinha[self.retornaLinhaToken()]
        while((tudoCerto) and (self.posicao < self.qntTokens)):
            if(not self.var_declaracao()):
                tudoCerto = False
                print('CHAMEI COMANDO LISTA POR AQUIIIIIIIIIIIIIIII 1')
                if(not self.comando_lista()):
                    print('por aqui não deu o comando_lista')
                    print('erro sintatico oficial local_declaracoes')
                    tudoCerto = False
        return True

    def comando_lista(self): 
        print('CHAMEI comando_lista')
        tudoCerto = True
        #qntTokensAteALinha = self.tokensPorLinha[self.retornaLinhaToken()]
        #print('QNT TOKENS ATEH A LINHA', qntTokensAteALinha)
        print('POSICAO', self.posicao)
        print('aqui')
        while((tudoCerto) and (self.posicao < self.qntTokens)):
            #print('QNT TOKENS ATEH A LINHA', qntTokensAteALinha)
            print('POSICAO', self.posicao)
            if(self.proximo() == '}'):
                return True
            elif(self.proximo() == ';'): #adicionei pois estava dando interferencia com expressao-decl chamado via comando-lista após local-declaracoes
                return False
            elif(not self.comando()):
                print('erro sintatico oficial comando_lista')
                tudoCerto = False
                return tudoCerto

        
        return tudoCerto

    def comando(self):
        print('CHAMEI comando')
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
        print('CHAMEI EXPRESSÃOOOOOOOOOOOOOOOO_DECL')
        voltarPosicao = 0
        if(self.posicao < self.qntTokens):
            if(self.proximo() == ';'):
                tudoCerto = self.match(';')
                print('tudo certo expressao_decl 1')
            elif(self.expressao()):
                print('CHAMEI aqui dps de expressao dar  certo')
                voltarPosicao += 1
                print('testei ;')
                if(self.proximo() == ';'):
                    tudoCerto = self.match(';')
                else:
                    tudoCerto = False
                    self.backPosicao(voltarPosicao)
            else:
                tudoCerto = False
                print('erro sintatico oficial expressao_decl')
        else:
            tudoCerto = False

        return tudoCerto

    def selecao_decl(self):
        print('CHAMEI selecao_decl')
        tudoCerto = True
        voltarPosicao = 0
        if(not self.match('if')):
            tudoCerto = False
            print('erro sintatico selecao_decl 1')
            return tudoCerto
        voltarPosicao += 1
        if(not self.match('(')):
            self.backPosicao(voltarPosicao)
            print('erro sintatico selecao_decl 2')
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.expressao()):
            self.backPosicao(voltarPosicao)
            print('erro sintatico selecao_decl 2')
            tudoCerto = False        
            return tudoCerto
        voltarPosicao += 1
        if(not self.match(')')):
            self.backPosicao(voltarPosicao)        
            print('erro sintatico selecao_decl 2')
            tudoCerto = False        
            return tudoCerto
        voltarPosicao += 1
        if(not self.comando()):
            self.backPosicao(voltarPosicao)
            print('erro sintatico selecao_decl 5')
            tudoCerto = False
            return tudoCerto
        
        if(self.proximo() == 'else'):
            voltarPosicao += 1
            self.match('else')
            print('tudo certo selecao_decl 1')
            if(not self.comando()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                print('erro sintatico selecao_decl 6')
                return tudoCerto

        return tudoCerto
        #else:
            #print('implementar aqui')

    def iteracao_decl(self):
        print('CHAMEI iteracao_decl')
        tudoCerto = True
        voltarPosicao = 0
        if(not self.match('while')):
            tudoCerto = False
            print('erro sintatico iteracao_decl 1')
            return tudoCerto
        voltarPosicao += 1
        if(not self.match('(')):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            print('erro sintatico iteracao_decl 2')
            return tudoCerto
        voltarPosicao += 1
        if(not self.expressao()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            print('erro sintatico iteracao_decl 3')
            return tudoCerto
        voltarPosicao += 1
        if(not self.match(')')):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            print('erro sintatico iteracao_decl 4')
            return tudoCerto
        voltarPosicao += 1
        if(not self.comando()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            print('erro sintatico iteracao_decl 5')
            return tudoCerto
        #voltarPosicao += 1
        return tudoCerto

    def retorno_decl(self):
        print('CHAMEI retorno_decl')
        tudoCerto = True
        voltarPosicao = 0
        if(not self.match('return')):
            print('erro sintatico retorno_decl 1')
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(self.proximo() == ';'):
            self.match(';')
            print('tudo certo retorno_decl 1')
            tudoCerto = True
            return tudoCerto
        elif(self.expressao()):
            voltarPosicao += 1
            if(not self.match(';')):
                self.backPosicao(voltarPosicao)
                print('erro sintatico retorno_decl 2')
                tudoCerto = False
                return tudoCerto
        else:
            self.backPosicao(voltarPosicao)
            print('erro sintatico oficial retorno_decl')
            tudoCerto = False
            return tudoCerto

        return tudoCerto

    def expressao(self):
        print('CHAMEI expressao')
        tudoCerto = True
        print('posicao', self.posicao)
        print('tamanho', self.qntTokens)
        voltarPosicao = 0
        if(self.posicao < self.qntTokens):
            if(self.var()):
                voltarPosicao += 1
                print('tudo certo expressao 1')
                if(not self.match('=')):
                    self.backPosicao(voltarPosicao)
                    tudoCerto = False
                    print('erro sintatico expressao 1')
                    return tudoCerto
                #voltarPosicao += 1
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
        print('CHAMEI var')
        tudoCerto = True
        voltarPosicao = 0
        if(self.ident()):
            print('tudo certo var 1')
        else:
            print('erro sintatico oficial var')
            tudoCerto = False
            return tudoCerto

        
        while(self.abre_colchete()):
            voltarPosicao += 1
            if(not self.expressao()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                print('erro sintatico var 1')
                return tudoCerto
            voltarPosicao += 1
            if(not self.fecha_colchete()):
                self.backPosicao(voltarPosicao)
                print('erro sintatico var 2')
                tudoCerto = False
                return tudoCerto
        
        return tudoCerto

    def expressao_simples(self):
        print('CHAMEI expressao_simples')
        tudoCerto = True
        if(self.expressao_soma()):
            print('tudo certo expressao_simples 1')
            if(not self.relacional()):
                print('erro sintatico expressao_simples 1')
                print('CHAMEI aqui 1')
                tudoCerto = True
                return tudoCerto
            print('tudo certo expressao_simples 2')
            if(not self.expressao_soma()):
                print('erro sintatico expressao_simples 2')
                tudoCerto = False
                return tudoCerto
            print('tudo certo expressao_simples 3')
        else:
            tudoCerto = False
            print('erro sintatico oficial expressao_simples')
            return tudoCerto
        return tudoCerto

    def relacional(self):
        print('CHAMEI relacional')
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
        print('CHAMEI expressao_soma')
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
        print('CHAMEI soma')
        tudoCerto = True
        print('PROXIMO', self.proximo())

        tem = False
        if(self.posicao < self.qntTokens):
            if(('-' in self.proximo()) or ('+' in self.proximo())):
                tem = True

            if(self.proximo() == '+'):
                self.match('+')
                print('tudo certo soma 1')
            elif(self.proximo() == '-'):
                self.match('-')
                print('tudo certo soma 2')
            elif(tem):
                tudoCerto = True
                print('tudo certo soma 3')
            else:
                tudoCerto = False
                print('erro sintatico oficial soma')
                return tudoCerto
        else:
            tudoCerto = False

        return tudoCerto


    def termo(self):
        print('CHAMEI termo')
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

        print('tudo certo termo')
        return tudoCerto

    def mult(self):
        print('CHAMEI mult')
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
        print('CHAMEI fator')
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
                tudoCerto = True
                return tudoCerto
                print('tudo certo fator 2')
            else:
                print('erro sintatico fator 2')
                tudoCerto = False
                return tudoCerto
        elif(self.var()):
            print('tudo certo fator 3')
            if(self.proximo() == '('):
                if(self.ativacao()):
                    tudoCerto = True
                    return tudoCerto
                else:
                    tudoCerto = False
                    return tudoCerto
                print('PROXIMO EH PARENTESES')
            else:
                print('PROXIMO NAO EH PARENTESES')
                return tudoCerto
        elif(self.num_int()):
            print('tudo certo fator 5')
            return tudoCerto
        else:
            print('erro sintatico oficial fator')
            tudoCerto = False
            return tudoCerto
        '''elif(self.num()):
            print('tudo certo fator 6')
            return tudoCerto
        '''
        

    def ativacao(self):
        print('CHAMEI ativacao')
        tudoCerto = True
        ''' esta chamando direto de var no fator
        if(not self.ident()):
            print('erro sintatico ativacao 1')
            tudoCerto = False
            return tudoCerto
        '''

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
                tudoCerto = True
                return tudoCerto
            else:
                print('erro sintatico ativacao 3')
                tudoCerto = False
        else:
            print('erro sintatico oficial ativacao')
            tudoCerto = False

        return tudoCerto

    def args(self):
        print('CHAMEI args')
        #opcional
        if(self.arg_lista()):
            print('args tudo certo')
            return True
        else:
            print('erro sintatico oficial args')
            return False

    def arg_lista(self):
        print('CHAMEI arg_lista')
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
        print('CHAMEI num')
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
        print('CHAMEI num_int')
        tudoCerto = True
        digitos = list(self.proximo())
        print('tamanho digitos', len(digitos))
        contador = 0
        if(self.digito(digitos[contador])):
            contador += 1
            print('contador', contador)
            while((contador < len(digitos) - 1) and (self.digito(digitos[contador]))):
                tudoCerto = True
                contador += 1
        else:
            print('erro oficial num_int')
            tudoCerto = False
            return tudoCerto

        self.setPosicao() #match do num_int
        print('tudo certo num_int')
        return tudoCerto

    
    def digito(self, digito):
        print('CHAMEI digito')
        tudoCerto = True
        digitos = ['0','1','2','3','4','5','6','7','8','9','+','-']
        if digito not in digitos:
            print('erro sintatico oficial digito')
            tudoCerto = False
            return tudoCerto
            
        print('tudo certo digito')
        return tudoCerto

    def ident(self):
        print('CHAMEI ident')
        tudoCerto = True

        print('proximo', self.proximo())
        print('tipo', type(self.proximo()))
        if(self.posicao < self.qntTokens):
            caracteres = list(self.proximo())
        else:
            return False
        contador = 0
        print('caracteres', caracteres)
        if(self.letra(caracteres[contador])):
            print('tudo certo ident 1')
            contador += 1
            while((contador < len(caracteres) - 1) and ((self.letra(caracteres[contador])) or (self.digito(caracteres[contador])))):
                contador += 1
                print('tudo certo ident 2')
                tudoCerto = True
        else:
            print('erro sintatico oficial ident')
            tudoCerto = False
            return tudoCerto

        print('tudo certo ident')
        self.setPosicao() #match do identificador
        return tudoCerto

    
    def letra(self, caractere):
        print('CHAMEI letra')
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
        print('CHAMEI abre_chave')
        return self.match('{')

    def fecha_chave(self):
        print('CHAMEI fecha_chave')
        return self.match('}')

    def abre_colchete(self):
        print('CHAMEI abre_colchete')
        return self.match('[')

    def fecha_colchete(self):
        print('CHAMEI fecha_colchete')
        return self.match(']')