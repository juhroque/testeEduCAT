def reescreveString(string):
    vogais = 'aeiou'
    novaString = ''
    for letra in string:
        if letra in vogais:
            novaString += '-'
        else:
            novaString += letra.upper()
    return novaString

# Teste

string = 'Hello World'
novaString = reescreveString(string)
print(novaString)