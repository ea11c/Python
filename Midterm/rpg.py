'''Eric Adams ea11c'''
from __future__ import print_function
import random
import string
import sys
import threading
from socket import *

class BoardSpace:
	def __init__(self, num):
		self.space_num = num
		self.player = False
		self.enemy = None
		self.crown = False
		self.gate = False
		self.pit = False

class Character:
	def __init__(self, health, attack, defense, name):
		self.hp = health
		self.strength = attack
		self.defense = defense
		self.name = name

class Player(Character):
	def __init__(self, health, attack, defense, name, space):
		Character.__init__(self, health, attack, defense, name)
		self.position = space
	def help(self):
		print('go [N, S, E, or W]\nquit\nhealth\nattack\nhelp')
	def health(self):
		print(self.name, self.hp)
	def quit(self):
		print(self.name, "has decided to abandon their quest and return home in defeat.")
		sys.exit()
	def attack(self, opponent):
		while self.hp > 0 and opponent.hp > 0:
			damage = random.randint(1,6) + self.strength - opponent.defense
			if damage > 0:
				print("{} attacks {} for {} points of damage!".format(self.name,  opponent.name, str(damage)))
				opponent.hp = opponent.hp - damage
			else:
				print("{} blocks the attack from {}!".format(opponent.name, self.name))
			if opponent.hp > 6:
				damage = random.randint(1,6) + opponent.strength - self.defense
			else:
				damage = opponent.ability() - self.defense
			if damage > 0:
				print("{} attacks {} for {} points of damage!".format(opponent.name,  self.name, str(damage)))
				self.hp = self.hp - damage
			else:
				print("{} blocks the attack from {}!".format(self.name, opponent.name))
	def go(self, char):
		if char in ['w', 'W']:
			if self.position % 5 == 0:
				print("The manor wall blocks your route west.")
			else:
				self.position = self.position - 1
		elif char in ['e', 'E']:
			if self.position % 5 == 4:
				print("The manor wall blocks your route east.")
			else:
				self.position = self.position + 1
		elif char in ['n', 'N']:
			if 25 - self.position > 20:
				print("The manor wall blocks your route north.")
			else:
				self.position = self.position - 5
		elif char in ['s', 'S']:
			if 25 - self.position < 6:
				print("The manor wall blocks your route south.")
			else:
				self.position = self.position + 5


class Enemy(Character):
	def ability(self):
		#ability changes based on enemy name, default guard ability will be regular attack
		if self.name not in ['Amrathor', 'Cassie', 'Eldritch', 'Eamon']:
			return self.strength + random.randint(1, 6)
		elif self.name == 'Amrathor':
			return (self.strength + random.randint(1, 6)) * 1.2
		elif self.name == 'Cassie':
			heal = random.randint(1, 4)
			print("Cassie heals {} points of health.".format(heal))
			return self.strength + random.randint(1, 4)
		elif self.name == 'Eldritch':
			return self.strength + random.randint(1, 10)
		elif self.name == 'Eamon':
			print("Eamon switches combat stances, and you are confused leaving him an opening to hit you twice.")
			return self.strength + random.randint(1, 6) + random.randint(1, 6)

class Alea(Player):
	def illusion(self):
		success = random.randint(1, 20)
		if success > 15:
			return True
		else:
			return False

class Veloc(Player):
	def ability(self, opponent):
		damage = random.randint(1, 8) + self.strength * 1.5 - opponent.defense
		opponent.hp = opponent.hp - damage
		print("{} attacks {} for {} points of damage!".format(self.name,  opponent.name, str(damage)))


