import os
import json
import csv
import matplotlib.pyplot as plt

def generate_summary():
    runs_folder = "runs"
    output_file = os.path.join(runs_folder, "summary_table.csv")

    rows = []

    for run in sorted(os.listdir(runs_folder)):
        run_path = os.path.join(runs_folder, run)

        if not os.path.isdir(run_path):
            continue

        if not run.startswith("run_"):
            continue

        summary_path = os.path.join(run_path, "summary.json")
        config_path = os.path.join(run_path, "config.json")

        if not os.path.exists(summary_path) or not os.path.exists(config_path):
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
            summary.get("max_population", 0),
            summary.get("total_births", 0),
            summary.get("total_deaths", 0),
            summary.get("total_predator_kills", 0),
            summary.get("total_steps", 0),
            summary.get("avg_population", 0),
            summary.get("avg_energy", 0),
            summary.get("growth_rate", 0),
            summary.get("final_growth_rate", 0)
        ])

    headers = [
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
        "Final Growth Rate"
    ]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Summary table saved to {output_file}")

    if rows:
        fig, ax = plt.subplots(figsize=(16, len(rows) * 0.3 + 2))
        ax.axis("tight")
        ax.axis("off")

        table_data = [headers] + rows
        table = ax.table(
            cellText=table_data,
            loc="center",
            cellLoc="center"
        )
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        table.scale(1, 1.4)

        plt.title("Simulation Summary Table", fontsize=14)
        plt.tight_layout()

        image_path = os.path.join(runs_folder, "summary_table.png")
        fig.savefig(image_path, dpi=150, bbox_inches="tight")
        plt.close(fig)

        print(f"Summary table image saved to {image_path}")
    else:
        print("No run data found. summary_table.png was not created.")