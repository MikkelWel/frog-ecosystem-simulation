import json
import os
import shutil

CONFIG_FOLDER = "configs"

# 30 replications: seeds 42 through 71
SEEDS = range(42, 72)

STEPS = 200


def save_config(folder, filename, config):
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)


def reset_configs_folder():
    if os.path.exists(CONFIG_FOLDER):
        shutil.rmtree(CONFIG_FOLDER)

    os.makedirs(os.path.join(CONFIG_FOLDER, "sensitivity"), exist_ok=True)
    os.makedirs(os.path.join(CONFIG_FOLDER, "scenarios"), exist_ok=True)


def generate_attack_configs():
    attack_values = [
        ("005", 0.005),
        ("010", 0.01),
        ("020", 0.02),
        ("040", 0.04)
    ]

    for label, attack_probability in attack_values:
        for seed in SEEDS:
            config_id = f"attack_{label}_s{seed}"

            config = {
                "id": config_id,
                "initial_population": 50,
                "attack_probability": attack_probability,
                "food_regeneration_rate": 15,
                "steps": STEPS,
                "seed": seed
            }

            save_config(
                os.path.join(CONFIG_FOLDER, "sensitivity"),
                f"{config_id}.json",
                config
            )


def generate_food_configs():
    food_values = [
        ("005", 5),
        ("010", 10),
        ("015", 15),
        ("025", 25)
    ]

    for label, food_regeneration_rate in food_values:
        for seed in SEEDS:
            config_id = f"food_{label}_s{seed}"

            config = {
                "id": config_id,
                "initial_population": 50,
                "attack_probability": 0.01,
                "food_regeneration_rate": food_regeneration_rate,
                "steps": STEPS,
                "seed": seed
            }

            save_config(
                os.path.join(CONFIG_FOLDER, "sensitivity"),
                f"{config_id}.json",
                config
            )


def generate_population_configs():
    population_values = [
        ("020", 20),
        ("050", 50),
        ("100", 100),
        ("150", 150)
    ]

    for label, initial_population in population_values:
        for seed in SEEDS:
            config_id = f"pop_{label}_s{seed}"

            config = {
                "id": config_id,
                "initial_population": initial_population,
                "attack_probability": 0.01,
                "food_regeneration_rate": 15,
                "steps": STEPS,
                "seed": seed
            }

            save_config(
                os.path.join(CONFIG_FOLDER, "sensitivity"),
                f"{config_id}.json",
                config
            )


def generate_scenario_configs():
    scenarios = [
        ("balanced_001", 50, 0.02, 15),
        ("drought_001", 50, 0.02, 5),
        ("preddom_001", 50, 0.05, 15),
        ("resabun_001", 50, 0.005, 30)
    ]

    for scenario_name, initial_population, attack_probability, food_regeneration_rate in scenarios:
        for seed in SEEDS:
            config_id = f"scenario_{scenario_name}_s{seed}"

            config = {
                "id": config_id,
                "initial_population": initial_population,
                "attack_probability": attack_probability,
                "food_regeneration_rate": food_regeneration_rate,
                "steps": STEPS,
                "seed": seed
            }

            save_config(
                os.path.join(CONFIG_FOLDER, "scenarios"),
                f"{config_id}.json",
                config
            )


def main():
    reset_configs_folder()

    generate_attack_configs()
    generate_food_configs()
    generate_population_configs()
    generate_scenario_configs()

    total_configs = 16 * len(list(SEEDS))
    print(f"Generated {total_configs} configuration files.")
    print("Configs saved in:")
    print("  configs/sensitivity/")
    print("  configs/scenarios/")


if __name__ == "__main__":
    main()