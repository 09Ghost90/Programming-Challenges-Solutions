# Primeira Linha deve conter a quantidade de casos de testes que serão lidos. 
# Segunda Linha deve ser a mensagem codificada.
# Terceira Linha deve ser a quantidade de casas usadas para codificar a mesma.

def cifra_cesar(criptografado, used):
    decodificado = ""
    criptografado = criptografado.upper()
    for i in criptografado:
        ord(i) - used
        if ord(i) - used < 65:
            decodificado += chr(ord(i) - used + 26)
        else:
            decodificado += chr(ord(i) - used)
    print(decodificado)

n = True
t = int(input())

while n is not False:
    criptografado = input()
    used = int(input())
    if t == 0 or criptografado == "":
        break

    cifra_cesar(criptografado, used)

    if n < t:
        n += 1
    else:
        n = False

