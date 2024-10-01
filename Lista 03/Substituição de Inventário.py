entrada = input("")

stringLista = entrada.strip("[]").split(",")

lista = [item.strip() for item in stringLista]

itemRemover = input("")
itemSubstituir = input("")

if itemRemover in lista:
    for i in range(len(lista)):
        if lista[i] == itemRemover:
            lista[i] = itemSubstituir
    print (lista)
else:
    print("Item não presente no inventário.")