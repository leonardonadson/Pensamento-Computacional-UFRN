def parteEmail(email):
  email = email.split('@')
  email = email[1]
  email = email.split('.')
  return email[0]


vetor = []
while True:
  a = input()

  if a == 'FIM':
    break
  
  parte = parteEmail(a)
  vetor.append(parte)

for i in vetor:
  print(i)
