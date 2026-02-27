import random

class Environment:
    def __init__(self):
        self.food = 50
        self.temperature = 20

    def regenerate_food(self):
        max_food = 100
        self.food += 12
        if self.food > max_food:
            self.food = max_food
        if self.food < 0:
            self.food = 0

    def random_event(self):
        self.temperature += random.randint(-2, 2)

        if random.random() < 0.1:
            self.food -= 10
            if self.food < 0:
                self.food = 0