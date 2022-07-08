
# create robot character
# As a developer, I want a Robot to have a name, health, and active_weapon.
# As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon

from weapon import Weapon

weapon = Weapon("Iron Fist", 25)

class Robot():

    def __init__(self, name):
        self.name = name
        self.health = 60
        self.active_weapon = Weapon

    def attack(self, dinosaur): # pulls in the dinosaur object
        dinosaur.health -= weapon.attack_power

