
i = int(input("Escolha o número da tabuada: "))

print("Tabuada do número " + str(i))

for numero in range(1,11,1):
    print(str(i) + " x "+ str(numero) + " = " + str(numero * i))
    numero = numero +1

print("Gostou? Aprenda a tabuada de outro valor.")
