# lista
lista=['blue','red','green']
demo=[10, "hola mundo",[1,2,3]]
print(demo)
num_list=list((1,2,3,4))  #lista con tupla
print(num_list)

r=list(range(1,10))#crea una ista basada en rango
print(r)
print(type(r))
print(dir(r))

print(len(r))
print(r[1])
print('hola mundo' in demo)#in para saber si un elemento esta en ...
print(demo)
demo[2]="false"#para cambiar elemento remplasa
print(demo)
demo.append(12)#APPEND agrega de a 1 elemento
print(demo)

demo.extend([13,14,"chau"])#extend se agrega como lista 
print(demo)

demo.insert(1,'caca')
print(demo)
demo.insert(len(demo),'opop')
print(demo)

demo.pop()#remove ultimo elemento y tambien remove x posicion
print(demo)

demo.remove(13)
print(demo)
#demo.clear()#remove all
print(demo)

lista.sort()
print(lista)

# lista.sort(reverse=true)
# print(lista)


print(lista.index('red'))





