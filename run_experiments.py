import json
import os
import time
import random
import csv
from src.simulation import Simulation
from src.event_logger import EventLogger
from generate_summary_csv import generate_summary

CONFIG_FOLDER = "configs"
OUTPUT_FOLDER = "runs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def validate_config(config):
    if config["initial_population"] < 0:
        raise ValueError("initial_population must be >= 0")

    if not (0 <= config["attack_probability"] <= 1):
        raise ValueError("attack_probability must be between 0 and 1")

    if config["food_regeneration_rate"] <= 0:
        raise ValueError("food_regeneration_rate must be > 0")

    if config["steps"] <= 0:
        raise ValueError("steps must be > 0")

def load_config(path):
    with open(path) as f:
        return json.load(f)

def save_outputs(sim, run_folder, config):
    os.makedirs(run_folder, exist_ok=True)

    sim.data.export_to_csv(os.path.join(run_folder, "timeseries.csv"))

    with open(os.path.join(run_folder, "summary.json"), "w") as f:
        json.dump(sim.data.summary(), f, indent=4)

    with open(os.path.join(run_folder, "config.json"), "w") as f:
        json.dump(config, f, indent=4)

def main():
    index_file = os.path.join(OUTPUT_FOLDER, "index.csv")
    file_exists = os.path.isfile(index_file)

    for config_file in sorted(os.listdir(CONFIG_FOLDER)):
        if not config_file.endswith(".json"):
            continue

        config_path = os.path.join(CONFIG_FOLDER, config_file)
        config = load_config(config_path)

        validate_config(config)

        print(f"Running simulation {config['id']}...")

        random.seed(config.get("seed", None))

        sim = Simulation(
            initial_population=config["initial_population"],
            attack_probability=config["attack_probability"],
            food_regeneration_rate=config["food_regeneration_rate"]
        )

        run_folder = os.path.join(OUTPUT_FOLDER, f"run_{config['id']}")
        os.makedirs(run_folder, exist_ok=True)

        event_logger = EventLogger(os.path.join(run_folder, "events.csv"))

        start = time.time()
        sim.run(steps=config["steps"], event_logger=event_logger)
        duration = time.time() - start

        event_logger.close()

        save_outputs(sim, run_folder, config)

        final_population = (
            sim.data.population_history[-1]
            if sim.data.population_history else 0
        )

        with open(index_file, "a", newline="") as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow([
                    "run_id",
                    "seed",
                    "initial_population",
                    "attack_probability",
                    "food_regeneration_rate",
                    "steps",
                    "duration_seconds",
                    "final_population"
                ])
                file_exists = True

            writer.writerow([
                config["id"],
                config.get("seed", None),
                config["initial_population"],
                config["attack_probability"],
                config["food_regeneration_rate"],
                config["steps"],
                round(duration, 4),
                final_population
            ])

        print(f"Run {config['id']} complete in {round(duration,4)}s → {run_folder}")

generate_summary()

if __name__ == "__main__":
    main()