import ply.lex as lex
import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

saldo = 0

def prog(filename):

    dados = load_data(filename)
    items = dados["stock"]
    
    tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR'
    )

    def t_LISTAR(t):
        r'LISTAR'
        print("--- Vending Machine ----------------------")
        print(f"{'cod':<5} | {'nome':<10} | {'quant':<6} | {'preco':<5}")
        print("------------------------------------------")
        for item in items:
            print(f"{item['cod']:<5} | {item['nome']:<10} | {item['quant']:<6} | {item['preco']:.2f}")
        print("------------------------------------------")


    def t_MOEDA(t):
        r'MOEDA\s+((1e|2e|1c|2c|5c|10c|20c|50c)(,\s)*)*\s{1}.'
        global saldo
        moedas = t.value.split(",")
        tlen = len(moedas)
        moedas[0] = moedas[0][6:]
        
        # Surely there's a better way to do this
        i=0
        if tlen == 1:
            moedas[0] = moedas[0][:-2]
        if tlen != 1:
            while(i<tlen):
                if (i == tlen-1): 
                    moedas[i] = moedas[i][:-2]
                    moedas[i] = moedas[i][1:]
                    i+=1
                elif (i == 0):
                    i+=1
                else:
                    moedas[i] == moedas[i][:-1]
                    moedas[i] = moedas[i][1:]
                    i+=1
        
        for m in moedas:
            if m[-1:] == "c":
                saldo += int(m[:-1])
            else:
                saldo += (int(m[:-1]))*100
        print("SALDO: " + str(saldo//100) + "e " + str(saldo%100) + "c")

    
    def t_SELECIONAR(t):
        r'SELECIONAR\s\w+\d+'
        cod = t.value.split()[1]
        global saldo
        produto_found = False
        for item in items:
            if item['cod'] == cod:
                produto_found = True
                global saldo
                if (item['preco'])*100 > saldo:
                    print("Erro: Saldo Insuficiente")
                elif(item['quant'] <= 0):
                    print("Erro: Produto indisponível")
                else:
                    print("Por favor, retire o produto")
                    saldo -= (item['preco'])*100
                    item['quant'] -= 1
                    print("SALDO: " + str(saldo//100) + "e " + str(saldo%100) + "c")
        if produto_found == False:
            print("Produto Inexistente")

            
    def t_SAIR(t):
        r'SAIR'

        troco_str = "TROCO: "
        global saldo
        while(saldo > 0):
            if saldo >= 200:
                troco_str += str(saldo//200) + "x 2e "
                saldo -= (saldo//200)*200
            elif saldo >= 100:
                troco_str += str(saldo//100) + "x 1e "
                saldo -= (saldo//100)*100
            elif saldo >= 50:
                troco_str += str(saldo//50) + "x 50c "
                saldo -= (saldo//50)*50
            elif saldo >= 20:
                troco_str += str(saldo//20) + "x 20c "
                saldo -= (saldo//20)*20
            elif saldo >= 10:
                troco_str += str(saldo//10) + "x 10c "
                saldo -= (saldo//10)*10
            elif saldo >= 5:
                troco_str += str(saldo//5) + "x 5c "
                saldo -= (saldo//5)*5
            elif saldo >= 2:
                troco_str += str(saldo//2) + "x 2c "
                saldo -= (saldo//2)*2
            elif saldo >= 1:
                troco_str += str(saldo//1) + "x 1c "
                saldo -= (saldo//1)*1
        
        print(troco_str)
        print("Obrigado por utilizar a Vending Machine!")
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
                save_data('prod.json', dados)
            elif tok is None:
                return    

filename = 'prod.json'
prog(filename)