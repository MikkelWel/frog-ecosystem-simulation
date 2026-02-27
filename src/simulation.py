from src.frog import Frog
from src.predator import Predator
from src.enviroment import Environment
from src.data_collector import DataCollection

class Simulation:
    def __init__(self, initial_population = 10, attack_probability=0.02, food_regeneration_rate=12,):
        self.frogs = [Frog() for _ in range(initial_population)]
        self.predator = Predator(attack_probability=attack_probability)
        self.environment = Environment(food_regen_rate=food_regeneration_rate)
        self.data = DataCollection()
        self.time = 0

    def step(self):
        new_frogs = []

        self.environment.regenerate_food()
        self.environment.random_event()

        for frog in self.frogs:
            if frog.alive:
                food_used = frog.consume_food(self.environment.food)
                self.environment.food -= food_used

                killed = self.predator.attempt_attack(frog)
                if killed:
                    self.data.predator_kills += 1

                frog.step(self.environment.temperature)

                baby = frog.reproduce(self.time)
                if baby:
                    new_frogs.append(baby)
                    self.data.births += 1
                
                if not frog.alive:
                    self.data.deaths += 1
            
        self.frogs = [frog for frog in self.frogs if frog.alive]
        self.frogs.extend(new_frogs)

        self.data.record(self.frogs, self.environment.food)

        self.time += 1

    def run(self, steps=50):
        for _ in range(steps):
            self.step()