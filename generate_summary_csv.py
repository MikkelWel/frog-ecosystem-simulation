import os
import json
import csv

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

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Run ID",
            "Seed",
            "Initial Pop",
            "Final Pop",
            "Attack Prob",
            "Food Regen",
            "Max Pop",
            "Total Births",
            "Total Deaths",
            "Total Predator Kills",
            "Total Steps",
            "Avg Pop",
            "Avg Energy",
            "Growth Rate",
            "final_growth_rate"
        ])
        writer.writerows(rows)

    print(f"Summary table saved to {output_file}")