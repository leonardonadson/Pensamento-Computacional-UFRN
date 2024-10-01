def conta_palavras(texto):
  texto = texto.strip() 
  palavras = texto.split()
  contagem = {}
  for p in palavras:
    if p not in contagem:
      contagem[p] = 0
    contagem[p] += 1
  return contagem

texto = input("")
contagem = conta_palavras(texto)

for palavra, quantidade in contagem.items():
  print(f"{quantidade}: {palavra}")