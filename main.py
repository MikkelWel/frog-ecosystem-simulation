import json
import os
import matplotlib.pyplot as plt
from src.simulation import Simulation

CONFIG_FOLDER = "configs"

def load_config(config_path):
    with open(config_path) as f:
        return json.load(f)

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
    config_files = sorted([f for f in os.listdir(CONFIG_FOLDER) if f.endswith(".json")])

    if not config_files:
        print("No config files found.")
        return

    config_path = os.path.join(CONFIG_FOLDER, config_files[0])
    config = load_config(config_path)

    print(f"Running visualization for {config['id']}...")

    sim = Simulation(
        initial_population=config["initial_population"],
        attack_probability=config["attack_probability"],
        food_regeneration_rate=config["food_regeneration_rate"]
    )

    sim.run(steps=config["steps"])

    plot_metrics(sim)

if __name__ == "__main__":
    main()