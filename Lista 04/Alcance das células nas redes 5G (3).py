def get_range(n, cells, distance, user):
  start, end = -1, -1
  count = 0

  for i in range(n):
    if abs(cells[i] - user) <= distance:
      count += 1
      if start == -1:
        start = i
      end = i

  return count, start, end

cells = []
entradas = list(map(int, input().split()))

n, d, u = entradas[0], entradas[1], entradas[2]

for i in range(n):
  numero = int(input())
  cells.append(numero)

count, start, end = get_range(n, cells, d, u)
saida = []
if count > 0:
  for i in range(start, end + 1):
    saida.append(cells[i])
  print(*saida)
else:
  print("USUARIO DESCONECTADO")