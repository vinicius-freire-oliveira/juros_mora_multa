def valorPagamento(p, d):
    # Calcula o valor a ser pago, incluindo uma taxa de 2% sobre o valor da prestação e uma taxa de R$ 0,001 por dia de atraso
    return p * 1.02 + 0.01 * (p/30) * d

# Inicializa as variáveis c e t para contar a quantidade de prestações e o total pago
c = t = 0

# Loop que solicita continuamente a entrada do valor da prestação e do dia de atraso e calcula o valor a ser pago
while True:
    p = float(input('Valor da prestação: '))
    if p == 0:
        # Se o valor da prestação for 0, encerra o loop e imprime o total pago e a quantidade de prestações
        print(f'Total: {t:.2f}. Quantidade: {c} ')
        break
    d = int(input('Dia em atraso: '))
    # Calcula e imprime o valor a ser pago
    print(f'Valor a ser pago: {valorPagamento(p, d) :.2f}')
    print('-+-'*10)
    # Atualiza o contador de prestações e o total pago
    c += 1
    t += valorPagamento(p, d)
