medidas = input()

aux = medidas.split(' ')

a = float(aux[0])
b = float(aux[1])
c = float(aux[2])

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

if a >= b + c:
  print("NAO FORMA TRIANGULO")
else:
  if a ** 2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
  if a ** 2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
  if a ** 2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
  if a == b and a == c:
    print("TRIANGULO EQUILATERO")
  if not(a == b and a == c) and (a == b or a == c or b == c):
    print("TRIANGULO ISOSCELES")
  
