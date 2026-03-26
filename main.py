import json
import os
import random
import matplotlib.pyplot as plt
from src.simulation import Simulation
from src.event_logger import EventLogger

CONFIG_FOLDER = "configs"
OUTPUT_BASE = "runs"

def validate_config(config):
    if config["initial_population"] < 0:
        raise ValueError("initial_population must be >= 0")

    if not (0 <= config["attack_probability"] <= 1):
        raise ValueError("attack_probability must be between 0 and 1")

    if config["food_regeneration_rate"] <= 0:
        raise ValueError("food_regeneration_rate must be > 0")

    if config["steps"] <= 0:
        raise ValueError("steps must be > 0")

def load_config(config_path):
    with open(config_path) as f:
        return json.load(f)

def save_outputs(sim, run_folder, config):
    os.makedirs(run_folder, exist_ok=True)

    sim.data.export_to_csv(os.path.join(run_folder, "timeseries.csv"))

    with open(os.path.join(run_folder, "summary.json"), "w") as f:
        json.dump(sim.data.summary(), f, indent=4)

    with open(os.path.join(run_folder, "config.json"), "w") as f:
        json.dump(config, f, indent=4)

def plot_metrics(sim):
    plt.figure()
    plt.plot(sim.data.population_history)
    plt.title("Frog Population Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Population")
    plt.show()

    plt.figure()
    plt.plot(sim.data.birth_history)
    plt.title("Births Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Births")
    plt.show()

    plt.figure()
    plt.plot(sim.data.death_history)
    plt.title("Deaths Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Deaths")
    plt.show()

    plt.figure()
    plt.plot(sim.data.food_history)
    plt.title("Food Level Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Food Level")
    plt.show()

    plt.figure()
    plt.plot(sim.data.predator_kill_history)
    plt.title("Predator Kills Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Predator Kills")
    plt.show()

def main():
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

        run_folder = os.path.join(OUTPUT_BASE, f"run_{config['id']}")
        os.makedirs(run_folder, exist_ok=True)

        event_logger = EventLogger(os.path.join(run_folder, "events.csv"))

        sim.run(steps=config["steps"], event_logger=event_logger)
        event_logger.close()

        save_outputs(sim, run_folder, config)

        # plot_metrics(sim)
        print(f"Run {config['id']} complete. Outputs saved in {run_folder}")

if __name__ == "__main__":
    main()