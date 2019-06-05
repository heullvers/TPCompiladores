from Sintatico.classes.Erro import *
class AnaliseSintatica:
    def __init__(self, tokens):
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
        if(self.posicao < self.qntTokens):
            if(esperado == self.arrayTokens[self.posicao].lexema):
                self.setPosicao()
                return True
        return False
    
    def proximo(self):
        if(self.posicao < self.qntTokens):
            return self.arrayTokens[self.posicao].lexema
            

    def retornaToken(self):
        return self.arrayTokens[self.posicao - 1]

    def retornaLinhaToken(self):
        return self.arrayTokens[self.posicao - 1].linha

    def imprimirErros(self):
        print('ERROS:')
        if(len(self.erros) > 0):
            for erro in self.erros:
                print('Linha:', erro.linha, 'Coluna:', erro.coluna)
        else:
            print('Não foi encontrado erros sintáticos')
    
    def programa(self):
        self.declaracao_lista()

    def declaracao_lista(self):
        if(not self.declaracao()):
            token = self.retornaToken()
            erro = Erro(token.linha, token.coluna)
            self.erros.append(erro)
            tudoCerto = False
            return tudoCerto
        else:
            tudoCerto = True
        
        while((self.posicao < self.qntTokens)):
            if(self.declaracao()):
                tudoCerto = True
            else:
                tudoCerto = False
                token = self.retornaToken()
                erro = Erro(token.linha, token.coluna)
                self.erros.append(erro)
                return tudoCerto
    
        return tudoCerto

    def declaracao(self):
        if(self.var_declaracao()):
            tudoCerto = True
        elif(self.fun_declaracao()):
            tudoCerto = True
        else:
            tudoCerto = False
            return tudoCerto

        return tudoCerto

    def var_declaracao(self):
        voltarPosicao = 0
        tudoCerto = True
        if(not self.tipo_especificador()):
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.ident()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1

        if(self.proximo() == ';'):
            self.match(';')
        elif(self.abre_colchete()):
            if(not self.num_int()):
                tudoCerto = False
                return tudoCerto
            if(not self.fecha_colchete()):
                tudoCerto = False
                return tudoCerto

            qntTokensAteALinha = self.tokensPorLinha[self.retornaLinhaToken()]
            
            while(self.posicao < qntTokensAteALinha):
                if(self.proximo() != ';'):
                    if(not self.abre_colchete()):
                        tudoCerto = False
                        return tudoCerto
                    if(not self.num_int()):
                        tudoCerto = False
                        return tudoCerto
                    if(not self.fecha_colchete()):
                        tudoCerto = False
                        return tudoCerto
                else:

                    break

            if(not self.match(';')):
                tudoCerto = False
                return tudoCerto
        else:
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        
        return tudoCerto

    def tipo_especificador(self):
        tudoCerto = True
        voltarPosicao = 0
        if(self.proximo() == 'int'):
            self.match('int')
        elif(self.proximo() == 'float'):
            self.match('float')
        elif(self.proximo() == 'void'):
            self.match('void')
        elif(self.proximo() == 'struct'):
            voltarPosicao += 1
            self.match('struct')
            if(not self.ident()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.abre_chave()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.atributos_declaracao()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.fecha_chave()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
        else:
            tudoCerto = False
            return tudoCerto
        
        return tudoCerto

    def atributos_declaracao(self):
        return self.var_declaracao()

    def fun_declaracao(self):
        tudoCerto = True
        if(not self.tipo_especificador()):
            tudoCerto = False
            return tudoCerto
        if(not self.ident()):
            tudoCerto = False
            return tudoCerto
        if(not self.match('(')):
            tudoCerto = False
            return tudoCerto
        if(not self.params()):
            tudoCerto = False
            return tudoCerto
        if(not self.match(')')):
            tudoCerto = False
            return tudoCerto
        if(not self.composto_decl()):
            tudoCerto = False
            return tudoCerto
        
        return tudoCerto

    def params(self):
        if(self.proximo() == 'void'):
            self.match('void')
            tudoCerto = True
            return tudoCerto
        elif(self.param_lista()):
            tudoCerto = True
            return tudoCerto
        else:
            tudoCerto = False
            return tudoCerto

    def param_lista(self):
        if(self.param()):
            tudoCerto = True
        else:
            tudoCerto = False
            return tudoCerto
        while(self.proximo() == ','):
            self.match(',')
            if(not self.param()):
                tudoCerto = False
                return tudoCerto
        return tudoCerto

    def param(self):
        tudoCerto = True
        if(not self.tipo_especificador()):
            tudoCerto = False
            return tudoCerto
        if(not self.ident()):
            tudoCerto = False
            return tudoCerto

        if(self.abre_colchete()):
            if(not self.fecha_colchete()):
                tudoCerto = False
                return tudoCerto

        return tudoCerto

    def composto_decl(self):
        tudoCerto = True
        if(not self.abre_chave()):
            tudoCerto = False
            return tudoCerto
        if(not self.local_declaracoes()):
            tudoCerto = False
            return tudoCerto

        if(not self.fecha_chave()):
            tudoCerto = False
            return tudoCerto

        return tudoCerto

    def local_declaracoes(self):
        tudoCerto = True
        while((tudoCerto) and (self.posicao < self.qntTokens)):
            if(not self.var_declaracao()):
                tudoCerto = False
                if(not self.comando_lista()):
                    tudoCerto = False
        return True

    def comando_lista(self): 
        tudoCerto = True
        while((tudoCerto) and (self.posicao < self.qntTokens)):
            if(self.proximo() == '}'):
                return True
            elif(self.proximo() == ';'): #adicionei pois estava dando interferencia com expressao-decl chamado via comando-lista após local-declaracoes
                return False
            elif(not self.comando()):
                tudoCerto = False
                return tudoCerto

        return tudoCerto

    def comando(self):
        if(self.expressao_decl()):
            tudoCerto = True
        elif(self.composto_decl()):
            tudoCerto = True
        elif(self.selecao_decl()):
            tudoCerto = True
        elif(self.iteracao_decl()):
            tudoCerto = True
        elif(self.retorno_decl()):
            tudoCerto = True
        else:
            tudoCerto = False
        
        return tudoCerto

    def expressao_decl(self):
        voltarPosicao = 0
        if(self.posicao < self.qntTokens):
            if(self.proximo() == ';'):
                tudoCerto = self.match(';')
            elif(self.expressao()):
                voltarPosicao += 1
                if(self.proximo() == ';'):
                    tudoCerto = self.match(';')
                else:
                    tudoCerto = False
                    self.backPosicao(voltarPosicao)
            else:
                tudoCerto = False
        else:
            tudoCerto = False

        return tudoCerto

    def selecao_decl(self):
        tudoCerto = True
        voltarPosicao = 0
        if(not self.match('if')):
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.match('(')):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.expressao()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False        
            return tudoCerto
        voltarPosicao += 1
        if(not self.match(')')):
            self.backPosicao(voltarPosicao)        
            tudoCerto = False        
            return tudoCerto
        voltarPosicao += 1
        if(not self.comando()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        
        if(self.proximo() == 'else'):
            voltarPosicao += 1
            self.match('else')
            if(not self.comando()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto

        return tudoCerto

    def iteracao_decl(self):
        tudoCerto = True
        voltarPosicao = 0
        if(not self.match('while')):
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.match('(')):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.expressao()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.match(')')):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(not self.comando()):
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto
        return tudoCerto

    def retorno_decl(self):
        tudoCerto = True
        voltarPosicao = 0
        if(not self.match('return')):
            tudoCerto = False
            return tudoCerto
        voltarPosicao += 1
        if(self.proximo() == ';'):
            self.match(';')
            tudoCerto = True
            return tudoCerto
        elif(self.expressao()):
            voltarPosicao += 1
            if(not self.match(';')):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
        else:
            self.backPosicao(voltarPosicao)
            tudoCerto = False
            return tudoCerto

        return tudoCerto

    def expressao(self):
        tudoCerto = True
        voltarPosicao = 0
        if(self.posicao < self.qntTokens):
            if(self.var()):
                voltarPosicao += 1
                if(not self.match('=')):
                    self.backPosicao(voltarPosicao)
                    tudoCerto = False
                    return tudoCerto
                #voltarPosicao += 1
                if(not self.expressao()):
                    tudoCerto = False
                    return tudoCerto
            elif(self.expressao_simples()):
                tudoCerto = True
                return tudoCerto
            else:
                tudoCerto = False
                return tudoCerto

        return tudoCerto

    def var(self):
        tudoCerto = True
        voltarPosicao = 0
        if(self.ident()):
            tudoCerto = True
        else:
            tudoCerto = False
            return tudoCerto

        while(self.abre_colchete()):
            voltarPosicao += 1
            if(not self.expressao()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
            voltarPosicao += 1
            if(not self.fecha_colchete()):
                self.backPosicao(voltarPosicao)
                tudoCerto = False
                return tudoCerto
        
        return tudoCerto

    def expressao_simples(self):
        tudoCerto = True
        if(self.expressao_soma()):
            if(not self.relacional()):
                tudoCerto = True
                return tudoCerto
            if(not self.expressao_soma()):
                tudoCerto = False
                return tudoCerto
        else:
            tudoCerto = False
            return tudoCerto
        return tudoCerto

    def relacional(self):
        tudoCerto = True
        if(self.proximo() == '<='):
            self.match('<=')
        elif(self.proximo() == '<'):
            self.match('<')
        elif(self.proximo() == '>'):
            self.match('>')
        elif(self.proximo() == '>='):
            self.match('>=')
        elif(self.proximo() == '=='):
            self.match('==')
        elif(self.proximo() == '!='):
            self.match('!=')
        else:
            tudoCerto = False

        return tudoCerto

    def expressao_soma(self):
        tudoCerto = True
        if(not self.termo()):
            tudoCerto = False
            return tudoCerto

        while(self.soma()):
            if(not self.termo()):
                tudoCerto = False
                return tudoCerto
        
        return tudoCerto

    def soma(self):
        tudoCerto = True
        tem = False
        if(self.posicao < self.qntTokens):
            if(('-' in self.proximo()) or ('+' in self.proximo())):
                tem = True

            if(self.proximo() == '+'):
                self.match('+')
            elif(self.proximo() == '-'):
                self.match('-')
            elif(tem):
                tudoCerto = True
            else:
                tudoCerto = False
                return tudoCerto
        else:
            tudoCerto = False

        return tudoCerto


    def termo(self):
        tudoCerto = True
        if(not self.fator()):
            tudoCerto = False
            return tudoCerto

        while(self.mult()):
            if(not self.fator()):
                tudoCerto = False
                return tudoCerto

        return tudoCerto

    def mult(self):
        tudoCerto = True
        if(self.proximo() == '*'):
            self.match('*')
        elif(self.proximo() == '/'):
            self.match('/')
        else:
            tudoCerto = False

        return tudoCerto

    def fator(self):
        tudoCerto = True
        if(self.proximo() == '('):
            self.match('(')
            if(not self.expressao()):
                tudoCerto = False
                return tudoCerto
            if(self.proximo() == ')'):
                self.match(')')
                tudoCerto = True
                return tudoCerto
            else:
                tudoCerto = False
                return tudoCerto
        elif(self.var()):
            if(self.proximo() == '('):
                if(self.ativacao()):
                    tudoCerto = True
                    return tudoCerto
                else:
                    tudoCerto = False
                    return tudoCerto
            else:
                return tudoCerto
        elif(self.num_int()):
            return tudoCerto
        else:
            tudoCerto = False
            return tudoCerto
        

    def ativacao(self):
        tudoCerto = True
        #esta chamando direto de var no fator

        if(self.proximo() == '('):
            self.match('(')
            if(not self.args()):
                tudoCerto = False
                return tudoCerto
            if(self.proximo() == ')'):
                self.match(')')
                tudoCerto = True
                return tudoCerto
            else:
                tudoCerto = False
        else:
            tudoCerto = False

        return tudoCerto

    def args(self):
        #opcional
        if(self.arg_lista()):
            return True
        else:
            return False

    def arg_lista(self):
        if(self.expressao()):
            tudoCerto = True
        else:
            tudoCerto = False
            return tudoCerto
        while(self.proximo() == ','):
            self.match(',')
            if(not self.expressao()):
                tudoCerto = False
                return tudoCerto
        return tudoCerto

    def num(self):
        tudoCerto = True
        if(self.proximo() == '+'):
            self.match('+')
            while(self.digito()):
                if(self.proximo() == '.'):
                    self.match('.')
                    if(not self.digito()):
                        tudoCerto = False
                        return tudoCerto
                    else:
                        while(self.digito()):
                            tudoCerto = True
        elif(self.proximo() == '-'):
            self.match('-')
            while(self.digito()):
                if(self.proximo() == '.'):
                    self.match('.')
                    if(not self.digito()):
                        tudoCerto = False
                        return tudoCerto
                    else:
                        while(self.digito()):
                            tudoCerto = True
        elif(self.digito()):
            while(self.digito()):
                if(self.proximo() == '.'):
                    self.match('.')
                    if(not self.digito()):
                        tudoCerto = False
                        return tudoCerto
                    else:
                        while(self.digito()):
                            tudoCerto = True
        else:
            tudoCerto = False
        return tudoCerto


    def num_int(self):
        tudoCerto = True
        digitos = list(self.proximo())
        contador = 0
        if(self.digito(digitos[contador])):
            contador += 1
            while((contador < len(digitos) - 1) and (self.digito(digitos[contador]))):
                tudoCerto = True
                contador += 1
        else:
            tudoCerto = False
            return tudoCerto

        self.setPosicao() #match do num_int
        return tudoCerto

    
    def digito(self, digito):
        tudoCerto = True
        digitos = ['0','1','2','3','4','5','6','7','8','9','+','-']
        if digito not in digitos:
            tudoCerto = False
            return tudoCerto
            
        return tudoCerto

    def ident(self):
        tudoCerto = True

        if(self.posicao < self.qntTokens):
            caracteres = list(self.proximo())
        else:
            return False
        contador = 0
        if(self.letra(caracteres[contador])):
            contador += 1
            while((contador < len(caracteres) - 1) and ((self.letra(caracteres[contador])) or (self.digito(caracteres[contador])))):
                contador += 1
                tudoCerto = True
        else:
            tudoCerto = False
            return tudoCerto

        self.setPosicao() #match do identificador
        return tudoCerto

    
    def letra(self, caractere):
        tudoCerto = True
        letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if caractere not in letras:
            tudoCerto = False
            return tudoCerto
        return tudoCerto
        
    def abre_chave(self):
        return self.match('{')

    def fecha_chave(self):
        return self.match('}')

    def abre_colchete(self):
        return self.match('[')

    def fecha_colchete(self):
        return self.match(']')