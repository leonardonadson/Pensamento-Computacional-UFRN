coordenadasRetangulo = input()
parOrdenado = input()
aux = coordenadasRetangulo.split()
x1 = aux[0]
y1 = aux[1]
x2 = aux[2]
y2 = aux[3]

aux2 = parOrdenado.split()
px = aux2[0]
py = aux2[1]

if (x1 <= px <= x2) and (y1 <= py <= y2):
  print ("Dentro!")
else:
  print ("Fora!")