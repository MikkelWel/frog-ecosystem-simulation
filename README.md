# Frog Pond Ecosystem Simulation

This repository contains a Python-based simulation of a simplified frog pond ecosystem.
This project simulates a frog ecosystem using stochastic population modeling, predator-prey interaction, and environmental food dynamics. The goal is to observe emergent behavior such as population growth, oscillation, and extinction under probabilistic conditions.

## Course
CS 4632: Modeling and Simulation  
Kennesaw State University

## Author
Mikkel Welch

## Status
Milestone 2 – Initial Implementation

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
   
2. Run the simulation:
   python main.py

## Implemented Features
* Frog lifecycle with energy and aging
* Probabilistic reproduction
* Predator with stochastic attack probability
* Food regeneration system
* Random environmental variation
* Data collection for:
  * Population over time
  * Births per step
  * Deaths per step
  * Predator kills per step
  * Food levels

## Models Implemented

### 1. Stochastic Birth-Death Model
Frog reproduction and mortality are governed by probabilistic rules.
Birth and death events occur based on energy thresholds and random chance, producing non-deterministic population dynamics.

### 2. Predator-Prey Interaction Model
A predator agent attacks frogs with a configurable attack probability.
This introduces density-dependent mortality into the system.

### 3. Environmental Resource Model
Food availability changes over time and affects frog survival and reproduction.
Food regeneration and environmental variability influence population stability.