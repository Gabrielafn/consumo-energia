# Calculadora de consumo de energia elétrica
# Autor: Gabriela

# Dados de entrada
aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência do aparelho em Watts: "))
horas_dia = float(input("Tempo médio de uso por dia (horas): "))

# Valor médio do kWh
valor_kwh = 0.75 

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_mensal = consumo_mensal * valor_kwh

# Saída
print("      RESULTADO      ")
print(f"Aparelho:         {aparelho}")
print(f"Consumo mensal:   {consumo_mensal:.2f} kWh")
print(f"Custo mensal:     R$ {custo_mensal:.2f}")
