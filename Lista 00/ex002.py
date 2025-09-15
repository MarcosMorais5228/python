x = int(input())
z = int(input())

hogsmeade_x = 34
hogsmeade_z = 220

kakariko_x = 0
kakariko_z = 0

solitude_x = 140
solitude_z = 456

distancia_hogsmeade = float((x - hogsmeade_x)**2 + (z - hogsmeade_z)**2)**0.5
distancia_kakariko = float((x - kakariko_x)**2 + (z - kakariko_z)**2)**0.5
distancia_solitude = float((x - solitude_x)**2 + (z - solitude_z)**2)**0.5

print(f'Distancia para Hogsmeade: {distancia_hogsmeade:0.2f}')
print(f'Distancia para Kakariko: {distancia_kakariko:0.2f}')
print(f'Distancia para Solitude: {distancia_solitude:0.2f}')