print("Bienvenido!!")
a = "Cuantas palabras desea en su lista?: "
n=int(input(a))

lista=[]
for i in range(n):
    lista.append(input("Escriba su palabra n° {}: ".format(i+1)))

print()
print("Muy bien su lista es: ")
print(lista)