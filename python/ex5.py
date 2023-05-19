def isPrimo(numero):
    divisores = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            divisores += 1
    if divisores == 2:
        return True
    return False

def primosDe0a2000():
    for c in range(0, 2001):
        if(isPrimo(c)):
            print(c, end=' ')

# Teste

print(isPrimo(23))
primosDe0a2000()