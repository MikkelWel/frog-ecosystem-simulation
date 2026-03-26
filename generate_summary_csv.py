import os
import json
import csv

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
        config["initial_population"],
        config["attack_probability"],
        config["food_regeneration_rate"],
        summary["max_population"],
        summary["total_births"],
        summary["total_deaths"],
        summary["total_predator_kills"],
        summary["total_steps"],
        summary["avg_population"],
        summary["avg_energy"],
        summary["growth_rate"]
    ])

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Run ID",
        "Initial Pop",
        "Attack Prob",
        "Food Regen",
        "Max Pop",
        "Total Births",
        "Total Deaths",
        "Total Predator Kills",
        "Total Steps",
        "Avg Population",
        "Avg Energy",
        "Growth Rate"
    ])
    writer.writerows(rows)

print(f"Summary table saved to {output_file}")