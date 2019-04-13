from Token import *
from Erro import *


import enum
from enum import Enum

#enumeração dos tipos possíveis
class tipoToken(Enum):
    Letra, Digito, NumInt, NumFloat, OpAritSub, OpAritAdic, OpAritMult, OpAritDiv, OpAtribuicao, OpRelMenorIgual, OpRelMenor, OpRelMaior, OpRelMaiorIgual, OpRelIgual, OpRelDif, AbreChave, FechaChave, AbreColchete, FechaColchete, AbreParenteses, FechaParenteses, Separador, Delimitador, Comentario, Ident, PRInt, PRFloat, PRChar, PRStruct, PRIf, PRElse, PRWhile, PRVoid, PRReturn = range(34)

#array de Tokens
tokens = []

def getNextCaractere(linha, posicao): #lê um caractere do arquivo ignorando os espaços
    
    caractere = linha[posicao]
    while(caractere == ' '):
        posicao = posicao + 1
        caractere = linha[posicao]

    return {'caractere':linha[posicao], 'posicao': posicao }

def getCaractere(linha, posicao): #lê um caractere do arquivo
    try:
        return linha[posicao]
    except:
        return '\n' #retorna quebra de linha na última linha para finalizar a divisão de lexemas do arquivo

def lerArquivo(arquivo):
    infoArquivo = []
    for linha in arquivo:
        infoArquivo.append(linha)
    
    infoArquivo[len(infoArquivo)-1] = infoArquivo[len(infoArquivo)-1] + '\n'
    return infoArquivo
    

def numberRows(arquivo): #retorna o número de linhas do código-fonte
    qnt_linhas = 0
    for linha in arquivo:
        qnt_linhas += 1
    arquivo.seek(0)
    return qnt_linhas

def isLetter(caractere): #verifica se o caractere lido é uma letra
    try:
        return letras[caractere]
    except:
        return False

def isDigit(caractere): #verifica se o caractere lido é um digito
    try:
        return digitos[int(caractere)]
    except:
        return False

def isReserved(identificador): #verifica se o identificador encontrado é uma palavra reservada
    try:
        return reservadas[identificador]
    except:
        return False

#letras permitidas na linguagem
letras = {'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True, 'g': True, 'h': True, 'i': True, 'j': True, 'k': True,
'l': True, 'm': True, 'n': True, 'o': True, 'p': True, 'q': True, 'r': True, 's': True, 't': True, 'u': True, 'v': True, 'w': True, 'x': True,
'y': True, 'z': True}

#digitos
digitos = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}

#palavras reservadas da linguagem
reservadas = {'int': tipoToken.PRInt, 'float': tipoToken.PRFloat,
 'char': tipoToken.PRChar, 'struct': tipoToken.PRStruct, 'if': tipoToken.PRIf,
  'else': tipoToken.PRElse, 'while': tipoToken.PRWhile, 'void': tipoToken.PRVoid, 'return': tipoToken.PRReturn}

#indice dos identificadores na tabela de símbolos
indiceTs = 0

nome_arquivo = 'exemplo1.txt' #nome do arquivo
arquivo = open(nome_arquivo, 'r')

info_arquivo = lerArquivo(arquivo) #retorna uma lista em que cada elemento é uma linha do arquivo
numero_linhas_arquivo = len(info_arquivo)

erros = []
voltando_de_comentario = False

linha_atual = 0
posicao = 0


