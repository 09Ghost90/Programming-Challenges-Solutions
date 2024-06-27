while True:
    N = input()
    N = int(N)
    if N == 0:
        break
    
    largada = list(map(int, input().split()))
    chegada = list(map(int, input().split()))
    
    ultrapassagens = 0
    
    # Vamos comparar cada competidor na largada com sua posição na chegada
    for i in range(N):
        posicao_na_largada = largada[i]
        posicao_na_chegada = chegada.index(posicao_na_largada)
        
        # Contar quantos competidores na largada estão à frente na chegada
        for j in range(i + 1, N):
            if chegada.index(largada[j]) < posicao_na_chegada:
                ultrapassagens += 1
    
    print(ultrapassagens)
