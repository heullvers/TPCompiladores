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

def readFile(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    infoArquivo = []
    for linha in arquivo:
        infoArquivo.append(linha)
    
    arquivo.close()
    infoArquivo[len(infoArquivo)-1] = infoArquivo[len(infoArquivo)-1] + '\n' ##verificar se realmente precisa depois
    return infoArquivo
    

def numberRows(lista_linhas_arquivo): #retorna o número de linhas do código-fonte
        
    return len(lista_linhas_arquivo)

def isLetter(caractere, letras): #verifica se o caractere lido é uma letra
    try:
        return letras[caractere]
    except:
        return False

def isDigit(caractere, digitos): #verifica se o caractere lido é um digito
    try:
        return digitos[int(caractere)]
    except:
        return False

def isReserved(identificador, reservadas): #verifica se o identificador encontrado é uma palavra reservada
    try:
        return reservadas[identificador]
    except:
        return False

def panicMode(palavraAtual, posicao, linha): #ignora os caracteres identificados até finalizar a palavra
    palavra = palavraAtual
    caractere = linha[posicao]
    while((caractere != ' ') and (posicao < len(linha) - 1)):
        posicao += 1
        caractere = linha[posicao]

    return posicao
