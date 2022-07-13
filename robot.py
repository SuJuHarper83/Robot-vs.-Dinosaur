
# create robot character
# As a developer, I want a Robot to have a name, health, and active_weapon.
# As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon

from weapon import Weapon

class Robot():

    def __init__(self, name):
        self.name = name
        self.health = 60
        self.active_weapon = ""
        self.weapons_list = []
        self.build_weapons()

    def attack(self, dinosaur): # pulls in the dinosaur object
        user_choice = int(input("Press 0 to select Iron Fist, 1 to select Gun, and 2 to select Mace"))
        dinosaur.health -= self.weapons_list[user_choice].attack_power
        print()
        print(f"Dinosaur {dinosaur.name} takes a hit from Robot {self.name}'s mighty {self.weapons_list[user_choice].name} for {self.weapons_list[user_choice].attack_power} damage!")
        print(f"Dinosaur {dinosaur.name} has {dinosaur.health} health.")  

    def build_weapons(self):
        weapon_one = Weapon("Iron Fist", 15)
        weapon_two = Weapon("Gun", 10)
        weapon_three = Weapon("Mace", 25)
        self.weapons_list.append(weapon_one)
        self.weapons_list.append(weapon_two)
        self.weapons_list.append(weapon_three)

