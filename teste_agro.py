#Bibliotecas
import time

#Variáveis
temperatura = 0
motor = False

#Main

while temperatura >= 0 and temperatura <= 15:
    if motor == True:
        temperatura -= 0.8
    else:
        temperatura += 1.5
    print(temperatura)
    time.sleep(1)
