def retornaDicionario(lista):
    contador = {}
    for palavra in lista:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return contador

# Teste

lista =  ["apple", "banana", "apple", "orange"]
dicionario = retornaDicionario(lista)
print(dicionario)