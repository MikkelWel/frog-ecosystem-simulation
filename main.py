import matplotlib.pyplot as plt
from src.simulation import Simulation

def main():
    sim = Simulation(initial_population=10, attack_probability=0.02, food_regeneration_rate=12)
    sim.run(steps=100)

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
    plt.title("Predator kills Per Step")
    plt.xlabel("Time Step")
    plt.ylabel("Predator Kills")
    plt.show()

if __name__ == "__main__":
    main()