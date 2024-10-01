def ordenar_fila(casos): #função recebe uma lista de casos de teste
  r = [] #lista que armazena resultado de cada caso

  for caso in casos: #para cada caso extrai o número de alunos e lista de notas
      m = caso[0] #número de alunos
      notas = caso[1:] #lista de notas

      notas_ordenadas = sorted(notas, reverse=True) #ordena em ordem decrescente
      nao_trocados = sum(1 for i in range(m) if notas[i] == notas_ordenadas[i]) #soma 1 para cada aluno que nao precisa de troca - o for percorre cada item da lista notas e compara com a lista ordenada, se a nota nas posições i forem iguais soma 1
      r.append(nao_trocados) #adiciona o número de alunos que nao precisam trocar de lugar 

  return r #retorna o resultado

n = int(input()) #número de casos de teste
casos = [] #lista vazia para armazenamento

for i in range(n): #lê os dados para cada caso
  m = int(input()) #número de alunos
  notas = list(map(int, input().split())) #lista de notas
  casos.append([m] + notas) #adiciona o número de alunos e a lista de notas à lista de casos

r = ordenar_fila(casos) #chama a função e armazena o resultado

for resultado in r:
  print(resultado) #imprime o resultado para cada caso