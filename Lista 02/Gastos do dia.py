maiorNumero = 0
while True:
  n = float(input())
  if n == 0:
    if maiorNumero == 0:
      print("Você não teve gastos hoje!")
    else:
      print("O seu maior gasto hoje foi R$ %.2f" % maiorNumero)
    break
  elif n >= maiorNumero:
    maiorNumero = n
