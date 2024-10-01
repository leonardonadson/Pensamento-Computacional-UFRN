def segundoMaior(valores):

  valoresInseridos = list(valores)
  valoresUnicos = list(set(valores))

  if len(valoresInseridos) != len(valoresUnicos) and len(valoresUnicos) < 2:
      return "Não é possível determinar o segundo maior valor com menos de dois valores distintos."

  if len(valoresUnicos) < 2:
    return "Não é possível determinar o segundo maior valor com menos de dois elementos."

  valoresOrdenados = sorted(valoresUnicos)

  return valoresOrdenados[-2]

entrada = input()

valores = [float(valor) for valor in entrada.split(",")]

n2 = segundoMaior(valores)

print(n2)