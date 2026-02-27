import random

class Frog:
    def __init__(self):
        self.energy = 15
        self.age = 0
        self.alive = True
        self.stage = "tadpole"

    def consume_food(self, food_available):
        if food_available > 0:
            if random.random() < 0.8:
                self.energy += 5
                return 1 #consumed 1 unit of food
        return 0
    
    def reproduce(self, current_time):
        if self.stage != "adult":
            return None
        
        #only allow reproduction in "spring"
        if 5 <= (current_time % 40) <= 12:
            if self.energy >= 18:
                reproduction_chance = 0.3
                if random.random() < reproduction_chance:
                    self.energy -= 6
                    return Frog()
        return None
    
    def maybe_die(self):
        if self.age > 50:
            self.alive = False
            return

        if self.energy <= 0:
            self.alive = False
            return
        
        death_probability = 0.02 * (self.age / 50)
        if random.random() < death_probability:
            self.alive = False

    def step(self, temperature):
        self.age += 1

        if self.age > 3:
            self.stage = "adult"

        if temperature < 10:
            self.energy -= 2
        elif temperature > 30:
            self.energy -= 2
        else:
            self.energy -= 1

        self.maybe_die()