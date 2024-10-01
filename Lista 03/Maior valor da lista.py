dados = input()

lista = []
dados = dados.split(", ") 

tamanho = len(dados)
for i in range(tamanho):
  lista.append(float(dados[i]))

maiorValor = max(lista)
print(maiorValor)