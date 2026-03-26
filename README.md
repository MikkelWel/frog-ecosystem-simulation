# Frog Pond Ecosystem Simulation

This project implements a stochastic simulation of a frog pond ecosystem. The system models population dynamics through interactions between frogs, predators, and environmental resources. The simulation is designed to explore emergent behaviors such as population growth, collapse, and stability under varying conditions.

## Course

CS 4632: Modeling and Simulation
Kennesaw State University

## Author
Mikkel Welch

## Status
* Milestone 3 – Complete Implementation & Testing

---

## Requirements

* Python 3.10+
* Install dependencies:

```
pip install -r requirements.txt
```

---

## How to Run

Run all simulation experiments:

```
python run_experiments.py
```

This will:

* Execute all configurations in `/configs`
* Generate outputs in `/runs`
* Record results in a master index file

---

## Features

* Frog lifecycle with energy, aging, and reproduction
* Predator-prey interaction model
* Environmental system with food regeneration and temperature variation
* Stochastic birth-death processes
* Parameterized simulation via configuration files
* Automated multi-run execution system

---

## Data Collection System

The simulation includes a comprehensive data collection system:

### Time-Series Data

* Population over time
* Births and deaths per step
* Predator kills per step
* Food levels
* (Optional) Average energy and growth rate

### Event Data

* Birth events
* Death events
* Predator kill events
  (Recorded in `events.csv`)

### Summary Data

* Maximum and minimum population
* Total births and deaths
* Total predator kills

### Run Index

* All runs are tracked in `runs/index.csv`
* Includes parameters, duration, and final population

---

## Output Structure

```
runs/
├── index.csv
├── summary_table.csv
├── summary_table.png
├── run_001/
│   ├── timeseries.csv
│   ├── events.csv
│   ├── summary.json
│   └── config.json
```

---

## Models Implemented

### 1. Stochastic Birth-Death Model

Population changes are governed by probabilistic reproduction and mortality rules, introducing variability and non-deterministic outcomes.

### 2. Predator-Prey Interaction Model

Predators attempt to eliminate adult frogs based on a configurable probability, adding external population pressure.

### 3. Environmental Resource Model

Food availability fluctuates over time and directly impacts survival and reproduction.

---

## Architecture Overview

* `frog.py` – Frog entity logic
* `predator.py` – Predator behavior
* `environment.py` – Environmental dynamics
* `data_collector.py` – Data tracking system
* `simulation.py` – Core simulation engine
* `run_experiments.py` – Batch execution system

---

## Project Structure

```
frog-ecosystem-simulation/
│
├── src
│   ├── data_collector.py
│   ├── environment.py
│   ├── event_logger.py
│   ├── frog.py
│   ├── predator.py
│   └── simulation.py
│
├── configs/
├── runs/
├── .gitignore
├── generate_summary_csv.py
├── main.py
├── README.md
├── requirements.txt
└── run_experiments.py
```

---

## Repository

https://github.com/MikkelWel/frog-ecosystem-simulation