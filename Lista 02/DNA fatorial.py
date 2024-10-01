n = int(input())

fatorial = 1

if n > 0:
  for i in range(n, 1, -1):
    fatorial = fatorial * i  
  print("Resultado do fatorial:", fatorial)
else:
  print("O número deve ser maior que 0.")