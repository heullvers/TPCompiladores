import enum
from enum import Enum

#enumeração dos tipos possíveis
class tipoToken(Enum):
    Letra, Digito, NumInt, NumFloat, OpAritSub, OpAritAdic, OpAritMult, OpAritDiv, OpAtribuicao, OpRelMenorIgual, OpRelMenor, OpRelMaior, OpRelMaiorIgual, OpRelIgual, OpRelDif, AbreChave, FechaChave, AbreColchete, FechaColchete, AbreParenteses, FechaParenteses, Separador, Delimitador, Comentario, Ident, PRInt, PRFloat, PRChar, PRStruct, PRIf, PRElse, PRWhile, PRVoid, PRReturn = range(34)