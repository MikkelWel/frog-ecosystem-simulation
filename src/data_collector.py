import csv
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

        self.avg_energy_history = []
        self.growth_rate_history = []

        self.births = 0
        self.deaths = 0
        self.predator_kills = 0

    def record(self, step, frogs, food):
        self.step_history.append(step)
        self.timestamps.append(datetime.now().isoformat())

        current_population = len(frogs)
        self.population_history.append(current_population)
        self.birth_history.append(self.births)
        self.death_history.append(self.deaths)
        self.food_history.append(food)
        self.predator_kill_history.append(self.predator_kills)

        avg_energy = sum(f.energy for f in frogs) / current_population if frogs else 0
        self.avg_energy_history.append(avg_energy)

        prev_pop = self.population_history[-2] if len(self.population_history) > 1 else 0
        growth_rate = (current_population - prev_pop) / prev_pop if prev_pop > 0 else 0
        self.growth_rate_history.append(growth_rate)

        # Reset per-step counters
        self.births = 0
        self.deaths = 0
        self.predator_kills = 0

    def export_to_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "Timestamp",
                "Step",
                "Population",
                "Births",
                "Deaths",
                "Food Level",
                "Predator Kills",
                "Average Energy",
                "Growth Rate"
            ])

            for i in range(len(self.population_history)):
                writer.writerow([
                    self.timestamps[i],
                    self.step_history[i],
                    self.population_history[i],
                    self.birth_history[i],
                    self.death_history[i],
                    self.food_history[i],
                    self.predator_kill_history[i],
                    round(self.avg_energy_history[i], 2),
                    round(self.growth_rate_history[i], 2)
                ])

    def summary(self):
        return {
            "max_population": max(self.population_history) if self.population_history else 0,
            "min_population": min(self.population_history) if self.population_history else 0,
            "total_births": sum(self.birth_history),
            "total_deaths": sum(self.death_history),
            "total_predator_kills": sum(self.predator_kill_history),
            "total_steps": len(self.step_history),
            "avg_population": round(sum(self.population_history) / len(self.population_history) if self.population_history else 0, 4),
            "avg_energy": round(sum(self.avg_energy_history) / len(self.avg_energy_history) if self.avg_energy_history else 0, 4),
            "growth_rate": round(sum(self.growth_rate_history) / len(self.growth_rate_history) if self.growth_rate_history else 0, 4)
        }