from Lexico.classes.AnaliseLexica import *
from Sintatico.classes.AnaliseSintatica import *

nome_arquivo = input('Digite o nome do arquivo: ')
nome_arquivo = 'exemplos/' + nome_arquivo #nome do arquivo

anLex = AnaliseLexica(nome_arquivo)

#anLex.imprimirTokens()
anSint = AnaliseSintatica(anLex.tokens)



#anLex.imprimirErros()
#anLex.imprimirTabelaDeSimbolos()





