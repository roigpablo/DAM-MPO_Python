#Tengo todos los ejercicios comentados para evitar duplicidades en las variables, y para no tener que estar ingresando todos los datos a cada vez que pruebo.
#Para probar los ejercicios lo suyo sería ir descomentando, probando y comentando para que todo funcione bien. GRACIAAAAAS
import math
import random
#1️⃣ Generador de nombres de usuario
#Lo he puesto en inglés pa'hacerme el chulo, pero la primera vez y la úiltima jajajaja


#name = input("Write your name: ")
#surname = input("Write your surname: ")
#username = ((name + surname).lower())
#number = random.randint(10, 99) ##He intentado poner el valor del 01 al 99, y me daba un error al empezar por 0, no se por qué... voy a googlear.
#generatedUser = f"{username}{number}" ##Nunca había usado esto, he intentado concatenar las dos variables de la forma que he hecho siempre con el + y he visto que se quedan separadas por un espacio y de esta forma no.
#print(f"Your generated username is: {generatedUser}")


#2️⃣ Analizador de frases

#frase = input("Introduce una frase para analizarla: ")
#print("La longitud de la frase es de: ", len(frase))
#print("La frase contiene 'Python'? ", "Python" in frase)
#print("La frase en mayúsculas es: ", frase.upper())
#print("La frase invertida es: ", frase[::-1])


#3️⃣ Cálculo de descuentos

#descuento = 0.15
#precio_producto = input("Introduce el precio del producto: ")
#precio_producto = float(precio_producto)
#precio_con_descuento = (precio_producto - (precio_producto * descuento))
#print(f"El precio sin descuento es: {precio_producto}€")
#print(f"El precio final con dos decimales es: {round(precio_con_descuento,2)}€")    #Se puede cambiar el '2' para modificar el número de decimales.
#print(f"El precio redondeado hacia arriba es: {round(precio_con_descuento,0)}€")    #Redondea el precio sin decimales. Cambiar el '0' para ajustar el redonde ode decimales.


#4️⃣ Generador de etiquetas de productos

#nombre_producto = input("Introduce un nombre de producto: ")
#precio_producto = input("Introduce el precio del producto: ")
#precio_producto = float(precio_producto)
#nombre_producto_mayus = nombre_producto.upper()
#print(f"El producto en CAPS es: {nombre_producto_mayus}")
#print(f"El precio con dos decimales es de: {round(precio_producto,2)}€")
#print(nombre_producto_mayus[:1]) #He puesto esta línea cómo paso intermedio para saber si me estaba pillando bien la primera letra del nombre, me ha parecido interesante dejarlo para que veas el proceso.
#print(f"El codigo de la primera letra en ASCII del producto es: {ord(nombre_producto_mayus[:1])}")


#5️⃣ Conversión de tipos y manipulación de listas

#lista_numeros = input("Introduce una lista de números separados por comas: ")
#print(lista_numeros)    #Se muestra pero como string, no como int.
#lista_numeros_enteros = list(set(map(int, lista_numeros.split(","))))
#print("La lista sin duplicados y ordenada es:", sorted(lista_numeros_enteros))


#6️⃣ Creación de mensajes personalizados
#Pide al usuario su nombre, edad y ciudad.
#Muestra un mensaje con toda la información.
#Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.
nombre = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad:"))
ciudad = input("En qué ciudad vives?:")
#No entiendo a que se refiere con lo de redondea hasta la mayoria de edad.
edad_redondeada = math.ceil(edad/18)*18
print(f"Entonces, eres {nombre}, que vives en {ciudad} y tienes {edad} años. Edad mínima para ser mayor de edad: {edad_redondeada}")


#7️⃣ Generador de contraseñas aleatorias
#Pide al usuario su nombre.
#Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
#Muestra la contraseña generada.

#8️⃣ Verificación de nombres en listas
#Pide al usuario su nombre.
#Verifica si su nombre está en una lista de invitados predefinida.
#Si está en la lista, muestra su posición.


#9️⃣ Manipulación de nombres
#Pide al usuario su nombre y apellido.
#Convierte el nombre a minúsculas y el apellido a mayúsculas.
#Genera un alias combinando las primeras 3 letras del nombre y del apellido.
#Muestra el alias generado.


#🔟 Formatear y mostrar datos matemáticos
#Pide al usuario un número decimal.
#Muestra el número redondeado a dos decimales.
#Calcula y muestra su cuadrado.
#Calcula y muestra su raíz cuadrada.
