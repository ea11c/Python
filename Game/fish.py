#!/usr/bin/python2

import os
import pygame
import time

class Map():
	def __init__(self, dirname):
		#controls game loop
		self.playing = True
		#called to load levels
		self.load_lvls(dirname)
		#the size of a block is 25x25
		self.atom = 25
		#the valid keys that can be pressed are up, left, down, and right
                self.keys = [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT]
		#images being set to variables
                self.tele_img = pygame.image.load("teleport.png")
		self.fish_img = pygame.image.load("fish.png")
		self.button_img = pygame.image.load("butto.png")
		#designating which blocks are which pictures
		self.dic = {
	 		"W" : pygame.image.load("wall.png"),
			"G" : pygame.image.load("glory.png"),
			"I" : pygame.image.load("ice.png"),
			" " : pygame.image.load("ground.png"),
		}
		#load the level
		self.load_level()

	#loads levels from specified directory	
	def load_lvls(self, dirname):
		#level counter starts at 0
		self.lvl_i = 0
		#empty level list
		self.levels = []
		#for each file in the directory, if it ends with .lvl, its a level
		for f in os.listdir(dirname):
			if f.endswith('.lvl'):
				#append directory name and filename to get full path
				self.levels.append(os.path.join(dirname, f))
		#sort the levels, i.e. level1.lvl precedes level2.lvl
		self.levels = sorted(self.levels)

	#loads the level
	def load_level(self):
		#make an empty lsit
		self.level = []
		# 'with' is a keyword used as an alternative to try/except blocks
		with open(self.levels[self.lvl_i], 'r') as f:
			#read each line
			for l in f.readlines():
				#if the file is done, continue
				#append line to level list for every line
				if not l:
					continue
				self.level.append(l.strip())
		#initialize map after level contents are loaded
		self.init_map()
                self.draw()

	#initializes the map
	def init_map(self):
		#go through the level list
		for i in range(len(self.level)):
			#make a list out of the contents read from file
			self.level[i] = list(self.level[i])

		#initialize number of fish to 0
		self.fish_cnt = 0	
		#go through the list with file contents	
		for i in range(len(self.level)):
			#go through each list within the big list of levels
			for j in range(len(self.level[i])):
				#if it is a fish, increment the fish count
				#if it is a goal block, note the position and hide it for the time being
				#if it is a character block, set it equal to the player position
				if self.is_fish(j, i):
					self.fish_cnt += 1
				elif self.level[i][j] == "G":
					self.door = (j, i)
					self.level[i][j] = " "
				elif self.level[i][j] == "C":
					self.p = Player(j, i, self.atom)
					self.level[i][j] = " "
		#initialize the teleports and buttons
		self.init_teleports()
		self.init_buttons()
	#initializes the buttons
	def init_buttons(self):
		#make an empty dictionary
		self.buttons = {}
		#go through the levels list
		for i in range(len(self.level)):
			#go through each level contents
			for j in range(len(self.level[i])):
				#make variable for level position
				n = self.level[i][j]
				#if that position is not a digit, continue
				if not n.isdigit():
					continue
				#if the position is an even number
				#else, its odd. that means the block should be ice
				if self.is_even(j, i):
					#set to True, so we know to place a button there
					self.buttons[n] = True
				else:
					if n not in self.buttons:
						self.buttons[n] = []
					self.buttons[n].append((j, i))
					self.level[i][j] = "I"

	#initializes teleports
        def init_teleports(self):
		#make an empty dictionary
		self.teles = {}
		#go through levels
                for i in range(len(self.level)):
			#go through level contents, for each level
                        for j in range(len(self.level[i])):
				#if position isn't lowercase, skip it
                                if not self.level[i][j].islower():
                                        continue
				#make temp variable
                                l = self.level[i][j]
				#
                                if l not in self.teles:
                                        self.teles[l] = Teleport(j, i)
                                else:
                                        self.teles[l].add(j, i)
	#checks the keys pressed
        def check_keys(self, keyin):
                for x in self.keys:
                        if keyin[x]:
				#if input was valid, move the player
                                self.move_player(x)

        def move_player(self, key):
                self.erase_player()
                
                direction = self.keys.index(key)
                if direction != self.p.angle:
                        self.p.change_direction(direction)
                        self.draw_player()
                        return

		coll = False
                self.p.move(direction)
                if self.collide():
			coll = True
                        self.p.move(direction, True)

		self.draw()
		if not coll:
			self.event()

        def event(self):
                l = self.level[self.p.y][self.p.x]
                if l.islower():
                        self.p.move_to(self.teles[l].next_xy((self.p.x, self.p.y)))
                        self.draw()
		elif self.is_fish(self.p.x, self.p.y):
			self.fish_cnt -= 1
			f = chr(ord(l) - 1)
			self.level[self.p.y][self.p.x] = f
			if not self.fish_cnt:
				tmpx, tmpy = self.door
				self.level[tmpy][tmpx] = "G"
			self.draw()
		elif self.is_even(self.p.x, self.p.y) and l in self.buttons:
			for tx, ty in self.buttons[chr(ord(l) + 1)]:
				self.level[ty][tx] = "W" if self.level[ty][tx] == "I" else "I"
			self.draw()

		if self.level[self.p.y][self.p.x] == "I":
			self.p.move(self.p.angle)
			if self.collide():
				self.p.move(self.p.angle, True)
			else:
				self.wait_sec(0.07)
				self.draw()
				self.event()
		elif self.collide_goal():
                        print "YUR SO GOOD"
			self.lvl_i += 1
			if self.lvl_i == len(self.levels):
				self.playing = False
			else:
				self.load_level() 

        def collide(self):
                return self.level[self.p.y][self.p.x] == "W"

	def collide_goal(self):
                return self.level[self.p.y][self.p.x] == "G"
		
	def is_even(self, x, y):
		n = self.level[y][x]
		return n.isdigit() and int(n) % 2 == 0

	def is_fish(self, x, y):
		l = ord(self.level[y][x])
		for k in self.dic:
			if l - ord(k) == 1:
				return True
		return False
                
	def draw(self):
		wid = s_width / self.atom
		sy = self.p.y - (wid / 2)
                
		for y in range(wid):
                        sx = self.p.x - (wid / 2)
			for x in range(wid):
                                self.draw_block(x, y, sx, sy)
                                sx += 1
                        sy += 1

                self.draw_player()

        def erase_player(self):
                w = s_width / self.atom / 2
                self.draw_block(w, w, self.p.x, self.p.y)
                
        def draw_player(self):
                screen.blit(self.p.image, (s_width / 2, s_height / 2))
                pygame.display.flip()

	def draw_block(self, x, y, sx, sy):
                if sx < 0 or sy < 0 or sy >= len(self.level) or sx >= len(self.level[sy]):
			pygame.draw.rect(screen, (0, 0, 0), (x * self.atom, y * self.atom, self.atom, self.atom))
		elif self.level[sy][sx].islower():
                        screen.blit(self.tele_img, (x * self.atom, y * self.atom))
                elif self.is_fish(sx, sy):
			l = chr(ord(self.level[sy][sx]) - 1)
			screen.blit(self.dic[l], (x * self.atom, y * self.atom))
			screen.blit(self.fish_img, (x * self.atom, y * self.atom))
		elif self.level[sy][sx].isdigit():
			if self.is_even(sx, sy):
				screen.blit(self.button_img, (x * self.atom, y * self.atom))
			else:
				screen.blit(self.dic['I'], (x * self.atom, y * self.atom))
		else:
		        screen.blit(self.dic[self.level[sy][sx]], (x * self.atom, y * self.atom))

        def wait_sec(self, sec):
                t = sec / 0.01
                for i in range(int(t)):
                        time.sleep(0.01)
                        pygame.event.clear()

	#def game_over(self):
	#	len = screen.info().current_w
	#	w, h = self.over_img.get_rect().size
	#	screen.blit(self.over_img, (len - w, len - h))
	#	ks = pygame.key.get_pressed()
	#	while not ks[K_r]:
	#		pass
	#	self.__init__()

