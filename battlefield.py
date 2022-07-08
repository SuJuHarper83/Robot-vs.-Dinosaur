# create battlefield setting
# As a developer, I want the battle to conclude once either 
# the robot or the dinosaur has its health points reduced to zero.

from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur("Jaws", 25)
        self.robot = Robot("Titan")
        self.weapon = Weapon("Iron Fist", 25)

    def run_game(self):
        
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self): # intro to the players
        print("Come one, come all! Today is the day when the fate between Jaws and Titan will be determined! Who will be the ultimate champion!")

    def battle_phase(self): # attack functions; # while loop
        while self.dinosaur.health > 0 and self.robot.health > 0:
            print()
            print(f"Robot {self.robot.name} takes a hit from Dinosaur {self.dinosaur.name} for {self.dinosaur.attack_power} damage!")
            self.dinosaur.attack(self.robot)
            print(f"Robot {self.robot.name} has {self.robot.health}% health.")
            if self.robot.health <= 0:
                print()
                print(f"Dinosaur {self.dinosaur.name} wins!")
            print()
            print(f"Dinosaur {self.dinosaur.name} takes a hit from Robot {self.robot.name}'s mighty {self.weapon.name} for {self.weapon.attack_power} damage!")
            self.robot.attack(self.dinosaur)
            print(f"Dinosaur {self.dinosaur.name} has {self.dinosaur.health}% health.")
            if self.dinosaur.health <= 0:
                print()
                print(f"Robot {self.robot.name} wins!")

    def display_winner(self):
        if self.dinosaur.health > 0:
            print()
            print(f"Dinosaur {self.dinosaur.name} reigns supreme!")
        elif self.robot.health > 0:
            print()
            print(f"Robot {self.robot.name} reigns supreme!")
