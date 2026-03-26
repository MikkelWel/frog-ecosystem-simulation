# Frog Pond Ecosystem Simulation

This repository contains a Python-based simulation of a simplified frog pond ecosystem.
The simulation models frog population dynamics using stochastic processes, predator-prey interactions, and environmental resource availability. The goal is to observe emergent behavior such as population growth, oscillation, and extinction under probabilistic conditions.

## Course
CS 4632: Modeling and Simulation  
Kennesaw State University

## Author
Mikkel Welch

## Status
- Milestone 2 – Initial Implementation  
- Milestone 3 - In progress

## Requirements
Python Version: Python 3.10+  
Install dependencies:  
- pip install -r requirements.txt

## How to Run
1. Install dependencies:  
   pip install -r requirements.txt
   
2. Run the simulation:  
   python main.py

The simulation will execute a full run and generate several graphs showing ecosystem behavior over time. 

## Implemented Features
* Frog lifecycle with energy and aging
* Probabilistic reproduction model
* Predator with stochastic attack probability
* Enviromental food regeneration system
* Random environmental tempenture variation
* Automated data collection for simulation metrics

## Metrics Collected
The simulation collects the following time-series data:
* Population over time
* Births per step
* Deaths per step
* Predator kills per step
* Food levels

These metrics are used to analyze ecosystem stability and population dynamics

## Models Implemented

### 1. Stochastic Birth-Death Model
Frog reproduction and mortality are governed by probabilistic rules.
Birth events occur when adult frogs reach sufficient energy during breeding periods, while death events occur due to aging, energy depetion, or stochastic mortality.

This model introduces natural variability into population dynamics and allows the system to produce different outcomes across simulation runs.

### 2. Predator-Prey Interaction Model
A predator agent interacts with the frog population by attempting attcks each simulation step.
Predation occurs based on a configurable attack probability and currently targets adult frogs.

This mechanism introduces additional mortality pressure and affects long-term population stability. 

### 3. Environmental Resource Model
The enviroment maintains a dynamic food recourse that frogs consume to gain energy.
Food regenerates each simulation step and can also fluctuate due to random enviromental events.

Food availabilty directly influences reproduction rates and survival, making it a key factor in ecosystem stability.

## Architecture Overview 
The simulation is organized using modular components located in the src/ directory.

**src/frog.py**  
Defines the Frog entity including lifecycle behavior, energy management, reproduction rules, and mortality conditions.

**src/predator.py**  
Implements predator behavior and probabilistic attack mechanics.

**src/enviroment.py**  
Manages enviromental conditions including food regeneration and temperature variations.

**src/data_collectior.py**  
Handles automated data collection for simulation metrics such as population size, births, deaths, food levels, predator kills.

**src/simulation.py**  
Coordinates the simulation data collection for simulation metrics such as population size, births, deaths, food levels, and predator kills.

**main.py**  
Entry point that runs the simulation and generates visualization graphs using matplotlib.

## Project Structure
```
frog-ecosystem-simulation
│
├── src
│   ├── data_collector.py
│   ├── environment.py
│   ├── frog.py
│   ├── predator.py
│   └── simulation.py
│
├── configs/
├── runs/
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── run_experiments.py
```

## Repository
Github Repository:  
https://github.com/MikkelWel/frog-ecosystem-simulation