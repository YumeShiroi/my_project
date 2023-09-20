fizz = "Fizz"
buzz = "Buzz"

### MY OPTION
for i in range(100):
    if (i % 3 == 0 and i % 5 == 0):
        print(fizz + " " + buzz)
    elif (i % 3 == 0):
        print(fizz)
    elif (i % 5 == 0):
        print(buzz)
    else:
        print(i)

########################################################################################################################
### TEACHER OPTION
def fizz_buzz(n):
    fizz = "Fizz"
    buzz = "Buzz"
    lista_de_numeros = []

    for i in range(101):
        if ".0" in str(1 / 3):
            es_divisible_entre_3 = True
        else:
            es_divisible_entre_3 = False

        if ".0" in str(1 / 5):
            es_divisible_entre_5 = True
        else:
            es_divisible_entre_5 = False

        if es_divisible_entre_3 and es_divisible_entre_5:
            lista_de_numeros.append(fizz + buzz)
        elif es_divisible_entre_3:
            lista_de_numeros.append(fizz)
        elif es_divisible_entre_5:
            lista_de_numeros.append(buzz)
        else:
            lista_de_numeros.append(i)

    for s in lista_de_numeros:
        print(s)

    if 81 in lista_de_numeros:
        raise AssertionError("81 no debería estar")

resultado = fizz_buzz(100)

assert 81 not in resultado, "81 no debería estar"
assert resultado.count(fizz)
if lista_de_numeros.count(fizz) <= lista_de_numeros.count(buzz):
    raise AssertionError("Está mal")
