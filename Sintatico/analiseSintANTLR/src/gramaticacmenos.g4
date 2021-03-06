grammar gramaticacmenos;

programa: declaracao_lista;
declaracao_lista: (declaracao)+;
declaracao: var_declaracao | fun_declaracao;
var_declaracao: tipo_especificador ident ';' | tipo_especificador ident abre_colchete
num_int fecha_colchete (abre_colchete num_int fecha_colchete)*;
tipo_especificador: 'int'|'float'|'char'|'void'|'struct' ident abre_chave atributos_declaracao fecha_chave;
atributos_declaracao: var_declaracao (var_declaracao)*;
fun_declaracao: tipo_especificador ident '(' params ')' composto_decl;
params: param_lista | 'void';
param_lista: param (',' param)*;
param: tipo_especificador ident | tipo_especificador ident abre_colchete fecha_colchete;
composto_decl: abre_chave local_declaracoes comando_lista fecha_chave;
local_declaracoes: (var_declaracao)*;
comando_lista: (comando)*;
comando: expressao_decl | composto_decl | selecao_decl | iteracao_decl | retorno_decl;
expressao_decl: expressao ';' | ';';
selecao_decl: 'if' '(' expressao ')' comando | 'if' '(' expressao ')' comando
'else' comando;
iteracao_decl: 'while' '(' expressao ')' comando;
retorno_decl: 'return' ';' | 'return' expressao;
expressao: var '=' expressao | expressao_simples;
var: ident | ident abre_colchete expressao fecha_colchete (abre_colchete expressao fecha_colchete)*;
expressao_simples: expressao_soma relacional expressao_soma | expressao_soma;
relacional: '<=' | '<' | '>' | '>=' | '==' | '!=';
expressao_soma: termo ( soma termo )*;
soma: '+' | '-';
termo: fator (mult fator)*;
mult: '*' | '/';
fator: '(' expressao ')' | var | ativacao | num | num_int;
ativacao: ident '(' args ')';
args: arg_lista;
arg_lista: expressao (',' expressao)*;
num: soma digito (digito '.' digito (digito)*)* | digito (digito '.' digito (digito)*)*;
num_int: digito (digito)*;
digito: '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';
ident: letra ( letra | digito )*;
letra: 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|
'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z';
abre_chave: '{';
fecha_chave: '}';
abre_colchete: '[';
fecha_colchete: ']';

WS:[ \t\r\n\u000C]+ -> skip;
