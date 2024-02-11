import sys

sys.stdin.reconfigure(encoding='utf-8') # definir encoding do stdin (no meu pc não usa utf-8 por default)

modalidades = [] # lista de modalidades
aptos = 0 # total de atletas aptos
total = 0 # total de atletas
idades = {} # dicionário de faixas etárias
idades_nomes = {} # dicionário com a lista dos nomes para cada faixa etária

def getEscalao(n): # Obtém o escalão correspondente a cada idade
    if n%10 > 4:
        return f"{n//10 * 10 + 5}-{n//10 * 10 + 9}"
    else:
        return f"{n//10 * 10}-{n//10 * 10 + 4}"
    
file = sys.stdin # abrir o ficheiro
next(file) # ignorar a primeira linha
for linha in file:
    info = linha.split(',')
    # tratar da modalidade
    if(info[8]) not in modalidades:
        modalidades.append(info[8])
    # tratar da aptidão
    if info[12] == "true\n":
        aptos += 1
    total += 1
    # tratar do escalão
    escalao = getEscalao(int(info[5]))
    if escalao in idades.keys(): 
        idades[escalao] = idades[escalao] + 1
        idades_nomes[escalao].append(info[3] + " " + info[4])
    else:
        idades[escalao] = 1
        idades_nomes[escalao] = [info[3] + " " + info[4]]
file.close()

# organizar e printar a informação
modalidades.sort()
print("----- Modalidades -----")
print(modalidades)

pct_aptos = aptos/total * 100
inaptos = total - aptos
pct_inaptos = 100-pct_aptos
print("\n----- Aptos e Inaptos -----")
print(f"Aptos: {aptos} ({pct_aptos}%)")
print(f"Inaptos: {inaptos} ({pct_inaptos}%)")

print("\n----- Distribuição etária -----")
print(dict(sorted(idades.items())))
print(dict(sorted(idades_nomes.items())))

# gerar um ficheiro com a informação
file_res = open('res.txt', 'w+')
file_res.write(f"Modalidades: {modalidades}\n")
file_res.write(f"Aptos: {aptos} ({pct_aptos}%)\nInaptos: {inaptos} ({pct_inaptos}%)\n")
file_res.write(f"Distribuição de escalões: {dict(sorted(idades.items()))}\n") 
file_res.write(f"Distribuição de escalões por nomes: {dict(sorted(idades_nomes.items()))}") 

print("\nfile res.txt created")



