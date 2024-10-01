def fuso(horaPartida, tempo, diferenca):
    horaChegada = horaPartida + tempo + diferenca
    if horaChegada >= 24:
        horaChegada -= 24
    elif horaChegada < 0:
        horaChegada += 24
    return horaChegada

horaPartida = int(input())
tempo = int(input())
diferenca = int(input())
print("Hora de saída: %d" % horaPartida)
print("Hora de chegada: %d" % fuso(horaPartida, tempo, diferenca))