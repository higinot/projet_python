string1 = "Eduardo e Monica!"
string2 = "Monica"

# Usando o operador "in"
if string2 in string1:
    print("A string '{}' contém a string '{}'".format(string1, string2))

# Usando o método __contains__
if string1.__contains__(string2):
    print("A string '{}' contém a string '{}'".format(string1, string2))

tipo_verificacao_in = string2 in string1
tipo_verificacao_contains = string1.__contains__(string2)

print(tipo_verificacao_contains)
print(tipo_verificacao_in)