def Game():
	Board = []
	for num in range(0,25):
		Board.insert(num, BoardSpace(num))
	print("Alea Auir is a wood elf illusionist who is tired of her oppressive family and has decided to run away from home. Veloc Umbrarum is a dwarf assassin/burglar who has been tasked by the Eith wood elves to steal the Auir crown.  Please choose which character you would like to play as by entering [a] or [v]: ")
	enemy1 = Enemy(10, 7, 9, "Cassie")
	enemy2 = Enemy(12, 9, 8, "Eldritch")
	enemy3 = Enemy(10, 9, 7, "Amrathor")
	enemy4 = Enemy(15, 10, 10, "Eamon")
	num_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
	random.shuffle(num_list)
	Board[num_list[0]].enemy = enemy1
	Board[num_list[1]].enemy = enemy2
	Board[num_list[2]].enemy = enemy3
	Board[num_list[3]].enemy = enemy4
	Board[num_list[4]].pit = True
	Board[num_list[5]].gate = True
	Board[num_list[6]].crown = True
	choice = raw_input()
	if choice not in ['a', 'A', 'v', 'V']:
		while choice not in ['a', 'A', 'v', 'V']:
			choice = raw_input("You did not enter a valid choice, please try again: ")
	if choice in ['a', 'A']:
		print("Alea is sick of her family controlling every aspect of her life, she has decided to run away from home tonight.  It is dark and she can't see the ground very well, but she knows that there are several guards and a trap between her and the gate in the wall that leads to freedom...\n")
		toon = Alea(25, 8, 11, "Alea", num_list[8])
		Board[num_list[7]].ally = True
		Board[toon.position].player = True
	elif choice in ['v', 'V']:
		print("Veloc approaches the Auir manor on a cloudy night and quietly slips over the walls into the courtyard.  His task is to find the crown, hopefully he can avoid the guards and any traps...\n")
		toon = Veloc(25, 12, 7, "Veloc", num_list[8])
		Board[num_list[7]].ally = True
		Board[toon.position].player = True
	command = ' '
	while True:
		command = raw_input()
		command = string.lower(command)
		if len(command) < 4:
			print("Enter help to see a list of available commands.")
		elif command == 'help':
			toon.help()
		elif command == 'health':
			toon.health()
		elif command == 'quit':
			toon.quit()
		elif command == 'attack':
			if not Board[toon.position].enemy:
				print("nothing to attack")
			else:
				toon.attack(Board[toon.position].enemy)
				if toon.hp > 0:
					print("The guard is dead, you can continue unimpeded now!")
					Board[toon.position].enemy = None
				else:
					print("The guard killed you.")
					sys.exit()
		elif command[0] + command[1] == 'go':
			if len(command) < 4:
				direction = raw_input("please enter n, s, e, or w")
			else:
				direction = command[3]
			if Board[toon.position].enemy:
				print("You must kill the guard so that he doesn't alert the whole manor!")
			else:			
				Board[toon.position].player == False	
				toon.go(direction)
				Board[toon.position].player == True
				if Board[toon.position].crown == True and toon.name == 'Veloc':
					print("You find the crown and manage to grab it without any trouble and quickly escape!  Having completed your mission successfully, you head to a river to relax and do some fishing.")
					sys.exit()
				if Board[toon.position].gate == True and toon.name == 'Alea':
					print("You made it to the gate, say goodbye to a controlled life and hello to freedom!")
					sys.exit()
				if Board[toon.position].pit == True:
					print("You fell into the pit trap and broke your legs, eventually the guards found you...")
					sys.exit()
				if Board[toon.position].enemy:
					if toon.name == 'Alea':
						print("You see a guard and cast an illusion to try and lure him away from you")
						illusion = toon.illusion()
						if illusion == True:
							print("You succesfully cast an illusion and make the guard think that there is a fire somewhere else on the manor grounds.")

							if toon.position + 5 > 24:
								if not Board[toon.position - 1].enemy:
									new_position = toon.position - 1
								elif not Board[toon.position - 5].enemy:
									new_position = toon.position - 5
							elif toon.position - 5 < 0:
								if not Board[toon.position + 1].enemy:
									new_position = toon.position + 1
								elif not Board[toon.position + 5].enemy:
									new_position = toon.position + 5
							else:
								if not Board[toon.position - 1].enemy:
									new_position = toon.position - 1
								elif not Board[toon.position - 5].enemy:
									new_position = toon.position - 5
								elif not Board[toon.position + 1].enemy:
									new_position = toon.position + 1
								elif not Board[toon.position + 5].enemy:
									new_position = toon.position + 5
							Board[new_position].enemy = Board[toon.position].enemy
							Board[toon.position].enemy = None
						else:
							print("You're illusion was unsucessful, prepare to fight the guard")
					if toon.name == 'Veloc':
						print("You hear a guard coming, so you quickly move to the shadows so that you can ambush him")	
						toon.ability(Board[toon.position].enemy)
						if Board[toon.position].enemy.hp > 0:
							print("The guard survived your ambush, prepare to fight!")
						else:
							print("You managed to kill the guard and drag his body out of sight, you continue searching for the crown.")
							Board[toon.position].enemy = None


def handle_client(c):
	Game()
	c.close()

def Server():
	s = socket(AF_INET, SOCK_STREAM)
	s.bind(("",9000))
	s.listen(5)
	while True:
		c,a = s.accept()
		t = threading.Thread(target = handle_client, args=(c,))
		t.start()

if __name__ == "__main__":
	Game()
