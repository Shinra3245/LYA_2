grammar Expr;

root : expr EOF ;

expr: ID IGUAL NUM;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
IGUAL: '=';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
