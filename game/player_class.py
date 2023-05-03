#!/usr/bin/python3

import xmltodict
import random

class Player:
	def __init__ (self, name="", health=100, strength=10, level=1, xp=0):
		self.name = name
		self.health = health
		self.strength = strength
		self.level = level
		self.xp = xp

		xml_file = open("levels.xml", "r")

		levels = xmltodict.parse(xml_file.read())

		xml_file.close()

		tmp = levels["levels"]["level"]
		
		print(tmp)

		self.levels = {}

		for level in tmp:
			self.levels[ int(level["@num"]) ] = int(level["@xp"])


		print(self.levels)


	def set_health (self, health):
		self.health = health

	def set_strength (self, strength):
		self.strength = strength

	def set_level (self, level):
		self.level = level


	def get_level (self, xp = -1):
		if xp == -1:
			return self.level

		level_cur = self.level

		for level in self.levels:
			if self.levels[level] <= xp:
				level_cur = level
				
		return level_cur


	def set_xp (self, xp):
		self.xp = xp


	def attack (self):
		return random.randint(0, self.strength)


	def hurt (self, damage):
		self.health -= damage

		if self.health > 0:
			return False
		
		return True

	
	def show_info (self):
		print("Name: "+self.name)
		print("Health: "+str(self.health))
		print("Strength: "+str(self.strength))
		print("Level: "+str(self.level))
		print("XP: "+str(self.xp))


	def input_info (self):
		self.name = input("Introduce el nombre: ")
		self.health = int(input("Introduce la vida: "))
		self.strength = int(input("Introduce la fuerza: "))
		self.level = int(input("Introduce el nivel base: "))
		self.xp = int(input("Introduce la experiencia base: "))

	
	def write_info (self):
		info = {
			"name": self.name,
			"health": self.health,
			"strength": self.strength,
			"level": self.level,
			"xp": self.xp
		}

		player_info = {
			"player": info
		}

		xml_file = open("player.xml", "w")

		xml_file.write(xmltodict.unparse(player_info))
	

	def read_info (self):
		xml_file = open("player.xml", "r")

		player_dict = xmltodict.parse(xml_file.read())

		info = player_dict["player"]

		self.name = info["name"]
		self.health = int(info["health"])
		self.strength = int(info["strength"])
		self.level = int(info["level"])
		self.xp = int(info["xp"])

	
	
if __name__ == "__main__":
	player = Player("Juan Ramón")

	print(player.get_level(66))


