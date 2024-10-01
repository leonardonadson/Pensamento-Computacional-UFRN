n = int(input())

vetor = []

for i in range(1, n+1, 1):
  aux = 0
  atualizacoes = 1
  
  dados = input()
  dados = dados.split()

  x = int(dados[0])
  y = int(dados[1])

  
  while atualizacoes <= y:
    if x % 2 != 0:
      aux += x
      atualizacoes += 1
    x += 1
  vetor.append(str(aux))

for l in range(0, n, 1):
  print(vetor[l])