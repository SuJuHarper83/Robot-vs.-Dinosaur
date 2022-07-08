# create dinosaur character
# As a developer, I want a Dinosaur to have a name, health, and attack power
# As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power

class Dinosaur():

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50

    def attack(self, robot): # pulls in the robot object
        robot.health -= self.attack_power
                
            
