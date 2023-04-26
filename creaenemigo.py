#!/usr/bin/python3

import xmltodict


print("Crea un enemigo")
print("---------------")

name = input("Nombre: ")
strength = int(input("Fuerza: "))
health = int(input("Salud: "))


enemy = {
	"enemy": {
		"name": name,
		"damage": strength,
		"health": health
	}
}

enemy_xml = xmltodict.unparse(enemy, pretty=True)

print(enemy_xml)

archivo = open("enemy.xml", "w")

archivo.write(enemy_xml)

archivo.close()
