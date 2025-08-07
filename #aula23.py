#aula23
#tratamento de erro e exceções
#erro semantico
#print(x)
#está errado pq eu não declarei a variavel x
#isso é exceção
#mesma coisa se colocar int(input) e digitar oito ao invés de 8 
#comandos try e except
#tente
#exemplo
try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    x = a / b

#exeção
except Exception as erro: 
    print(f'Infelizmente tivemos um b.o :( O erro foi: {erro}')

except (ValueError, TypeError):
    print('Tivemos um erro ao interpretar os valores adicionados')

#se não der problema...    
#se eu não colocar o else ele me mostrar qual foi o erro
else:
    print(f'O resultado é: {x}')

#sempre vai acontecer
finally:
    print('Volte sempre! Muito obg! ')

#isso server para testar os erros. 

#else e finally são opicionais. 
#posso usar except Exception as erro: 
#para mostrar qual foi o erro
#posso colocar exceps quanto eu quiser para detectar erros especificos