# -*- coding: utf-8 -*-

#Designing and Debugging
#ex36.py

from sys import exit
import time

your_life = 50.0
your_attack = 6.0
your_armor = 3.0

anmial_life = 70.0
animal_attack = 8.0
animal_armor =4.0

def fight():
	global your_armor
	global your_life
	global your_attack
	
	global anmial_life
	global animal_attack
	global animal_armor
	
	rat1 = your_attack / (your_attack + animal_armor)
	rat2 = animal_attack / (animal_attack + your_armor)
	
	while your_life > 0 and anmial_life > 0 :
		print "You attack the animal"
		anmial_life = anmial_life - your_attack * rat1
		print "animal remain %.2f" % anmial_life
		time.sleep(0.5)
		print "animal fight back"
		your_life = your_life - animal_attack * rat2
		print "you remain %.2f" % your_life
		time.sleep(0.5)
	
	if your_life <= 0 :
		print "your life gone~"
		exit(0)
	else:
		print "You win !!!"
		exit(0)
		
		
def door():
	print "You walk to the west."
	print "You can see a door."
	print "You walk through the door"
	print "A animal suddenly stop you!"
	print "Make your choose!"
	
	ch_door = raw_input(">")
	
	if 'fight' in ch_door :
		fight()
	elif 'escape' in ch_door :
		print "You escape, and close the door!"
		start()
	else:
		print "Please make a choose! There is no time to wast!"
		print "But it's too late"
		print "You die ..."
		exit(0)
		

def desk():
	print "You walk to the north."
	print "You can see a desk."
	print "Make your choose!"
	desk = True
	global your_armor
	
	while True:
		ch_desk = raw_input(">")
	
		if 'take' in ch_desk and 'desk' in ch_desk :
			if desk == True:
				print "You take the desk as your armor!"
				apple = False
				your_armor = your_armor + 4
			else :
				print "It's empty here."
		elif 'back' in ch_desk :
			start()
		else:
			print "You must take something for safe!"

def window():
	print "You walk to the east."
	print "You can see the forest through the window."
	print "Make your choose!"
	apple = True
	global your_life
	
	while True:
		ch_window = raw_input(">")
	
		if 'look' in ch_window and 'around' in ch_window :
			if apple == True:
				print "there is an apple in the box"
				print "You eat it!"
				apple = False
				your_life = your_life + 20
			else :
				print "The wind cold your face."
		elif 'back' in ch_window :
			start()
		else:
			print "shadows in the forest!!!"

def box():
	print "You walk to the south."
	print "You find a box in the corner."
	print "Make your choose!"
	knife = True
	global your_attack
	
	while True:
		ch_box = raw_input(">")
	
		if 'open' in ch_box and 'box' in ch_box :
			if knife == True:
				print "there is a knife in the box"
				print "You take it!"
				knife = False
				your_attack = your_attack + 5
			else :
				print "it is a empty box"
		elif 'back' in ch_box :
			start()
		else:
			print "It's dark and cold!!!"
		

def start():
	print "You are in a room!"
	print "You have four directions 'south' 'east' 'north' 'west' "
	print "which direction you choose to move"
	
	dir = raw_input(">")
	
	if dir == 'south':
		box()
	elif dir == 'east':
		window()
	elif dir == 'north':
		desk()
	elif dir == 'west':
		door()
	else:
		print "Please make a choose!"
		start()
		
start()
		