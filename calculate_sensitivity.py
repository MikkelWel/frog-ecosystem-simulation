import csv
import os

INPUT_FILE = "runs/statistical_summary.csv"
OUTPUT_FILE = "runs/sensitivity_ratios.csv"


def load_final_population_means():
    means = {}

    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return means

    with open(INPUT_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            group = row["Group"].strip()
            metric = row["Metric"].strip()

            if metric == "Final Pop":
                means[group] = float(row["Mean"])

    return means


def percent_change(old_value, new_value):
    if old_value == 0:
        return 0

    return ((new_value - old_value) / old_value) * 100


def calculate_sensitivity(input_old, input_new, output_old, output_new):
    input_change = percent_change(input_old, input_new)
    output_change = percent_change(output_old, output_new)

    if input_change == 0:
        sensitivity = 0
    else:
        sensitivity = output_change / input_change

    return input_change, output_change, sensitivity


def add_sensitivity_rows(rows, parameter_name, values, groups, means):
    for i in range(len(values) - 1):
        input_old = values[i]
        input_new = values[i + 1]

        group_old = groups[i]
        group_new = groups[i + 1]

        if group_old not in means or group_new not in means:
            print(f"Skipping missing group: {group_old} or {group_new}")
            continue

        output_old = means[group_old]
        output_new = means[group_new]

        input_change, output_change, sensitivity = calculate_sensitivity(
            input_old,
            input_new,
            output_old,
            output_new
        )

        rows.append([
            parameter_name,
            group_old,
            group_new,
            input_old,
            input_new,
            round(output_old, 4),
            round(output_new, 4),
            round(input_change, 4),
            round(output_change, 4),
            round(sensitivity, 4)
        ])


def main():
    means = load_final_population_means()

    if not means:
        return

    rows = []

    add_sensitivity_rows(
        rows,
        "Predator Attack Probability",
        [0.005, 0.01, 0.02, 0.04],
        ["attack_005", "attack_010", "attack_020", "attack_040"],
        means
    )

    add_sensitivity_rows(
        rows,
        "Food Regeneration Rate",
        [5, 10, 15, 25],
        ["food_005", "food_010", "food_015", "food_025"],
        means
    )

    add_sensitivity_rows(
        rows,
        "Initial Population",
        [20, 50, 100, 150],
        ["pop_020", "pop_050", "pop_100", "pop_150"],
        means
    )

    os.makedirs("runs", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Parameter",
            "From Group",
            "To Group",
            "Input Old",
            "Input New",
            "Output Old Mean Final Pop",
            "Output New Mean Final Pop",
            "% Change Input",
            "% Change Output",
            "Sensitivity Ratio"
        ])

        writer.writerows(rows)

    print("\n=== SENSITIVITY RATIOS ===\n")

    for row in rows:
        print(
            f"{row[0]}: {row[1]} -> {row[2]} | "
            f"%Δ input={row[7]}%, "
            f"%Δ output={row[8]}%, "
            f"sensitivity={row[9]}"
        )

    print(f"\nSensitivity ratios saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()