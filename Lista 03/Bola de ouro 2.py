import math

qtdAmigos = int(input())

valor = []
jogador = []
apostadoresVencedores = []
valorAposta = 0

for i in range(qtdAmigos):
  aposta = input()
  aposta = aposta.split()
  valor.append(int(aposta[0]))
  jogador.append(int(aposta[1]))

vencedor = int(input())

valorRepassado = 0.9 * sum(valor)

for j in range(qtdAmigos):
  if jogador[j] == vencedor:
    apostadoresVencedores.append(j)

for k in range(len(apostadoresVencedores)):
  valorAposta += valor[apostadoresVencedores[k]]

if valorAposta != 0:
  print("Total: R$ %.0f" % sum(valor))
  Constante = valorRepassado / valorAposta
  for l in range(len(apostadoresVencedores)):
    print("Apostador %d: R$ %.0f" % ((apostadoresVencedores[l]+1), Constante * valor[apostadoresVencedores[l]]))

else:
  for z in range(qtdAmigos):
    print("Apostador %d: R$ %.0f" % ((z+1), math.floor(valor[z] * 0.9)))
print("Bebidas e petiscos: R$ %.0f" % math.ceil(sum(valor) - valorRepassado))