import json
from src.simulation import Simulation
import os
import time
import random

config_folder = "configs"
output_folder = "runs"
os.makedirs(output_folder, exist_ok=True)

for config_file in sorted(os.listdir(config_folder)):
    if not config_file.endswith(".json"):
        continue

    with open(os.path.join(config_folder, config_file)) as f:
        config = json.load(f)

    print(f"Running simulation {config['id']}...")

    random.seed(config.get("seed", None))

    sim = Simulation(
        initial_population=config["initial_population"],
        attack_probability=config["attack_probability"],
        food_regeneration_rate=config["food_regeneration_rate"]
    )

    start = time.time()
    sim.run(steps=config["steps"])
    duration = time.time() - start

    run_folder = os.path.join(output_folder, f"run_{config['id']}")
    os.makedirs(run_folder, exist_ok=True)

    sim.data.export_to_csv(os.path.join(run_folder, "timeseries.csv"))
    with open(os.path.join(run_folder, "summary.json"), "w") as f:
        json.dump(sim.data.summary(), f, indent=4)

    with open(os.path.join(run_folder, "config.json"), "w") as f:
        json.dump(config, f, indent=4)

    print(f"Run {config['id']} complete in {round(duration,2)}s → {run_folder}")