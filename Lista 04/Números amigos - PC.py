n1, n2 = map(int, input().split())


def divisores(number):
  divisores = []
  for i in range(1, number + 1):
    if number % i == 0:
      divisores.append(i)
  return divisores

def somarDivisores(divisores):
  soma = 0
  for i in divisores:
    if divisores.index(i) == len(divisores) -1: 
        break
    soma += i
  return soma

d1 = divisores(n1)
d2 = divisores(n2)
s1 = somarDivisores(d1)
s2 = somarDivisores(d2)

if s1 == n2 and s2 == n1:
  print("S")
else:
  print("N")
