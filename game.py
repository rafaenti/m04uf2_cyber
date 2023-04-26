#!/usr/bin/python3

import os
import random
import xmltodict

from asciimatics.renderers import FigletText

player_health = 100
player_strength = 5

player_name = input("Cuál es tu nombre: ")


def enemy_attack (enemy):
	defeat = False

	name = enemy["name"]
	hp = enemy["health"]
	strength = enemy["strength"]
	while not defeat:
		print("El enemigo "+name+" te ataca [HP: "+str(hp)+" | Strength: "+str(strength)+"]")

		input("Presiona una tecla para contraatacar")

		attack = random.randrange(0, strength + 1)

		hp -= attack






enemies_xml = open("enemies.xml", "r")

os.system('clear')

title = FigletText("EL GRAN JUEGO DE", font="big")
player_title = FigletText(player_name.upper(), font="big")

print(title)
print(player_title)



