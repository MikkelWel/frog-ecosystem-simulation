from src.simulation import Simulation
import time
import json

runs = [
    {"id": "001", "population": 50, "attack": 0.2, "food": 12},
    {"id": "002", "population": 100, "attack": 0.2, "food": 12},
    {"id": "003", "population": 50, "attack": 0.4, "food": 12},
    {"id": "004", "population": 150, "attack": 0.3, "food": 12},
    {"id": "005", "population": 80, "attack": 0.25, "food": 10},
    {"id": "006", "population": 120, "attack": 0.35, "food": 15},
    {"id": "007", "population": 60, "attack": 0.3, "food": 8},
    {"id": "008", "population": 90, "attack": 0.4, "food": 14},
    {"id": "009", "population": 110, "attack": 0.2, "food": 10},
    {"id": "010", "population": 70, "attack": 0.3, "food": 12},
    {"id": "011", "population": 140, "attack": 0.25, "food": 15},
    {"id": "012", "population": 100, "attack": 0.35, "food": 10}
]

for run in runs:
    start = time.time()

    sim = Simulation(
        initial_population=run["population"],
        attack_probability=run["attack"],
        food_regeneration_rate=run["food"]
    )

    sim.run(steps=200)

    duration = time.time() - start

    filename = f"run_{run['id']}.csv"
    sim.data.export_to_csv(filename)

    config_filename = f"run_{run['id']}_config.json"

    with open(config_filename, "w") as f:
        json.dump(run, f, indent=4)

    print(f"Run {run['id']} complete in {round(duration, 2)}s → {filename}")