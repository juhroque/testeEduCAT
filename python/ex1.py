def retornaPares(lista):
    listaPares = []
    for numero in lista:
        if numero % 2 == 0:
            listaPares.append(numero)
    return listaPares

#Teste:

lista = [1,2,3,4,5,6,7,8,9,10]
print(retornaPares(lista))
