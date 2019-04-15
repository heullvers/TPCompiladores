from classes.EnumTipoToken import *

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