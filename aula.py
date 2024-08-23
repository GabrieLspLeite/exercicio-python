respostas = []

respostas.append(input("Telefonou para a vítima?[S/N]\n"))
respostas.append(input("Esteve no local do crime?[S/N]\n"))
respostas.append(input("Mora perto da vítima?[S/N]\n"))
respostas.append(input("Devia para a vítima?[S/N]\n"))
respostas.append(input("Já trabalhou com a vítima?[S/N]\n"))

contador = 0
for i in respostas:
    if i == "s" or i == "S":
        contador += 1

if contador == 2:
    print("Você é suspeito")
elif contador > 2 and contador < 5:
    print("Você é cúmplice")
elif contador == 5:
    print("Você é o assassino")
else:
    print("Você é inocente")