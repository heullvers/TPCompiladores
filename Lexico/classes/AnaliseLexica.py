
from classes.Token import *
from classes.Caracteres import *
from classes.Erro import *
from functions.funcoes import *
from classes.teste import *

class AnaliseLexica(object):

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo #nome do arquivo
        self.tokens = [] #array de objetos (Token)
        self.erros = [] #array de objetos (Erro)
        self.tabela_de_simbolos = {}
        self.indiceTs = 0 #indice inicial dos lexemas na tabela de símbolos
        self.analisar()

    def adicionarSimboloaTS(self, lexema):
        jaExiste = False
        key = False
        for simbolo in self.tabela_de_simbolos.values():
            if(simbolo.lexema == lexema):
                valor = simbolo
                jaExiste = True
                for chave in self.tabela_de_simbolos:
                    if(self.tabela_de_simbolos[chave] == valor):
                        key = chave
                break

        if(not jaExiste):
            self.tabela_de_simbolos[self.indiceTs] = Simbolo(lexema, self.indiceTs) #cria-se um novo símbolo se não existe o valor na hash

        return key
        
    def incrementarIndiceTS(self):
        self.indiceTs = self.indiceTs + 1

    def getTabelaSimbolos(self):
        return self.tabela_de_simbolos

    def imprimirTokens(self):
        print('TOKENS:')
        for token in self.tokens:
            print('Lexema:', token.lexema, ', Tipo:', token.tipo.name, ', Linha:' , token.linha, ' Coluna: ', token.coluna, ' Indice: ', token.indiceTs)
    
    def imprimirErros(self):
        print('ERROS:')
        if(len(self.erros) > 0):
            for erro in self.erros:
                print('Linha:', erro.linha, ', Coluna:', erro.coluna, ', Caractere:', erro.caractere, ', Descrição:', erro.descricao)
        else:
            print('Não foi encontrado erros léxicos')

    def imprimirTabelaDeSimbolos(self):
        print('TABELA DE SÍMBOLOS:')
        for indice, simbolo in self.tabela_de_simbolos.items():
            print('Indice:', indice, ', Lexema:', simbolo.lexema)

    def analisar(self):

        info_arquivo = readFile(self.nome_arquivo) #cada elemento é uma linha do arquivo
        numero_linhas_arquivo = numberRows(info_arquivo) #número de linhas do arquivo

        #linha e coluna inicial para inicializar a análise léxica do arquivo
        linha_atual = 0
        posicao = 0

        #booleano que verifica se o comentário aberto, foi fechado
        voltando_de_comentario = False

        while (linha_atual < numero_linhas_arquivo): #enquanto não acabar as linhas do arquivo
            if(not voltando_de_comentario): #se não está voltando de um fechamento de comentário, inicia-se a leitura na posição 0
                posicao = 0
            else:
                linha_atual = linha_atual - 1 

            voltando_de_comentario = False #retorna ao valor inicial, pois não está sendo feito mais a leitura de um comentário
            linha = info_arquivo[linha_atual]

            while (posicao < len(linha) - 1): ##enquanto não ler a linha toda
                leitura_proximo = getNextCaractere(linha, posicao) #lê o primeiro caractere da palavra
                caractere = leitura_proximo['caractere'] #recebe o caractere
                posicao = leitura_proximo['posicao'] #recebe a posicao atual do ponteiro que está lendo o arquivo
                palavra = "" #palavra inicialmente vazia

                ### VERIFICAR SE É UM IDENTIFICADOR
                if(isLetter(caractere, letras)): #palavra iniciada com LETRA
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    while(isLetter(caractere, letras) or isDigit(caractere,digitos)): #loop de LETRAS e DIGITOS
                        palavra += caractere
                        posicao += 1
                        caractere = getCaractere(linha, posicao)
                    #verifica se o identificador é uma palavra reservada da linguagem
                    if(isReserved(palavra, reservadas)):
                        token = Token(reservadas[palavra], palavra, linha_atual, posicao)
                        self.tokens.append(token)
                    else:
                        aux_indice_ts = self.adicionarSimboloaTS(palavra)
                        if(aux_indice_ts is False):
                            token = Token(tipoToken.Ident, palavra, linha_atual, posicao, self.indiceTs)
                            self.incrementarIndiceTS()
                        else:
                            token = Token(tipoToken.Ident, palavra, linha_atual, posicao, aux_indice_ts)
                        self.tokens.append(token)

                ### VERIFICAR SE É UM NÚMERO INTEIRO/FLUTUANTE (SEM SINAL)
                elif(isDigit(caractere,digitos)): #palavra iniciada com DIGITO
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    while(isDigit(caractere,digitos)): #enquanto houver digito
                        palavra += caractere
                        posicao += 1
                        caractere = getCaractere(linha, posicao)
                    if(caractere == '.'):
                        palavra += caractere
                        posicao += 1
                        caractere = getCaractere(linha, posicao)
                        if(isDigit(caractere,digitos)):
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)
                            while(isDigit(caractere,digitos)): #enquanto houver digito
                                palavra += caractere
                                posicao += 1
                                caractere = getCaractere(linha, posicao)
                            if(isLetter(caractere, letras)):
                                aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                if(aux_indice_ts is False):
                                    token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, self.indiceTs)
                                    self.incrementarIndiceTS()
                                else:
                                    token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, aux_indice_ts)
                                self.tokens.append(token)
                                erro = Erro(linha_atual, posicao, caractere, 0)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                            else:
                                aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                if(aux_indice_ts is False):
                                    token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, self.indiceTs)
                                    self.incrementarIndiceTS()
                                else:
                                    token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, aux_indice_ts)
                                self.tokens.append(token)
                        else:
                            palavra = palavra[:-1] #remove o ponto
                            aux_indice_ts = self.adicionarSimboloaTS(palavra)

                            if(aux_indice_ts is False):
                                token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, self.indiceTs)
                                self.incrementarIndiceTS()
                            else:
                                token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, aux_indice_ts)
                            self.tokens.append(token)
                            erro = Erro(linha_atual, posicao, caractere, 1)
                            self.erros.append(erro)
                            posicao = tratamentoErroLexico(palavra, posicao, linha)
                    else:                  
                        aux_indice_ts = self.adicionarSimboloaTS(palavra)
                        if(aux_indice_ts is False):
                            token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, self.indiceTs)
                            self.incrementarIndiceTS()
                        else:
                            token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, aux_indice_ts)
                        self.tokens.append(token)

                        if(isLetter(caractere, letras)):
                            erro = Erro(linha_atual, posicao, caractere, 0)
                            self.erros.append(erro)
                            posicao = tratamentoErroLexico(palavra, posicao, linha)  

                ##VERIFICAR SE É OPERADOR RELACIONAL MENOR OU MENOR IGUAL
                elif(caractere == '<'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelMenorIgual, palavra, linha_atual, posicao)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        token = Token(tipoToken.OpRelMenor, palavra, linha_atual, posicao)
                        self.tokens.append(token)
                
                ##VERIFICAR SE É OPERADOR RELACIONAL MAIOR OU MAIOR IGUAL
                elif(caractere == '>'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelMaiorIgual, palavra, linha_atual, posicao)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        token = Token(tipoToken.OpRelMaior, palavra, linha_atual, posicao)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR RELACIONAL DE IGUALDADE OU ATRIBUIÇÃO
                elif(caractere == '='):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelIgual, palavra, linha_atual, posicao)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        token = Token(tipoToken.OpAtribuicao, palavra, linha_atual, posicao)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR DE DIFERENTE
                elif(caractere == '!'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelDif, palavra, linha_atual, posicao)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        # exclamação sozinho ou seguido de qualquer outro caractere que não seja '=', 
                        #não é reconhecido pela linguagem
                        erro = Erro(linha_atual, posicao, '!', 4)
                        self.erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)

                ##VERIFICAR SE É OPERADOR ARITMÉTICO DE DIVISÃO OU COMENTÁRIO
                elif(caractere == '/'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '*'):
                        posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                        palavra += caractere
                        caractere = getCaractere(linha, posicao)
                        alertaFalso = True
                        while((alertaFalso) and (linha_atual < numberRows(info_arquivo))):
                            alertaFalso = False #avisa que foi encontrado um /, mas não há um asterisco anteriormente para o comentário ser fechado
                            while(caractere != '/'): #O que está entre /* *\ será descartado
                                alertaFalso = False
                                if(caractere == '\n'): #é a última posição da linha, vai precisar ir pra linha de baixo
                                    linha_atual = linha_atual + 1
                                    if(linha_atual == numberRows(info_arquivo)): ##acabou o arquivo e o comentário não foi fechado
                                        erro = Erro(linha_atual, 0, ' ', 3)
                                        self.erros.append(erro)
                                        break
                                    else:
                                        posicao = 0
                                        linha = info_arquivo[linha_atual]
                                        leitura_proximo = getNextCaractere(linha, posicao)
                                        caractere = leitura_proximo['caractere'] #recebe o caractere
                                        posicao = leitura_proximo['posicao'] #recebe a posicao atual do ponteiro que está lendo o arquivo
                                else: #ainda não foi identificado o / para haver a possibilidade de finalizar o comentário e não está no final da linha
                                    posicao += 1
                                    leitura_proximo = getNextCaractere(linha, posicao)
                                    caractere = leitura_proximo['caractere'] #recebe o caractere
                                    posicao = leitura_proximo['posicao'] #recebe a posicao atual do ponteiro que está lendo o arquivo
                            #foi encontrado um /
                            caractere = getCaractere(linha, posicao - 1) 
                            posicao += 1 
                            #verifica se o caractere anterior ao / é um * para fechar o comentário
                            if(caractere == '*'):
                                caractere = getCaractere(linha, posicao)
                                voltando_de_comentario = True #necessário para manter a posição de leitura da linha do arquivo
                            else:
                                caractere = getCaractere(linha, posicao)
                                alertaFalso = True
                            
                    else:
                        token = Token(tipoToken.OpAritDiv, palavra, linha_atual, posicao)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR ARITMÉTICO DE ADIÇÃO OU NÚMERO INTEIRO/FLUTUANTE COM SINAL POSITIVO
                elif(caractere == '+'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(isDigit(caractere,digitos)):
                        posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                        palavra += caractere
                        caractere = getCaractere(linha, posicao)
                        while(isDigit(caractere,digitos)): #enquanto houver digito
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)
                        if(caractere == '.'):
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)
                            if(isDigit(caractere,digitos)):
                                palavra += caractere
                                posicao += 1
                                caractere = getCaractere(linha, posicao)
                                while(isDigit(caractere,digitos)): #enquanto houver digito
                                    palavra += caractere
                                    posicao += 1
                                    caractere = getCaractere(linha, posicao)
                                if(isLetter(caractere, letras)):
                                    aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                    if(aux_indice_ts is False):
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, self.indiceTs)
                                        self.incrementarIndiceTS()
                                    else:
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, aux_indice_ts)
                                    self.tokens.append(token)
                                    erro = Erro(linha_atual, posicao, caractere, 0)
                                    self.erros.append(erro)
                                    posicao = tratamentoErroLexico(palavra, posicao, linha)
                                else:
                                    aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                    if(aux_indice_ts is False):
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, self.indiceTs)
                                        self.incrementarIndiceTS()
                                    else:
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, aux_indice_ts)
                                    self.tokens.append(token)
                            else:
                                palavra = palavra[:-1] #remove o ponto
                                aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                if(aux_indice_ts is False):
                                    token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, self.indiceTs)
                                    self.incrementarIndiceTS()
                                else:
                                    token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, aux_indice_ts)
                                self.tokens.append(token)
                                erro = Erro(linha_atual, posicao, caractere, 1)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)

                        else:
                            if(isLetter(caractere, letras)):
                                erro = Erro(linha_atual, posicao, caractere, 0)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                            aux_indice_ts = self.adicionarSimboloaTS(palavra)
                            if(aux_indice_ts is False):
                                token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, self.indiceTs)
                                self.incrementarIndiceTS()
                            else:
                                token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, aux_indice_ts)
                            self.tokens.append(token)
                    else:
                        token = Token(tipoToken.OpAritAdic, palavra, linha_atual, posicao)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR ARITMÉTICO DE SUBTRAÇÃO OU NÚMERO INTEIRO/FLUTUANTE COM SINAL NEGATIVO
                elif(caractere == '-'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(isDigit(caractere,digitos)):
                        posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                        palavra += caractere
                        caractere = getCaractere(linha, posicao)
                        while(isDigit(caractere,digitos)): #enquanto houver digito
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)
                        if(caractere == '.'):
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)
                            if(isDigit(caractere,digitos)):
                                palavra += caractere
                                posicao += 1
                                caractere = getCaractere(linha, posicao)
                                while(isDigit(caractere,digitos)): #enquanto houver digito
                                    palavra += caractere
                                    posicao += 1
                                    caractere = getCaractere(linha, posicao)
                                if(isLetter(caractere, letras)):
                                    aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                    if(aux_indice_ts is False):
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, self.indiceTs)
                                        self.incrementarIndiceTS()
                                    else:
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, aux_indice_ts)
                                    self.tokens.append(token)
                                    erro = Erro(linha_atual, posicao, caractere, 0)
                                    self.erros.append(erro)
                                    posicao = tratamentoErroLexico(palavra, posicao, linha)
                                else:
                                    aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                    if(aux_indice_ts is False):
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, self.indiceTs)
                                        self.incrementarIndiceTS()
                                    else:
                                        token = Token(tipoToken.NumFloat, palavra, linha_atual, posicao, aux_indice_ts)
                                    self.tokens.append(token)
                            else:
                                palavra = palavra[:-1] #remove o ponto
                                aux_indice_ts = self.adicionarSimboloaTS(palavra)
                                if(aux_indice_ts is False):
                                    token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, self.indiceTs)
                                    self.incrementarIndiceTS()
                                else:
                                    token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, aux_indice_ts)
                                self.tokens.append(token)
                                erro = Erro(linha_atual, posicao, caractere, 1)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                        else:
                            if(isLetter(caractere, letras)):
                                erro = Erro(linha_atual, posicao, caractere, 0)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                            aux_indice_ts = self.adicionarSimboloaTS(palavra)
                            if(aux_indice_ts is False):
                                token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, self.indiceTs)
                                self.incrementarIndiceTS()
                            else:
                                token = Token(tipoToken.NumInt, palavra, linha_atual, posicao, aux_indice_ts)
                            self.tokens.append(token)
                    else:
                        token = Token(tipoToken.OpAritSub, palavra, linha_atual, posicao)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR ARITMÉTICO DE MULTIPLICAÇÃO
                elif(caractere == '*'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.OpAritMult, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É ABRE CHAVES
                elif(caractere == '{'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.AbreChave, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É FECHA CHAVES
                elif(caractere == '}'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.FechaChave, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É ABRE COLCHETE
                elif(caractere == '['):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.AbreColchete, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É FECHA COLCHETE
                elif(caractere == ']'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.FechaColchete, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É ABRE PARENTESES
                elif(caractere == '('):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.AbreParenteses, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É FECHA PARENTESES
                elif(caractere == ')'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.FechaParenteses, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É SEPARADOR
                elif(caractere == ','):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.Separador, palavra, linha_atual, posicao)
                    self.tokens.append(token)

                ##VERIFICAR SE É DELIMITADOR
                elif(caractere == ';'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.Delimitador, palavra, linha_atual, posicao)
                    self.tokens.append(token)
                
                ##CARACTERE NÃO PERMITIDO NA LINGUAGEM
                else:
                    if(caractere != '\n'): ## \n é permitido para quebra de linha
                        #caractere não é reconhecido pela linguagem
                        erro = Erro(linha_atual, posicao, caractere, 2)
                        self.erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)
                    else: #é igual a \n
                        posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                        palavra += caractere
                        caractere = getCaractere(linha, posicao)
            
            #o índice da linha lida é acrescido
            linha_atual = linha_atual + 1 


        ##Criando a tabela de símbolos
        #self.tabela_de_simbolos = TabelaDeSimbolos(self.tokens)