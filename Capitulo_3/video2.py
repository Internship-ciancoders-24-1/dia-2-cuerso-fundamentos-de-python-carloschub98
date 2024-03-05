a = [1,2]
b=[2,3]

print(a+b)

print(a*2)

# Del es para eliminar una pos

d = list(range(0,100,2))
e = list(range(0,10))

frutas = list()

frutas.append('coco')
frutas.append('mango')
frutas.append('naranja')
print(len(frutas))
print(frutas)


some_fruit = frutas.pop() #elimina el punto

print(some_fruit)

del frutas[0]

print(frutas)

#existe un metodo sorted que sire para ordenar una lista