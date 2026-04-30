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

def require_metric(data, group, metric):
    if group not in data:
        raise KeyError(f"Missing group '{group}' in statistical_summary.csv")
    if metric not in data[group]:
        raise KeyError(f"Missing metric '{metric}' for group '{group}' in statistical_summary.csv")
    return data[group][metric]

def get_means_and_errors(data, keys, metric):
    means = []
    lower_errors = []
    upper_errors = []

    for key in keys:
        stats = require_metric(data, key, metric)

        mean = stats["mean"]
        ci_low = stats["ci_low"]
        ci_high = stats["ci_high"]

        means.append(mean)
        lower_errors.append(mean - ci_low)
        upper_errors.append(ci_high - mean)

    return means, [lower_errors, upper_errors]

def save_line_plot(x, y, yerr, title, xlabel, ylabel, filename):
    plt.figure(figsize=(8, 5))

    plt.errorbar(x, y, yerr=yerr, marker="o", capsize=5)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_FOLDER, filename), dpi=150)
    plt.close()

def save_bar_plot(labels, values, yerr, title, xlabel, ylabel, filename):
    plt.figure(figsize=(9, 5))

    plt.bar(labels, values, yerr=yerr, capsize=5)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=15)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_FOLDER, filename), dpi=150)
    plt.close()

def generate_plots():
    data = load_stat_summary()

    print("Available groups in statistical_summary.csv:")
    for group in sorted(data.keys()):
        print(" ", group)

    attack_x = [0.005, 0.01, 0.02, 0.04]
    attack_keys = ["attack_005", "attack_010", "attack_020", "attack_040"]
    attack_y, attack_err = get_means_and_errors(data, attack_keys, "Final Pop")

    save_line_plot(
        attack_x,
        attack_y,
        attack_err,
        "Effect of Predator Attack Probability on Final Population",
        "Attack Probability",
        "Mean Final Population",
        "attack_vs_finalpop.png"
    )

    food_x = [5, 10, 15, 25]
    food_keys = ["food_005", "food_010", "food_015", "food_025"]
    food_y, food_err = get_means_and_errors(data, food_keys, "Final Pop")

    save_line_plot(
        food_x,
        food_y,
        food_err,
        "Effect of Food Regeneration on Final Population",
        "Food Regeneration Rate",
        "Mean Final Population",
        "food_vs_finalpop.png"
    )

    pop_x = [20, 50, 100, 150]
    pop_keys = ["pop_020", "pop_050", "pop_100", "pop_150"]
    pop_y, pop_err = get_means_and_errors(data, pop_keys, "Final Pop")

    save_line_plot(
        pop_x,
        pop_y,
        pop_err,
        "Effect of Initial Population on Final Population",
        "Initial Population",
        "Mean Final Population",
        "initialpop_vs_finalpop.png"
    )

    scenario_labels = ["Balanced", "Drought", "Predator", "Abundance"]
    scenario_keys = [
        "scenario_balanced",
        "scenario_drought",
        "scenario_preddom",
        "scenario_resabun"
    ]

    scenario_y, scenario_err = get_means_and_errors(data, scenario_keys, "Final Pop")

    save_bar_plot(
        scenario_labels,
        scenario_y,
        scenario_err,
        "Scenario Comparison: Mean Final Population",
        "Scenario",
        "Mean Final Population",
        "scenario_finalpop_comparison.png"
    )

    scenario_avgpop, scenario_avgpop_err = get_means_and_errors(data, scenario_keys, "Avg Pop")

    save_bar_plot(
        scenario_labels,
        scenario_avgpop,
        scenario_avgpop_err,
        "Scenario Comparison: Mean Average Population",
        "Scenario",
        "Mean Average Population",
        "scenario_avgpop_comparison.png"
    )

    print(f"Plots with confidence interval error bars saved to {OUTPUT_FOLDER}")

if __name__ == "__main__":
    generate_plots()