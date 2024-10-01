n = int(input())

for j in range(1, n+1, 1):
  dados = input()

  dados = dados.split()
  PA = int(dados[0])
  PB = int(dados[1])
  G1 = float(dados[2])
  G2 = float(dados[3])

  anos = 0
  while PA <= PB and anos <= 100:
    PA = int(PA * (1 + G1 / 100))  # Calcula a nova população de A
    PB = int(PB * (1 + G2 / 100))  # Calcula a nova população de B
    anos += 1

  if anos > 100:
    print("Mais de 1 seculo")
  else:
    print(f"{anos} anos.")