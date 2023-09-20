def frase_palindromo(frase):

    frase = limpiar_frase(frase)
    inicio = 0
    fin = len(frase) - 1

    while frase[inicio] == frase[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1

    return False

def limpiar_frase(frase):

    frase = frase.lower()
    frase = frase.replace(" ", "")

    return frase

frase = input("Introduzca una frase: ")
frase_invertida = frase[::-1]

if frase_palindromo(frase):
    print("La frase introducida es palíndrom")
else:
    print("La frase introducida NO es palíndromo")

print("Frase introducida: " + frase)
print("Frase invertida: " + frase_invertida)