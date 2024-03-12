import ply.lex as lex

saldo = 0

def prog():

    items = [
        {
        "id": "123",
        "nome": "agua",
        "preco": "30c"
        },
        {
        "id": "456",
        "nome": "sumo",
        "preco": "90c"
        }
    ]

    tokens = (
    'LISTAR',
    'MOEDA_E',
    'MOEDA_C',
    'SELECIONAR',
    'SAIR'
    )

    def t_LISTAR(t):
        r'LISTAR'
        for item in items:
            print(item["id"] + " | " + item["nome"] + ": " + item["preco"])

    def t_MOEDA_E(t):
        r'MOEDA\s+[12]e'
        global saldo
        saldo += (int(t.value.split()[1][:-1]))*100  
        print("SALDO: " + str(saldo) + " c")
        return t

    def t_MOEDA_C(t):
        r'MOEDA\s+\d+c'
        global saldo
        saldo += int(t.value.split()[1][:-1])    
        print("SALDO: " + str(saldo) + " c")
        return t

    def t_SELECIONAR(t):
        r'SELECIONAR\s\d+'
        id = t.value.split()[1]
        print(id)
        global saldo
        for item in items:
            if item["id"] == id:
                saldo -= int((item["preco"])[:-1])  
                print(item["preco"])
                break # BANIDO DE PL
        print("SALDO: " + str(saldo) + " c")
        return t
    
    def t_SAIR(t):
        r'SAIR'
        print("TROCO: " + str(saldo))
        return t

    t_ignore  = ' \t'

    def t_error(t):
        print("erro")
        #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex()

    running = True  
    while running:
        data = input()
        lexer.input(data)
        while tok := lexer.token():
            if tok.type == 'SAIR':
                running = False
            elif tok is None:
                return    

prog()

# Doesn't account for not enough balance, non-existent products, etc 