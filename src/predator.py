import random

class Predator:
    def __init__(self, attack_probability=0.02):
        self.attack_probability = attack_probability

    def attempt_attack(self, frog):
        if frog.stage != "adult":
            return False

        if random.random() < self.attack_probability:
            frog.alive = False
            return True
        return False