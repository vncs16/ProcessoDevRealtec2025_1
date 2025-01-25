#Bibliotecas
import math
import matplotlib
import matplotlib.pyplot as plt

#Variáveis
taxa_resfriamento = 0.8
taxa_aquecimento = 1.5
atraso_efeito = 5
temperatura_inicial = 10
faixa_temperatura = [0.01, 15]
tempo = 0
comportamentoSimulado = {}
comportamentoIdeal = {}
tempoFinalAtraso = 0
tempoFinalIdeal = 0
constanteTempo = 5
tempoTotal = 50

#Funções

def comportamento_exponencial(temperatura_inicial, temperatura_final, constanteTempo, tempo_total, modo):
    comportamento = {}
    for t in range(tempo_total + 1):
        if t < atraso_efeito:
            temperatura = temperatura_inicial
        else:
            if modo == "resfriar":
                temperatura = temperatura_final + (temperatura_inicial - temperatura_final) * math.exp(-((t - atraso_efeito) / constanteTempo))
            elif modo == "aquecer":
                temperatura = temperatura_final - (temperatura_final - temperatura_inicial) * math.exp(-((t - atraso_efeito) / constanteTempo))
        comportamento[t] = temperatura
    return comportamento

#main
#//Simulação exponencial//
temperaturasResfriamento = comportamento_exponencial(temperatura_inicial, faixa_temperatura[0], constanteTempo, tempoTotal, modo="resfriar")
for chave, valor in temperaturasResfriamento.items():
    print(f"{chave}, {valor:.2f}")

temperaturasAquecimento = comportamento_exponencial(faixa_temperatura[0], faixa_temperatura[1], constanteTempo, tempoTotal, modo="aquecer")
for chave, valor in temperaturasAquecimento.items():
    print(f"{chave}, {valor:.2f}")

#/Exibição/
tempo = list(range(tempoTotal + 1))
#trasformar os dicionarios em listas
valores_resfriamento = list(temperaturasResfriamento.values())
valores_aquecimento = list(temperaturasAquecimento.values())
#Grafico
plt.plot(tempo, valores_resfriamento, label="Resfriamento Exponencial")
plt.plot(tempo, valores_aquecimento, label="Aquecimento Exponencial")
plt.axhline(faixa_temperatura[0], color="red", linestyle="--", label="Limite Inferior (0°C)")
plt.axhline(faixa_temperatura[1], color="blue", linestyle="--", label="Limite Superior (15°C)")
plt.xlabel("Tempo (minutos)")
plt.ylabel("Temperatura (°C)")
plt.title("Comportamento Exponencial de Resfriamento e Aquecimento")
plt.legend()
plt.grid()
plt.show()