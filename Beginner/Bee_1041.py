X, Y = map(float, input().split())

def coordenadas_(X, Y):
    if X == 0 and Y == 0:
        return "Origem"
    elif X == 0:
        return "Eixo Y"
    elif Y == 0:
        return "Eixo X"
    elif X > 0 and Y > 0:
        return "Q1"
    elif X < 0 and Y > 0:
        return "Q2"
    elif X < 0 and Y < 0:
        return "Q3"
    elif X > 0 and Y < 0:
        return "Q4"

# Processamento:
resultado = coordenadas_(X, Y)

# Saída:
print(resultado)
