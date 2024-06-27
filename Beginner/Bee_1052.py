entrada = int(input())

def calcula_mes(entrada):
    if entrada == 1:
        return "January"
    elif entrada == 2:
        return "February"
    elif entrada == 3:
        return "March"
    elif entrada == 4:
        return "April"
    elif entrada == 5:
        return "May"
    elif entrada == 6:
        return "June"
    elif entrada == 7:
        return "July"
    elif entrada == 8:
        return "August"
    elif entrada == 9:
        return "September"
    elif entrada == 10:
        return "October"
    elif entrada == 11:
        return "November"
    else:
        return "December"

resultado = calcula_mes(entrada)

print(resultado)
