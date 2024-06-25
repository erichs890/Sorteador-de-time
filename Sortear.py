import random

jogadores = []
lanes = ["Top", "Jg", "Mid", "Adc", "Sup"]

for i in range(10):
    jogador = input(f"Diz o nome do jogador {i+1}: \n")
    jogadores.append(jogador)

random.shuffle(jogadores)

lanesTime1 = lanes[:]
lanesTime2 = lanes[:]
Time1 = {lane: jogador for lane, jogador in zip(lanesTime1, jogadores[:5])}
Time2 = {lane: jogador for lane, jogador in zip(lanesTime2, jogadores[5:])}

print("\nTime 1:")
for lane in lanes:
    print(f"{lane}: {Time1[lane]}")

print("\nTime 2:")
for lane in lanes:
    print(f"{lane}: {Time2[lane]}")