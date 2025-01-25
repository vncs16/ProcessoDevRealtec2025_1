#Bibliotecas
import time

#Variáveis
taxa_resfriamento = 0.8
taxa_aquecimento = 1.5
atraso_efeito = 5
temperatura_inicial = 10
faixa_temperatura = [0, 15]
tempo = 0

#Funções

def calcularImpacto(atraso, ideal):
    impacto = ((atraso-ideal)/ideal)*100
    print(f"O tempo com o atraso do motor foi: {atraso:.2f}, O tempo sem o atraso do motor foi: {ideal:.2f}")
    print(f"O impacto do atraso foi de {impacto:.2f}% a mais no tempo")
    

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
            if tempo > atraso_efeito:
                temperatura -= taxa_resfriamento
        elif tipo == 2:
            temperatura -= taxa_resfriamento
        elif tipo == 3:
            if tempo > atraso_efeito:
                temperatura += taxa_aquecimento
        elif tipo == 4:
            temperatura += taxa_aquecimento
    return comportamento

def ExibirHistoricoTemperaturas(historicoAtraso, historicoIdeal):
    print("Historico do motor com atraso")
    for chave, valor in comportamentoSimuladoResfriamento.items():
        print(f"{chave}: {valor:.2f}")

    print("\nHistorico do motor sem atraso")
    for chave, valor in comportamentoIdealResfriamento.items():
        print(f"{chave}: {valor:.2f}")

#Main

#//Simulação linear//
#/Resfriamento/
comportamentoSimuladoResfriamento = simulaCenario(faixa_temperatura, temperatura_inicial, 1)
comportamentoIdealResfriamento = simulaCenario(faixa_temperatura, temperatura_inicial, 2)

#/Aquecimento/
comportamentoSimuladoAquecimento = simulaCenario(faixa_temperatura, temperatura_inicial, 3)
comportamentoIdealAquecimento = simulaCenario(faixa_temperatura, temperatura_inicial, 4)

tempoFinalAtrasoResfriamento = next(reversed(comportamentoSimuladoResfriamento.keys()))
tempoFinalIdealResfriamento = next(reversed(comportamentoIdealResfriamento.keys()))
tempoFinalAtrasoAquecimento = next(reversed(comportamentoSimuladoAquecimento.keys()))
tempoFinalIdealAquecimento = next(reversed(comportamentoIdealAquecimento.keys()))

#/Log refriamento/
#ExibirHistoricoTemperaturas(comportamentoSimuladoResfriamento, comportamentoIdealResfriamento)
#calcularImpacto(tempoFinalAtrasoResfriamento, tempoFinalIdealResfriamento)

#Log aquecimento
ExibirHistoricoTemperaturas(comportamentoSimuladoAquecimento, comportamentoIdealAquecimento)
calcularImpacto(tempoFinalAtrasoAquecimento, tempoFinalIdealAquecimento)