def flatten_lista(itens_aninhados):
  """
  Função para criar uma lista plana a partir de uma lista aninhada.

  Args:
    itens_aninhados: Uma lista com várias dimensões.

  Returns:
    Uma lista plana contendo todos os itens.
  """
  itens_planos = []
  for item in itens_aninhados:
    if isinstance(item, list):
      # Se o item é uma lista, chama recursivamente a função flatten_lista
      itens_planos.extend(flatten_lista(item))
    else:
      # Se o item não é uma lista, adiciona-o à lista plana
      itens_planos.append(item)
  return itens_planos

# Solicita ao usuário inserir a lista multidimensional
entrada = input("Digite a lista com várias dimensões: ")
itens_aninhados = eval(entrada)

# Chama a função flatten_lista para criar a lista plana
itens_planos = flatten_lista(itens_aninhados)

# Imprime a lista plana
print("Lista plana:", itens_planos)