

usuarios = { "u1":"Pepe", "u2":"Marta","u3":"Juan"}

print(usuarios)


print(usuarios["u2"])



lista_producto = [{"nombre":"Lampara", "precio":5000 ,"stock":5},
                  {"nombre":"Radio", "precio":12000 ,"stock":7},
                  {"nombre":"Mouse", "precio":8400 ,"stock":3},
                  {"nombre":"Teclado", "precio":15200 ,"stock":9},
                  {"nombre":"Microfono", "precio":19000 ,"stock":5},
                  {"nombre":"Camara", "precio":9300 ,"stock":2},
                  ]



producto_uno = {"nombre":"Lampara", "precio":5000 ,"stock":5}
producto_dos = {"nombre":"Radio", "precio":12000 ,"stock":7}



print( producto_uno["nombre"] )
print( producto_uno["precio"] + producto_dos["precio"])
print(f"Nombre:{producto_dos['nombre']} Stock:{producto_dos['stock']}")

total =  producto_uno["precio"] + producto_dos["precio"] 

print(f"Total: { producto_uno['precio'] + producto_dos['precio'] }")



#KEYS

print( producto_uno.keys())


#VALUES

print( producto_uno.values())



#UPDATE

producto_uno["nombre"] = "Farol"

print(producto_uno)




producto_uno.update({"nombre":"Mouse"})
print(producto_uno)


producto_uno.update({"color":"Rojo"})
producto_uno.update({"color":"Rojo"})

print(producto_uno)



#nombre_producto = input("Ingrese un nombre de producto")
#producto_dos.update({"nombre":nombre_producto})




#METODOS

#GET
#print(usuarios)
#print(usuarios.get("u2"))
#print(usuarios.get("u5"))




#POP 

producto_uno.pop("color")

print(producto_uno)


#DEL

del producto_uno["stock"]

print(producto_uno)


#DEL ALL

#del producto_uno
#print(producto_uno)


#CLear

print(producto_uno.clear())