valor = float(input())
opcao = input()

if opcao == "V":
  valorAvista = valor * 0.95
  print("Valor à pagar: %.0f" % valorAvista)

elif opcao == "P":
  valorParcelado = valor * 1.08
  valorParcela = valorParcelado / 3
  print("Valor à pagar: %.0f" % valorParcelado)
  print("Parcela 1: %.0f" % valorParcela)
  print("Parcela 2: %.0f" % valorParcela)
  print("Parcela 3: %.0f" % valorParcela)