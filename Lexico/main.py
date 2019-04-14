
from Token import *
from Caracteres import *
from Erro import *
from funcoes import *
from TabelaDeSimbolos import *


nome_arquivo = 'exemplos/exemplo4.txt' #nome do arquivo
info_arquivo = readFile(nome_arquivo) #cada elemento é uma linha do arquivo
numero_linhas_arquivo = numberRows(info_arquivo) #número de linhas do arquivo

tokens = [] #array de objetos (Token)
erros = [] #array de objetos (Erro)
indiceTs = 0 #indice dos identificadores na tabela de símbolos

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
                tokens.append(token)
            else:
                token = Token(tipoToken.Ident, palavra, indiceTs)
                tokens.append(token)
                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador

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
                        tokens.append(token)
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador
                        erro = Erro(linha_atual, posicao, caractere, 0)
                        erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)
                    else:
                        token = Token(tipoToken.NumFloat, palavra, indiceTs)
                        tokens.append(token)
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador
                else:
                    palavra = palavra[:-1] #remove o ponto
                    token = Token(tipoToken.NumInt, palavra, indiceTs)
                    tokens.append(token)
                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                    erro = Erro(linha_atual, posicao, caractere, 1)
                    erros.append(erro)
                    posicao = tratamentoErroLexico(palavra, posicao, linha)
            else:
                if(isLetter(caractere, letras)):
                    erro = Erro(linha_atual, posicao, caractere, 0)
                    erros.append(erro)
                    posicao = tratamentoErroLexico(palavra, posicao, linha)                    

                token = Token(tipoToken.NumInt, palavra, indiceTs)
                tokens.append(token)
                indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos

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
                # exclamação sozinho ou seguido de qualquer outro caractere que não seja '=', 
                #não é reconhecido pela linguagem, dessa forma é criado um 'falso' token identificador
                palavra = palavra.replace('!', 'identInvalido') 
                token = Token(tipoToken.Ident, palavra) 
                tokens.append(token)
                erro = Erro(linha_atual, posicao, caractere, 2)
                erros.append(erro)
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
                    caractere = getCaractere(linha, posicao)
                    
            else:
                token = Token(tipoToken.OpAritDiv, palavra)
                tokens.append(token)

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
                            tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador
                            erro = Erro(linha_atual, posicao, caractere, 0)
                            erros.append(erro)
                            posicao = tratamentoErroLexico(palavra, posicao, linha)
                        else:
                            token = Token(tipoToken.NumFloat, palavra, indiceTs)
                            tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador
                    else:
                        palavra = palavra[:-1] #remove o ponto
                        token = Token(tipoToken.NumInt, palavra, indiceTs)
                        tokens.append(token)
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                        erro = Erro(linha_atual, posicao, caractere, 1)
                        erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)

                else:
                    if(isLetter(caractere, letras)):
                        erro = Erro(linha_atual, posicao, caractere, 0)
                        erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)
                    token = Token(tipoToken.NumInt, palavra, indiceTs)
                    tokens.append(token)
                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
            else:
                token = Token(tipoToken.OpAritAdic, palavra)
                tokens.append(token)

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
                            tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador
                            erro = Erro(linha_atual, posicao, caractere, 0)
                            erros.append(erro)
                            posicao = tratamentoErroLexico(palavra, posicao, linha)
                        else:
                            token = Token(tipoToken.NumFloat, palavra, indiceTs)
                            tokens.append(token)
                            indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos para o próximo identificador
                    else:
                        palavra = palavra[:-1] #remove o ponto
                        token = Token(tipoToken.NumInt, palavra, indiceTs)
                        tokens.append(token)
                        indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
                        erro = Erro(linha_atual, posicao, caractere, 1)
                        erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)
                else:
                    if(isLetter(caractere, letras)):
                        erro = Erro(linha_atual, posicao, caractere, 0)
                        erros.append(erro)
                        posicao = tratamentoErroLexico(palavra, posicao, linha)
                    token = Token(tipoToken.NumInt, palavra, indiceTs)
                    tokens.append(token)
                    indiceTs += 1 #acrescenta 1 ao índice da tabela de símbolos
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
                #caractere não é reconhecido pela linguagem, dessa forma é criado um 'falso' token identificador
                palavra = 'identInvalido' 
                token = Token(tipoToken.Ident, palavra) 
                tokens.append(token)
                erro = Erro(linha_atual, posicao, caractere, 2)
                erros.append(erro)
                posicao = tratamentoErroLexico(palavra, posicao, linha)
            else:
                posicao += 1 #deixa o ponteiro apontado para o pŕoximo caractere a ser lido
                palavra += caractere
                caractere = getCaractere(linha, posicao)
    
    #o índice da linha lida é acrescido
    linha_atual = linha_atual + 1 


##Criando a tabela de símbolos
tabela_de_simbolos = TabelaDeSimbolos(tokens)



print('TOKENS:', tokens)
print('ERROS:', erros)
print('TABELA DE SIMBOLOS', tabela_de_simbolos.tabela)    
