#!/usr/bin/python3



try:
	archivo = open("numeritos.txt", "r")
#print(archivo.readline())
	linea = archivo.readline()
	lista = linea.split(";")
	print(lista[3])
	archivo.close()
except:
	print("Error al abrir el archivo")


archivo = open("textitos.txt", "w")

archivo.write("ola k ase")

archivo.close()


diccionario = {
	"nombre": "Guillem",
	"apellido": "Granjero",
	"altura": 1.1
}

print(diccionario["altura"])


