myStr = "hello world"

#dir muestra q cambios podemos hacer al string

print (dir(myStr))

# aca muestra como se hace el cambio
print(myStr.upper())
print(myStr.title())


# replace remplaza string x otro

print(myStr.replace("hello", "hola"))
# print(myStr.replace("hello", "hola").upper())#aca se le agrega mayuscales desp de remplazar
# print(myStr.count("l"))#cuenta cuantas letras "l" hay en el string
print(myStr.startswith("hello")) #muestra si empieza con
print(myStr.split())#separa string , x defecto es espacio vacio.
print(myStr.split(","))
print(myStr.index("e"))
print(len(myStr))
print(myStr[4])
print(myStr.isnumeric())


print("hola mundo " + myStr) # txt mas variable
print (f"hola caca {myStr}") # otra forma de concatenar 
print("hola caca {0}".format(myStr))