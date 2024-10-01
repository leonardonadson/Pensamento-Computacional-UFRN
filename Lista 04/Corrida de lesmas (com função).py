def nivelLesma(number):
  if number < 10:
    return 1
  elif number >= 10 and number < 20:
    return 2
  else:
    return 3

n = int(input())
vetor = []

for i in range(n):
  number = int(input())
  level = nivelLesma(number)
  vetor.append(level)

n2 = max(vetor)

if n2 == 1:
  print("Level 1")
elif n2 == 2:
  print("Level 2")
else:
  print("Level 3")