n = int(input())

vetor = []
aux = ""

while n != 1:
  vetor.append(n)
  if n % 2 == 0:
    n = int(n / 2)
  else:
    n = (n*3) + 1
    
for i in range(len(vetor)):
  aux += str(vetor[i]) + "->"

print(aux + "1")
