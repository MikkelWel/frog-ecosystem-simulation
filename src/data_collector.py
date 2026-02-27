class DataCollection:
    def __init__(self):
        self.population_history = []

        self.birth_history = []
        self.death_history = []
        self.food_history = []
        self.predator_kill_history = []

        self.births = 0
        self.deaths = 0
        self.predator_kills = 0

    def record(self, frogs, food):
        self.population_history.append(len(frogs))
        self.birth_history.append(self.births)
        self.death_history.append(self.deaths)
        self.food_history.append(food)
        self.predator_kill_history.append(self.predator_kills)

        # Reset per-step counters
        self.births = 0
        self.deaths = 0
        self.predator_kills = 0