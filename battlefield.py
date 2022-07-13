# create battlefield setting
# As a developer, I want the battle to conclude once either 
# the robot or the dinosaur has its health points reduced to zero.

from dinosaur import Dinosaur
from robot import Robot

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur("Jaws", 10)
        self.robot = Robot("Titan")

    def run_game(self):
        
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self): # intro to the players
        print("Come one, come all! Today is the day when the fate between Jaws and Titan will be determined! Who will be the ultimate champion!")

    def battle_phase(self): # attack functions; # while loop
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
          
    def display_winner(self):
        if self.dinosaur.health > 0:
            print()
            print(f"Dinosaur {self.dinosaur.name} reigns supreme!")
        elif self.robot.health > 0:
            print()
            print(f"Robot {self.robot.name} reigns supreme!")
