def retornaMaisCaro(lista):
    maisCaro = lista[0]
    for produto in lista:
        if produto['preco'] > maisCaro['preco']:
            maisCaro = produto
    return maisCaro

#Teste

produto1 = {'nome': 'Lápis Faber Castell', 'preco': 49.99}
produto2 = {'nome': 'Marca texto Stabillo', 'preco': 39.99}
produto3 = {'nome': 'Caderno Inteligente', 'preco': 110}

lista = [produto1, produto2, produto3]
print(retornaMaisCaro(lista))