class Teleport():
        def __init__(self, x, y):
                self.xys = [(x, y)]

        def add(self, x, y):
                self.xys.append((x, y))

        def next_xy(self, xy):
                p = (self.xys.index(xy) + 1) % len(self.xys)
                return self.xys[p]

class Player():
	def __init__(self, x, y, atom):
		self.image = pygame.image.load('Man.png')
		self.x, self.y = x, y
                self.angle = 0

        def move_to(self, xy):
                self.x, self.y = xy

        def move(self, direction, cancel=False):
                offset = ((direction & ~1) - 1) * (-1 if cancel else 1)
                if not direction % 2:
                        self.y += offset
                else:
                        self.x += offset

        def change_direction(self, key):
                self.image = pygame.transform.rotate(self.image, (key - self.angle) * 90)
                self.angle = key		

if __name__ == "__main__":
        pygame.init()
        clk = pygame.time.Clock()

	s_width, s_height = 500, 500
	screen = pygame.display.set_mode((s_width, s_height))
	
        world = Map("fish_levels")
        while world.playing:
                clk.tick(60)
                keyin = pygame.key.get_pressed()
		if keyin[pygame.K_ESCAPE] and (keyin[pygame.K_RSHIFT] or keyin[pygame.K_LSHIFT]):
			pygame.quit()
			quit()
                world.check_keys(keyin)
                world.wait_sec(0.07)
                pygame.event.clear()
	pygame.quit()