while (linha_atual < numero_linhas_arquivo):
    if(not voltando_de_comentario): #se não está voltando de um fechamento de comentário, inicia-se a leitura na posição 0
        posicao = 0
    else:
        linha_atual = linha_atual - 1 

    voltando_de_comentario = False #retorna ao valor inicial, pois não está sendo feito mais a leitura de um comentário
    linha = info_arquivo[linha_atual]

    while (posicao < len(linha) - 1):
        leitura_proximo = getNextCaractere(linha, posicao) #lê o primeiro caractere da palavra
        caractere = leitura_proximo['caractere'] #recebe o caractere
        posicao = leitura_proximo['posicao'] #recebe a posicao atual do ponteiro que está lendo o arquivo
        palavra = "" #palavra inicialmente vazia
        ### VERIFICAR SE É UM IDENTIFICADOR
        if(isLetter(caractere)): #palavra iniciada com LETRA

            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            while(isLetter(caractere) or isDigit(caractere)): #loop de LETRAS e DIGITOS
                palavra += caractere
                posicao += 1
                caractere = getCaractere(linha, posicao)

            #verifica se o identificador é uma palavra reservada da linguagem
            if(isReserved(palavra)):
                token = Token(reservadas[palavra], palavra)
                tokens.append(token)
            else:
                token = Token(tipoToken.Ident, palavra, indiceTs)
                tokens.append(token)
                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador

        ### VERIFICAR SE É UM NÚMERO INTEIRO/FLUTUANTE (SEM SINAL)
        elif(isDigit(caractere)): #palavra iniciada com DIGITO
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            while(isDigit(caractere)): #enquanto houver digito
                palavra += caractere
                posicao += 1
                caractere = getCaractere(linha, posicao)

            if(caractere == '.'):
                palavra += caractere
                posicao += 1
                caractere = getCaractere(linha, posicao)

                if(isDigit(caractere)):
                    palavra += caractere
                    posicao += 1
                    caractere = getCaractere(linha, posicao)

                    while(isDigit(caractere)): #enquanto houver digito
                        palavra += caractere
                        posicao += 1
                        caractere = getCaractere(linha, posicao)

                    token = Token(tipoToken.NumFloat, palavra)
                    tokens.append(token)
                else:
                    erro = Erro(linha_atual, posicao, caractere)
                    erros.append(erro)
                
            else:
                token = Token(tipoToken.NumInt, palavra)
                tokens.append(token)

        ##VERIFICAR SE É OPERADOR RELACIONAL MENOR OU MENOR IGUAL
        elif(caractere == '<'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(caractere == '='):
                palavra += caractere
                token = Token(tipoToken.OpRelMenorIgual, palavra)
                tokens.append(token)
                posicao += 1
            else:
                token = Token(tipoToken.OpRelMenor, palavra)
                tokens.append(token)
        
        ##VERIFICAR SE É OPERADOR RELACIONAL MAIOR OU MAIOR IGUAL
        elif(caractere == '>'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(caractere == '='):
                palavra += caractere
                token = Token(tipoToken.OpRelMaiorIgual, palavra)
                tokens.append(token)
                posicao += 1
            else:
                token = Token(tipoToken.OpRelMaior, palavra)
                tokens.append(token)

        ##VERIFICAR SE É OPERADOR RELACIONAL DE IGUALDADE OU ATRIBUIÇÃO
        elif(caractere == '='):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(caractere == '='):
                palavra += caractere
                token = Token(tipoToken.OpRelIgual, palavra)
                tokens.append(token)
                posicao += 1
            else:
                token = Token(tipoToken.OpAtribuicao, palavra)
                tokens.append(token)

        ##VERIFICAR SE É OPERADOR DE DIFERENTE
        elif(caractere == '!'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(caractere == '='):
                palavra += caractere
                token = Token(tipoToken.OpRelDif, palavra)
                tokens.append(token)
                posicao += 1
            else:
                erro = Erro(linha_atual, posicao, caractere)
                erros.append(erro)

        ##VERIFICAR SE É OPERADOR ARITMÉTICO DE DIVISÃO OU **********COMENTÁRIO**********
        elif(caractere == '/'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(caractere == '*'):
                posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                palavra += caractere
                caractere = getCaractere(linha, posicao)
               # while((not comentario_fechado) and (not fim_arquivo)) :
                while(caractere != '/'): #O que está entre /* *\ será descartado
                    if(caractere == '\n'): #é a última posição da linha, vai precisar ir pra linha de baixo
                        #if(linha_atual == numberRows(arquivo)):

                        linha_atual = linha_atual + 1
                        if(linha_atual == numberRows(arquivo)): ##acabou o arquivo e o comentário não foi fechado
                            erro = Erro(linha_atual, 0, caractere)
                            erros.append(erro)
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
                    #posicao += 1
                    caractere = getCaractere(linha, posicao)
                    
            else:
                token = Token(tipoToken.OpAritDiv, palavra)
                tokens.append(token)

        ##VERIFICAR SE É OPERADOR ARITMÉTICO DE ADIÇÃO OU NÚMERO INTEIRO/FLUTUANTE COM SINAL POSITIVO
        elif(caractere == '+'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(isDigit(caractere)):
                posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                palavra += caractere
                caractere = getCaractere(linha, posicao)

                while(isDigit(caractere)): #enquanto houver digito
                    palavra += caractere
                    posicao += 1
                    caractere = getCaractere(linha, posicao)

                if(caractere == '.'):
                    palavra += caractere
                    posicao += 1
                    caractere = getCaractere(linha, posicao)

                    if(isDigit(caractere)):
                        palavra += caractere
                        posicao += 1
                        caractere = getCaractere(linha, posicao)

                        while(isDigit(caractere)): #enquanto houver digito
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)

                        token = Token(tipoToken.NumFloat, palavra)
                        tokens.append(token)
                    else:
                        erro = Erro(linha_atual, posicao, caractere)
                        erros.append(erro)
                else:
                    token = Token(tipoToken.NumInt, palavra)
                    tokens.append(token)
            else:
                token = Token(tipoToken.OpAritAdic, palavra)
                tokens.append(token)

            ##VERIFICAR SE É OPERADOR ARITMÉTICO DE SUBTRAÇÃO OU NÚMERO INTEIRO/FLUTUANTE COM SINAL NEGATIVO
        elif(caractere == '-'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)

            if(isDigit(caractere)):
                posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                palavra += caractere
                caractere = getCaractere(linha, posicao)

                while(isDigit(caractere)): #enquanto houver digito
                    palavra += caractere
                    posicao += 1
                    caractere = getCaractere(linha, posicao)

                if(caractere == '.'):
                    palavra += caractere
                    posicao += 1
                    caractere = getCaractere(linha, posicao)

                    if(isDigit(caractere)):
                        palavra += caractere
                        posicao += 1
                        caractere = getCaractere(linha, posicao)

                        while(isDigit(caractere)): #enquanto houver digito
                            palavra += caractere
                            posicao += 1
                            caractere = getCaractere(linha, posicao)

                        token = Token(tipoToken.NumFloat, palavra)
                        tokens.append(token)
                    else:
                        erro = Erro(linha_atual, posicao, caractere)
                        erros.append(erro)
                else:
                    token = Token(tipoToken.NumInt, palavra)
                    tokens.append(token)
            else:
                token = Token(tipoToken.OpAritSub, palavra)
                tokens.append(token)

        ##VERIFICAR SE É OPERADOR ARITMÉTICO DE MULTIPLICAÇÃO
        elif(caractere == '*'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.OpAritMult, palavra)
            tokens.append(token)

        ##VERIFICAR SE É ABRE CHAVES
        elif(caractere == '{'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.AbreChave, palavra)
            tokens.append(token)

        ##VERIFICAR SE É FECHA CHAVES
        elif(caractere == '}'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.FechaChave, palavra)
            tokens.append(token)

        ##VERIFICAR SE É ABRE COLCHETE
        elif(caractere == '['):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.AbreColchete, palavra)
            tokens.append(token)

        ##VERIFICAR SE É FECHA COLCHETE
        elif(caractere == ']'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.FechaColchete, palavra)
            tokens.append(token)

        ##VERIFICAR SE É ABRE PARENTESES
        elif(caractere == '('):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.AbreParenteses, palavra)
            tokens.append(token)

        ##VERIFICAR SE É FECHA PARENTESES
        elif(caractere == ')'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.FechaParenteses, palavra)
            tokens.append(token)

        ##VERIFICAR SE É SEPARADOR
        elif(caractere == ','):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.Separador, palavra)
            tokens.append(token)

        ##VERIFICAR SE É DELIMITADOR
        elif(caractere == ';'):
            posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
            palavra += caractere
            caractere = getCaractere(linha, posicao)
            token = Token(tipoToken.Delimitador, palavra)
            tokens.append(token)
        
        
        ##CARACTERE NÃO PERMITIDO NA LINGUAGEM
        else:
            if(caractere != '\n'): ## \n é permitido para quebra de linha
                print('entrei')
                erro = Erro(linha_atual, posicao, caractere)
                erros.append(erro)
                posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                palavra += caractere
                caractere = getCaractere(linha, posicao)
            else:
                posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                palavra += caractere
                caractere = getCaractere(linha, posicao)
    
    #o índice da linha lida é acrescido
    linha_atual = linha_atual + 1 

print('TOKENS:')
for token in tokens:
     print(token.tipo)
     print(token.lexema)

print('ERROS')
for erro in erros:
    print(erro.linha)
    print(erro.coluna)
    print(erro.caractere)
arquivo.close()



    
