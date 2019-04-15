from classes.AnaliseLexica import *

nome_arquivo = input('Digite o nome do arquivo: ')
nome_arquivo = 'exemplos/' + nome_arquivo #nome do arquivo

anLex = AnaliseLexica(nome_arquivo)
anLex.analisar()
anLex.imprimirTokens()
anLex.imprimirErros()
anLex.imprimirTabelaDeSimbolos()

