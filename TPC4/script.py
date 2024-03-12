import ply.lex as lex

def ex1():
    tokens = (
    'NUM',
    'RW',  # reserved word
    'VAR',
    'MATH_SIGN',
    'COMMA'
    )

    t_NUM = r'\d+'
    t_RW = r'(Select|from|where)'
    t_VAR = r'\w+'
    t_MATH_SIGN = r'((>=*)|(<=*)|=)'
    t_COMMA = r','
    t_ignore = ' \t\n'
    def t_error(t):
        print(f"Illegal char {t.value[0]}")
        t.lexer.skip(1)

    lexer = lex.lex()

    data = '''Select id, noun, salario 
    from empregados 
        where salario >= 820
'''
    lexer.input(data)
    while tok := lexer.token():
        print(tok)

ex1()

