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

def simulaCenario(faixa, temperatura, tipo):
    #Tipo 1 = Com atraso e ligado
    #Tipo 2 = Sem atraso e ligado
    #Tipo 3 = Com atraso e desligado
    #Tipo 4 = Sem atraso e desligado
    tempo = 0
    comportamento = {}
    while faixa[0] <= temperatura <= faixa[1]:
        tempo += 1
        comportamento[tempo] = temperatura
        if tipo == 1:
            if tempo > 5:
                temperatura -= taxa_resfriamento
        elif tipo == 2:
            temperatura -= taxa_resfriamento
        elif tipo == 3:
            if tempo > 5:
                temperatura += taxa_aquecimento
        elif tipo == 4:
            temperatura += taxa_aquecimento
    return comportamento

#Main

#comportamentoSimulado = simulaCenario(faixa_temperatura, temperatura_inicial, 1)
#comportamentoIdeal = simulaCenario(faixa_temperatura, temperatura_inicial, 2)
comportamentoSimulado = simulaCenario(faixa_temperatura, temperatura_inicial, 3)
comportamentoIdeal = simulaCenario(faixa_temperatura, temperatura_inicial, 4)

print("Historico do motor com atraso")
for chave, valor in comportamentoSimulado.items():
    print(f"{chave}: {valor:.2f}")

print("\nHistorico do motor sem atraso")
for chave, valor in comportamentoIdeal.items():
    print(f"{chave}: {valor:.2f}")

tempoFinalAtraso = next(reversed(comportamentoSimulado.keys()))
tempoFinalIdeal = next(reversed(comportamentoIdeal.keys()))

impacto = calcularImpacto(tempoFinalAtraso, tempoFinalIdeal)

print(f"{tempoFinalAtraso:.2f}, {tempoFinalIdeal:.2f}")
print(f"O impacto do atraso foi de {impacto:.2f}% a mais no tempo")