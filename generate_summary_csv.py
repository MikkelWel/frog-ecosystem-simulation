import os
import json
import csv
import matplotlib.pyplot as plt

def generate_summary():
    runs_folder = "runs"
    output_file = "runs/summary_table.csv"

    rows = []

    for run in sorted(os.listdir(runs_folder)):
        run_path = os.path.join(runs_folder, run)

        if not os.path.isdir(run_path):
            continue

        summary_path = os.path.join(run_path, "summary.json")
        config_path = os.path.join(run_path, "config.json")

        if not os.path.exists(summary_path):
            continue

        with open(summary_path) as f:
            summary = json.load(f)

        with open(config_path) as f:
            config = json.load(f)

        rows.append([
            config["id"],
            config.get("seed"),
            config["initial_population"],
            summary.get("final_population", 0),
            config["attack_probability"],
            config["food_regeneration_rate"],
            summary["max_population"],
            summary["total_births"],
            summary["total_deaths"],
            summary["total_predator_kills"],
            summary["total_steps"],
            summary["avg_population"],
            summary["avg_energy"],
            summary["growth_rate"],
            summary.get("final_growth_rate", 0)
        ])

    headers = [
        "Run ID", "Seed", "Initial Pop", "Final Pop", "Attack Prob",
        "Food Regen", "Max Pop", "Total Births", "Total Deaths",
        "Total Predator Kills", "Total Steps", "Avg Pop", "Avg Energy",
        "Growth Rate", "Final Growth Rate"
    ]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([headers])
        writer.writerows(rows)

    print(f"Summary table saved to {output_file}")

    fig, ax = plt.subplots(figsize=(15, len(rows)*0.5 + 2))
    ax.axis('tight')
    ax.axis('off')

    table_data = [headers] + rows

    table = ax.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.07]*len(headers))
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1, 1.5)

    plt.title("Simulation Summary Table", fontsize=14)
    plt.tight_layout()
    plt.show()

    fig.savefig(os.path.join(runs_folder, "summary_table.png"), dpi=150)
    print("Summary table image saved to runs/summary_table.png")