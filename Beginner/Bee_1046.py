x, y = map(int, input().split())

def calcular_tempo_game(x, y):
    if x < y:
        return (f"O JOGO DUROU {y - x} HORA(S)")
    elif x == y:
        return (f"O JOGO DUROU 24 HORA(S)")
    else:
        return (f"O JOGO DUROU {(24 - x) + y} HORA(S)")
     

resultado = calcular_tempo_game(x, y)

print(resultado)
    
    