def Primo(n):
  if n == 1:
    return False
  for i in range(2,n):
    if n%i==0:
      return False
  return True

n = int(input(""))

if Primo(n) == True and Primo(n+2) == True:
  print("Número forma par de gêmeos")
else:
  print("Número não forma par de gêmeos")