#exerciocio83
expressao = str(input('Digite uma expressão: '))
parenteses1 = []
parenteses2 = []
lista = []
#para cada simbolo na expressao (pq vou usar apenas os parenteses)
#simples se a soma das duas listas for = 0 quer dizer que a mesma quantidade de parentes que abre, fecham tmb entt é valida
#se não ela não é valida. Vou tentar assim.
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print ('Sua expressão é valida!!!')
else:
    print ('Sua expressão não é valida :(')
