import ply.lex as lex

# Token names that the lexer produces and the parser expects
tokens = (
    'NUM',    # Numerical literals
    'ID',     # Identifiers (variable names)
    'PLUS', 'MINUS', 'MULT', 'DIV',
    'INPUT', 'OUTPUT', 'EQUAL',
    'LPAREN', 'RPAREN',  # Parentheses
)

# Regular expression rules for simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_MULT   = r'\*'
t_DIV    = r'/'
t_INPUT  = r'\?'
t_OUTPUT = r'!'
t_EQUAL  = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A string containing ignored characters (spaces, tabs, newlines)
t_ignore = ' \t\n'

# Regular expression rule with some action code for numbers
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # Convert string to a number
    return t

# Regular expression rule for identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Testing function for the lexer
def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break  # No more input
        print(tok)

# Example usage
if __name__ == "__main__":
    data = '''
    ?a
    b=a*2/(27-3)+5
    !b*(a+3)
    '''
    test_lexer(data)
