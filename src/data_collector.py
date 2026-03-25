import csv
import time
from datetime import datetime

class DataCollection:
    def __init__(self):
        self.step_history = []
        self.timestamps = []

        self.population_history = []
        self.birth_history = []
        self.death_history = []
        self.food_history = []
        self.predator_kill_history = []

        self.births = 0
        self.deaths = 0
        self.predator_kills = 0

    def record(self, step, frogs, food):
        self.step_history.append(step)
        self.timestamps.append(datetime.now().isoformat())
        self.population_history.append(len(frogs))
        self.birth_history.append(self.births)
        self.death_history.append(self.deaths)
        self.food_history.append(food)
        self.predator_kill_history.append(self.predator_kills)

        # Reset per-step counters
        self.births = 0
        self.deaths = 0
        self.predator_kills = 0

    def export_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Timestamp", "Step", "Population", "Births", "Deaths", "Food Level", "Predator Kills"])
            for i in range(len(self.population_history)):
                writer.writerow([
                    self.timestamps[i],
                    self.step_history[i],
                    self.population_history[i],
                    self.birth_history[i],
                    self.death_history[i],
                    self.food_history[i],
                    self.predator_kill_history[i]
                ])
    
    def summary(self):
        return {
            "max_population": max(self.population_history) if self.population_history else 0,
            "min_population": min(self.population_history) if self.population_history else 0,
            "total_births": sum(self.birth_history),
            "total_deaths": sum(self.death_history),
            "total_predator_kills": sum(self.predator_kill_history)
        }