temperatura = input()

aux = temperatura.split(' ')

valor = aux[0]
escala = aux[1]

if escala == 'C':
  celsius = float(valor)
  fahrenheit = (celsius * 9/5) + 32
  kelvin = celsius + 273.15

elif escala == 'F':
  fahrenheit = float(valor)
  celsius = (fahrenheit - 32) * 5/9
  kelvin = (fahrenheit - 32) * 5/9 + 273.15

else:
  if escala == 'K':
    kelvin = float(valor)
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32

print("Temperatura em Celsius: %.2f °C" % celsius)
print("Temperatura em Fahrenheit: %.2f °F" % fahrenheit)
print("Temperatura em Kelvin: %.2f K" % kelvin)