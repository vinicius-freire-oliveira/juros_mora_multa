def calcular_conta_atrasada(valor_original, dias_atraso, taxa_juros_mora, taxa_multa):
    # Convertendo dias de atraso para meses
    meses_atraso = dias_atraso / 30
    print(meses_atraso)
    # Calculando juros de mora
    juros = valor_original * (taxa_juros_mora / 100) * meses_atraso
    print(juros)
    # Calculando multa por atraso
    multa = valor_original * (taxa_multa / 100)
    print(multa)
    # Somando juros e multa ao valor original
    valor_total = valor_original + juros + multa
    print(valor_total)
    return valor_total

# Valor original da conta em atraso
valor_original = 300.00

# Solicitando o número de dias de atraso do usuário
dias_atraso = int(input("Informe o número de dias de atraso: "))

# Taxa de juros de mora por mês (em porcentagem)
taxa_juros_mora = 1.00  # 1% ao mês

# Taxa de multa por atraso (em porcentagem)
taxa_multa = 2.00  # 2%

# Calculando o valor total da conta em atraso
valor_total_atrasado = calcular_conta_atrasada(valor_original, dias_atraso, taxa_juros_mora, taxa_multa)

print("O valor total da conta em atraso é: R$%.2f" % valor_total_atrasado)
