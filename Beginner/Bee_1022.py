numerador, denominador = map(int, input().split())

def mdc(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

result = mdc(numerador, denominador)

def formata(numerador, denominador, result):
    if denominador == 0:
        return 0
    else:
        return (f"{numerador}/{denominador} = {(numerador/result):.0f}/{(denominador/result):.0f}")
    
formatado = formata(numerador, denominador, result)

print(formatado)

