while True:
  n = int(input())
  if n == 0:
    break

  matriz = []

  for i in range(n):
    linha = []
    for j in range(n):
      valor = 1 + abs(i - j)
      linha.append(str(valor))
    matriz.append(" ".join(linha))

  for linha in matriz:
    print(linha)  

  print() 