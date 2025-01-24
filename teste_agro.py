#Bibliotecas
import time

#Variáveis
taxa_resfriamento = 0.8
taxa_aquecimento = 1.5
atraso_efeito = 5
temperatura_inicial = 10
faixa_temperatura = [0, 15]
tempo = 0
comportamentoSimulado = {}
comportamentoIdeal = {}
tempoFinalAtraso = 0
tempoFinalIdeal = 0

#Funções

def calcularImpacto(atraso, ideal):
    impacto = ((atraso-ideal)/ideal)*100
    return impacto

#Main

while faixa_temperatura[0] <= temperatura_inicial <= faixa_temperatura[1]:
    tempo += 1
    comportamentoSimulado[tempo] = temperatura_inicial
    if tempo > 5:
        temperatura_inicial -= taxa_resfriamento
    

print(f"O tempo foi: {tempo} minutos com o motor ligado até atingir 0°C com o atraso")

temperatura_inicial = 10
tempo = 0

while faixa_temperatura[0] <= temperatura_inicial <= faixa_temperatura[1]:
    tempo += 1
    comportamentoIdeal[tempo] = temperatura_inicial
    temperatura_inicial -= taxa_resfriamento

for chave, valor in comportamentoSimulado.items():
    print(f"{chave}: {valor:.2f}")

print(f"\nO tempo foi: {tempo} minutos com o motor ligado até atingir 0°C sem o atraso")

for chave, valor in comportamentoIdeal.items():
    print(f"{chave}: {valor:.2f}")

tempoFinalAtraso = next(reversed(comportamentoSimulado.keys()))
tempoFinalIdeal = next(reversed(comportamentoIdeal.keys()))

impacto = calcularImpacto(tempoFinalAtraso, tempoFinalIdeal)

print(f"{tempoFinalAtraso:.2f}, {tempoFinalIdeal:.2f}")
print(f"O impacto do atraso foi de {impacto:.2f}% a mais no tempo")