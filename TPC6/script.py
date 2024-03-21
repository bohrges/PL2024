'''
GRAMÁTICA

G = {T,N,S,P}

REGRAS:


PROGRAMA -> INSTRUCOES
INSTRUCOES -> INSTRUCAO INSTRUCOES
            | ε
INSTRUCAO -> ATRIBUICAO
           | ENTRADA
           | SAIDA
ATRIBUICAO -> ID '=' EXP
ENTRADA -> '?' ID
SAIDA -> '!' EXP
EXP -> TERMO '+' EXP
     | TERMO '-' EXP
     | TERMO
TERMO -> FATOR '*' TERMO
       | FATOR '/' TERMO
       | FATOR
FATOR -> '(' EXP ')'
       | NUM
       | ID
'''


import ply.yacc as yacc

# Assuming you have a lexer with tokens defined,
# you need to import your tokens here
from lexer import tokens

# Define a function for each grammar rule. Each function receives a list of the elements
# (p) matched by the rule. The documentation string (docstring) at the beginning of each
# function describes the rule it implements.

def p_programa(p):
    "PROGRAMA : INSTRUCOES"
    p[0] = p[1]

def p_instrucoes_recursivo(p):
    "INSTRUCOES : INSTRUCAO INSTRUCOES"
    p[0] = [p[1]] + p[2]

def p_instrucoes_base(p):
    "INSTRUCOES : "
    p[0] = []

def p_instrucao(p):
    """
    INSTRUCAO : ATRIBUICAO
              | ENTRADA
              | SAIDA
    """
    p[0] = p[1]

def p_atribuicao(p):
    "ATRIBUICAO : ID EQUAL EXP"
    p[0] = ('ATRIBUICAO', p[1], p[3])

def p_entrada(p):
    "ENTRADA : INPUT ID"
    p[0] = ('ENTRADA', p[2])

def p_saida(p):
    "SAIDA : OUTPUT EXP"
    p[0] = ('SAIDA', p[2])

def p_exp_plus(p):
    "EXP : TERMO PLUS EXP"
    p[0] = ('+', p[1], p[3])

def p_exp_minus(p):
    "EXP : TERMO MINUS EXP"
    p[0] = ('-', p[1], p[3])

def p_exp_termo(p):
    "EXP : TERMO"
    p[0] = p[1]

def p_termo_mult(p):
    "TERMO : FATOR MULT TERMO"
    p[0] = ('*', p[1], p[3])

def p_termo_div(p):
    "TERMO : FATOR DIV TERMO"
    p[0] = ('/', p[1], p[3])

def p_termo_fator(p):
    "TERMO : FATOR"
    p[0] = p[1]

def p_fator_exp(p):
    "FATOR : LPAREN EXP RPAREN"
    p[0] = p[2]

def p_fator_num(p):
    "FATOR : NUM"
    p[0] = ('NUM', p[1])

def p_fator_id(p):
    "FATOR : ID"
    p[0] = ('ID', p[1])

# Error rule for syntax errors
def p_error(p):
    parser.success = True
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


def parse_input(input_data):
    print("Starting Parser!")
    parser = yacc.yacc()
    parser.success = True
    result = parser.parse(input_data)
    #print(result)
    if parser.success:
       print('Parsing completed!')
    else:
       print('Parsing failed!')

    # Optionally, return result if you want to use it further

# Example input
input_data = '''
?x
y=x*2/(27-3)+5
!y*(x+3)
'''

parse_input(input_data)


