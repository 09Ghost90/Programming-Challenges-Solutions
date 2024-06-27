# Produto 1:
cod, qtd, valor = map(float, input().split())
# Produto 2:
cod2, qtd2, valor2 = map(float, input().split())

# Operação:
def calcula_compra(qtd, valor, qtd2, valor2):
    return (qtd * valor) + (qtd2 * valor2)

resultado_produto = calcula_compra(qtd, valor, qtd2, valor2)

print(f"VALOR A PAGAR: R$ {resultado_produto:.2f}")


