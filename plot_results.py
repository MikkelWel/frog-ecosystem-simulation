import csv
import os
import matplotlib.pyplot as plt

SUMMARY_FILE = "runs/statistical_summary.csv"
OUTPUT_FOLDER = "runs/plots"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def load_stat_summary():
    data = {}

    with open(SUMMARY_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            group = row["Group"].strip()
            metric = row["Metric"].strip()
            mean = float(row["Mean"])
            ci_low = float(row["CI Low"])
            ci_high = float(row["CI High"])

            if group not in data:
                data[group] = {}

            data[group][metric] = {
                "mean": mean,
                "ci_low": ci_low,
                "ci_high": ci_high
            }

    return data

def save_line_plot(x, y, title, xlabel, ylabel, filename):
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, filename), dpi=150)
    plt.close()

def save_bar_plot(labels, values, title, xlabel, ylabel, filename):
    plt.figure(figsize=(8, 5))

    plt.bar(labels, values)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_FOLDER, filename), dpi=150)
    plt.close()

def require_metric(data, group, metric):
    if group not in data:
        raise KeyError(f"Missing group '{group}' in statistical_summary.csv")
    if metric not in data[group]:
        raise KeyError(f"Missing metric '{metric}' for group '{group}' in statistical_summary.csv")
    return data[group][metric]["mean"]

def generate_plots():
    data = load_stat_summary()

    print("Available groups in statistical_summary.csv:")
    for group in sorted(data.keys()):
        print(" ", group)

    attack_x = [0.005, 0.01, 0.02, 0.04]
    attack_keys = ["attack_005", "attack_010", "attack_020", "attack_040"]
    attack_y = [require_metric(data, key, "Final Pop") for key in attack_keys]

    save_line_plot(
        attack_x,
        attack_y,
        "Effect of Predator Attack Probability on Final Population",
        "Attack Probability",
        "Mean Final Population",
        "attack_vs_finalpop.png"
    )

    food_x = [5, 10, 15, 25]
    food_keys = ["food_005", "food_010", "food_015", "food_025"]
    food_y = [require_metric(data, key, "Final Pop") for key in food_keys]

    save_line_plot(
        food_x,
        food_y,
        "Effect of Food Regeneration on Final Population",
        "Food Regeneration Rate",
        "Mean Final Population",
        "food_vs_finalpop.png"
    )

    pop_x = [20, 50, 100, 150]
    pop_keys = ["pop_020", "pop_050", "pop_100", "pop_150"]
    pop_y = [require_metric(data, key, "Final Pop") for key in pop_keys]

    save_line_plot(
        pop_x,
        pop_y,
        "Effect of Initial Population on Final Population",
        "Initial Population",
        "Mean Final Population",
        "initialpop_vs_finalpop.png"
    )

    scenario_labels = ["Balanced", "Drought", "Predator Dominated", "Resource Abundance"]
    scenario_keys = [
        "scenario_balanced",
        "scenario_drought",
        "scenario_preddom",
        "scenario_resabun"
    ]
    scenario_y = [require_metric(data, key, "Final Pop") for key in scenario_keys]

    save_bar_plot(
        scenario_labels,
        scenario_y,
        "Scenario Comparison: Mean Final Population",
        "Scenario",
        "Mean Final Population",
        "scenario_finalpop_comparison.png"
    )

    scenario_avgpop = [require_metric(data, key, "Avg Pop") for key in scenario_keys]

    save_bar_plot(
        scenario_labels,
        scenario_avgpop,
        "Scenario Comparison: Mean Average Population",
        "Scenario",
        "Mean Average Population",
        "scenario_avgpop_comparison.png"
    )

    print(f"Plots saved to {OUTPUT_FOLDER}")

if __name__ == "__main__":
    generate_plots()