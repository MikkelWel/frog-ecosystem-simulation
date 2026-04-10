import csv
import math
from collections import defaultdict

def compute_stats(values):
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    std = math.sqrt(variance)
    ci = 1.96 * (std / math.sqrt(n)) if n > 0 else 0

    return {
        "n": n,
        "mean": mean,
        "std": std,
        "min": min(values),
        "max": max(values),
        "ci_low": mean - ci,
        "ci_high": mean + ci
    }

def analyze_results():
    input_file = "runs/summary_table.csv"
    output_file = "runs/statistical_summary.csv"

    groups = {}

    with open(input_file, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            run_id = row["Run ID"].strip()

            if run_id.startswith("scenario"):
                parts = run_id.split("_")
                key = parts[0] + "_" + parts[1]
            else:
                key = run_id.split("_s")[0]

            if key not in groups:
                groups[key] = {
                    "Final Pop": [],
                    "Max Pop": [],
                    "Avg Pop": [],
                    "Total Deaths": [],
                    "Growth Rate": []
                }

            groups[key]["Final Pop"].append(float(row["Final Pop"]))
            groups[key]["Max Pop"].append(float(row["Max Pop"]))
            groups[key]["Avg Pop"].append(float(row["Avg Pop"]))
            groups[key]["Total Deaths"].append(float(row["Total Deaths"]))
            groups[key]["Growth Rate"].append(float(row["Growth Rate"]))

    print("\n=== STATISTICAL SUMMARY ===\n")

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Group",
            "Metric",
            "N",
            "Mean",
            "Std Dev",
            "Min",
            "Max",
            "CI Low",
            "CI High"
        ])

        for group_name in sorted(groups.keys()):
            print(group_name)

            for metric_name, values in groups[group_name].items():
                stats = compute_stats(values)

                print(f"  {metric_name}: mean={stats['mean']:.2f}, std={stats['std']:.2f}")

                writer.writerow([
                    group_name,
                    metric_name,
                    stats["n"],
                    round(stats["mean"], 4),
                    round(stats["std"], 4),
                    round(stats["min"], 4),
                    round(stats["max"], 4),
                    round(stats["ci_low"], 4),
                    round(stats["ci_high"], 4)
                ])

            print()

    print(f"Statistical summary saved to {output_file}")

if __name__ == "__main__":
    analyze_results()