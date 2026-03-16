import matplotlib.pyplot as plt
from src.simulation import Simulation

def FrogPopulationSimulation():
    plt.figure()
    plt.plot(sim.data.population_history)
    plt.title("Frog Population Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Population")
    plt.show()

def BirthsPerStep():
    plt.figure()
    plt.plot(sim.data.birth_history)
    plt.title("Births Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Births")
    plt.show()

def DeathsPerStep():
    plt.figure()
    plt.plot(sim.data.death_history)
    plt.title("Deaths Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Deaths")
    plt.show()

def FoodLevelOverTime():
    plt.figure()
    plt.plot(sim.data.food_history)
    plt.title("Food Level Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Food Level")
    plt.show()

def PredatorKillsPerStep():
    plt.figure()
    plt.plot(sim.data.predator_kill_history)
    plt.title("Predator Kills Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Predator Kills")
    plt.show()

def main():

    config = {
        "initial_population": 10,
        "attack_probability": 0.02,
        "food_regeneration_rate": 12,
        "steps": 100
    }
    global sim
    sim = Simulation(initial_population=config["initial_population"], attack_probability=config["attack_probability"], food_regeneration_rate=config["food_regeneration_rate"])
    sim.run(steps=config["steps"])

    sim.data.export_to_csv("run_001.csv")

    FrogPopulationSimulation()
    BirthsPerStep()
    DeathsPerStep()
    FoodLevelOverTime()
    PredatorKillsPerStep()



if __name__ == "__main__":
    main()