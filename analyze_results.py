import csv
import math
import os


def compute_stats(values):
    n = len(values)

    if n == 0:
        return {
            "n": 0,
            "mean": 0,
            "std": 0,
            "min": 0,
            "max": 0,
            "ci_low": 0,
            "ci_high": 0
        }

    mean = sum(values) / n

    if n > 1:
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    else:
        variance = 0

    std = math.sqrt(variance)
    ci = 1.96 * (std / math.sqrt(n)) if n > 1 else 0

    return {
        "n": n,
        "mean": mean,
        "std": std,
        "min": min(values),
        "max": max(values),
        "ci_low": mean - ci,
        "ci_high": mean + ci
    }


def get_group_name(run_id):
    if run_id.startswith("scenario"):
        parts = run_id.split("_")

        if len(parts) >= 2:
            return parts[0] + "_" + parts[1]
        
    if "_s" in run_id:
        return run_id.split("_s")[0]

    return run_id


def add_value(groups, group_name, metric_name, value):
    if group_name not in groups:
        groups[group_name] = {
            "Final Pop": [],
            "Max Pop": [],
            "Avg Pop": [],
            "Total Births": [],
            "Total Deaths": [],
            "Total Predator Kills": [],
            "Avg Energy": [],
            "Growth Rate": [],
            "Final Growth Rate": []
        }

    groups[group_name][metric_name].append(value)


def analyze_results():
    input_file = "runs/summary_table.csv"
    output_file = "runs/statistical_summary.csv"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    groups = {}

    with open(input_file, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            run_id = row["Run ID"].strip()
            group_name = get_group_name(run_id)

            add_value(groups, group_name, "Final Pop", float(row["Final Pop"]))
            add_value(groups, group_name, "Max Pop", float(row["Max Pop"]))
            add_value(groups, group_name, "Avg Pop", float(row["Avg Pop"]))
            add_value(groups, group_name, "Total Births", float(row["Total Births"]))
            add_value(groups, group_name, "Total Deaths", float(row["Total Deaths"]))
            add_value(groups, group_name, "Total Predator Kills", float(row["Total Predator Kills"]))
            add_value(groups, group_name, "Avg Energy", float(row["Avg Energy"]))
            add_value(groups, group_name, "Growth Rate", float(row["Growth Rate"]))
            add_value(groups, group_name, "Final Growth Rate", float(row["Final Growth Rate"]))

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

                print(
                    f"  {metric_name}: "
                    f"n={stats['n']}, "
                    f"mean={stats['mean']:.4f}, "
                    f"std={stats['std']:.4f}, "
                    f"95% CI=[{stats['ci_low']:.4f}, {stats['ci_high']:.4f}]"
                )

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