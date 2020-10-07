# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=========== PROGRESSÃO ARITMÉTICA ===========')
primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão dessa PA: '))
termo = 0
n = 1
while n < 11:
    termo = primeiro + (n - 1) * r #Fórmula Geral da PA
    n += 1
    print(termo, end=' ')