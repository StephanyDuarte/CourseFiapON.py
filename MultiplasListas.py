equipamentos = []
valores = []
seriais = []
departamentos = []

resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("Equipamento.: ", (indice+1))
    print("Nome........: ", equipamentos[indice])
    print("Valor.......: ", valores[indice])
    print("Serial......: ", seriais[indice])
    print("Departamento: ", departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")

for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("valor..:", valores[indice])
        print("Serial.:", seriais[indice])

taxa = float(input("Digite o valor da depreciação em porcentagem: "))
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        valores[indice] = valores[indice] * (1-taxa)
        print("O novo valor de", busca, "será de: ", valores[indice])

for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        del equipamentos[indice]
        del valores[indice]
        del seriais[indice]
        del departamentos[indice]
        break

        print("O novo valor de", busca, "será de: ", valores[indice])