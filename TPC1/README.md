# TPC1: Análise de um dataset de exames médicos

## 2024-02-05

## Autor
- A96357
- Luís Tiago Pereira Borges

## Resumo
    
Neste trabalho, utiliza-se um dataset fornecido pelo docente relativo a exames médicos com os seguintes objetivos:
* Gerar uma lista das modalidades desportivas, ordenada alfabiteciamente.
* Descobrir a percentagem de atletas aptos e inaptos para a prática desportiva
* Distribuír os atletas por escalão etário, com intervalos de 5 anos ([30-34], [35-39], ...)

## Desenvolvimento
No que toca à lista de modalidades, analizou-se cada linha do ficheiro e adiconou-se a modalidade à lista, no caso de esta não estar já presente.
Quanto à percentagem de atletas, o processo passou apenas por incrementar a variável 'aptos' em 1 cada vez que era encontrado um atleta apto, e incrementar a variável 'total' a cada linha. Por fim, dividiu-se a primeira variável pela segunda.
Para o segmento da distribuição etária, foram criados 2 dicionários. Um deles guarda o número de atletas em cada escalão e o outro guarda uma lista com o nome desses atletas. Para cada linha lida, ambos os dicionários são atualizados, usando uma função prórpia para obter o escalão a partir da idade.



