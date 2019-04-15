
from classes.Token import *
from classes.Caracteres import *
from classes.Erro import *
from functions.funcoes import *
from classes.TabelaDeSimbolos import *

class AnaliseLexica(object):

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo #nome do arquivo
        self.tokens = [] #array de objetos (Token)
        self.erros = [] #array de objetos (Erro)
        self.tabela_de_simbolos = None

    def imprimirTokens(self):
        print('Tokens:')
        for token in self.tokens:
            print('Lexema:', token.lexema, ', Tipo:', token.tipo.name)
    
    def imprimirErros(self):
        print('Erros:')
        if(len(self.erros) > 0):
            for erro in self.erros:
                print('Linha:', erro.linha, ', Coluna:', erro.coluna, ', Caractere:', erro.caractere, ', Descrição:', erro.descricao)
        else:
            print('Não foi encontrado erros léxicos')

    def imprimirTabelaDeSimbolos(self):
        print('Tabela de símbolos:')
        for indice, simbolo in self.tabela_de_simbolos.tabela.items():
            print('Indice:', indice, ', Lexema:', simbolo.lexema)

    def analisar(self):
        info_arquivo = readFile(self.nome_arquivo) #cada elemento é uma linha do arquivo
        numero_linhas_arquivo = numberRows(info_arquivo) #número de linhas do arquivo

        indiceTs = 0 #indice dos lexemas na tabela de símbolos

        #linha e coluna inicial para inicializar a análise léxica do arquivo
        linha_atual = 0
        posicao = 0

        #booleano que verifica se o comentário aberto, foi fechado
        voltando_de_comentario = False

        while (linha_atual < numero_linhas_arquivo):
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
                        token = Token(reservadas[palavra], palavra)
                        self.tokens.append(token)
                    else:
                        token = Token(tipoToken.Ident, palavra, indiceTs)
                        self.tokens.append(token)
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos

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
                                token = Token(tipoToken.NumFloat, palavra, indiceTs)
                                self.tokens.append(token)
                                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                                erro = Erro(linha_atual, posicao, caractere, 0)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                            else:
                                token = Token(tipoToken.NumFloat, palavra, indiceTs)
                                self.tokens.append(token)
                                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                        else:
                            palavra = palavra[:-1] #remove o ponto
                            token = Token(tipoToken.NumInt, palavra, indiceTs)
                            self.tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                            erro = Erro(linha_atual, posicao, caractere, 1)
                            self.erros.append(erro)
                            posicao = tratamentoErroLexico(palavra, posicao, linha)
                    else:
                        if(isLetter(caractere, letras)):
                            erro = Erro(linha_atual, posicao, caractere, 0)
                            self.erros.append(erro)
                            posicao = tratamentoErroLexico(palavra, posicao, linha)                    

                        token = Token(tipoToken.NumInt, palavra, indiceTs)
                        self.tokens.append(token)
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos

                ##VERIFICAR SE É OPERADOR RELACIONAL MENOR OU MENOR IGUAL
                elif(caractere == '<'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelMenorIgual, palavra)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        token = Token(tipoToken.OpRelMenor, palavra)
                        self.tokens.append(token)
                
                ##VERIFICAR SE É OPERADOR RELACIONAL MAIOR OU MAIOR IGUAL
                elif(caractere == '>'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelMaiorIgual, palavra)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        token = Token(tipoToken.OpRelMaior, palavra)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR RELACIONAL DE IGUALDADE OU ATRIBUIÇÃO
                elif(caractere == '='):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelIgual, palavra)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        token = Token(tipoToken.OpAtribuicao, palavra)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR DE DIFERENTE
                elif(caractere == '!'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    if(caractere == '='):
                        palavra += caractere
                        token = Token(tipoToken.OpRelDif, palavra)
                        self.tokens.append(token)
                        posicao += 1
                    else:
                        # exclamação sozinho ou seguido de qualquer outro caractere que não seja '=', 
                        #não é reconhecido pela linguagem, dessa forma é criado um 'falso' token identificador
                        palavra = palavra.replace('!', 'identInvalido') 
                        token = Token(tipoToken.Ident, palavra, indiceTs) 
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                        self.tokens.append(token)
                        erro = Erro(linha_atual, posicao, caractere, 2)
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
                        while(caractere != '/'): #O que está entre /* *\ será descartado
                            if(caractere == '\n'): #é a última posição da linha, vai precisar ir pra linha de baixo
                                linha_atual = linha_atual + 1
                                if(linha_atual == numberRows(info_arquivo)): ##acabou o arquivo e o comentário não foi fechado
                                    erro = Erro(linha_atual, 0, caractere)
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
                            
                    else:
                        token = Token(tipoToken.OpAritDiv, palavra)
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
                                    token = Token(tipoToken.NumFloat, palavra, indiceTs)
                                    self.tokens.append(token)
                                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                                    erro = Erro(linha_atual, posicao, caractere, 0)
                                    self.erros.append(erro)
                                    posicao = tratamentoErroLexico(palavra, posicao, linha)
                                else:
                                    token = Token(tipoToken.NumFloat, palavra, indiceTs)
                                    self.tokens.append(token)
                                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                            else:
                                palavra = palavra[:-1] #remove o ponto
                                token = Token(tipoToken.NumInt, palavra, indiceTs)
                                self.tokens.append(token)
                                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                                erro = Erro(linha_atual, posicao, caractere, 1)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)

                        else:
                            if(isLetter(caractere, letras)):
                                erro = Erro(linha_atual, posicao, caractere, 0)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                            token = Token(tipoToken.NumInt, palavra, indiceTs)
                            self.tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                    else:
                        token = Token(tipoToken.OpAritAdic, palavra)
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
                                    token = Token(tipoToken.NumFloat, palavra, indiceTs)
                                    self.tokens.append(token)
                                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                                    erro = Erro(linha_atual, posicao, caractere, 0)
                                    self.erros.append(erro)
                                    posicao = tratamentoErroLexico(palavra, posicao, linha)
                                else:
                                    token = Token(tipoToken.NumFloat, palavra, indiceTs)
                                    self.tokens.append(token)
                                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                            else:
                                palavra = palavra[:-1] #remove o ponto
                                token = Token(tipoToken.NumInt, palavra, indiceTs)
                                self.tokens.append(token)
                                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                                erro = Erro(linha_atual, posicao, caractere, 1)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                        else:
                            if(isLetter(caractere, letras)):
                                erro = Erro(linha_atual, posicao, caractere, 0)
                                self.erros.append(erro)
                                posicao = tratamentoErroLexico(palavra, posicao, linha)
                            token = Token(tipoToken.NumInt, palavra, indiceTs)
                            self.tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                    else:
                        token = Token(tipoToken.OpAritSub, palavra)
                        self.tokens.append(token)

                ##VERIFICAR SE É OPERADOR ARITMÉTICO DE MULTIPLICAÇÃO
                elif(caractere == '*'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.OpAritMult, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É ABRE CHAVES
                elif(caractere == '{'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.AbreChave, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É FECHA CHAVES
                elif(caractere == '}'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.FechaChave, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É ABRE COLCHETE
                elif(caractere == '['):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.AbreColchete, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É FECHA COLCHETE
                elif(caractere == ']'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.FechaColchete, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É ABRE PARENTESES
                elif(caractere == '('):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.AbreParenteses, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É FECHA PARENTESES
                elif(caractere == ')'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.FechaParenteses, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É SEPARADOR
                elif(caractere == ','):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.Separador, palavra)
                    self.tokens.append(token)

                ##VERIFICAR SE É DELIMITADOR
                elif(caractere == ';'):
                    posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                    palavra += caractere
                    caractere = getCaractere(linha, posicao)
                    token = Token(tipoToken.Delimitador, palavra)
                    self.tokens.append(token)
                
                ##CARACTERE NÃO PERMITIDO NA LINGUAGEM
                else:
                    if(caractere != '\n'): ## \n é permitido para quebra de linha
                        #caractere não é reconhecido pela linguagem, dessa forma é criado um 'falso' token identificador
                        palavra = 'identInvalido' 
                        token = Token(tipoToken.Ident, palavra, indiceTs) 
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                        self.tokens.append(token)
                        erro = Erro(linha_atual, posicao, caractere, 2)
                        self.erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)
                    else:
                        posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                        palavra += caractere
                        caractere = getCaractere(linha, posicao)
            
            #o índice da linha lida é acrescido
            linha_atual = linha_atual + 1 


        ##Criando a tabela de símbolos
        self.tabela_de_simbolos = TabelaDeSimbolos(self.tokens)
