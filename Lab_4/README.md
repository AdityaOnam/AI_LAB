
# AI Scheduling & Optimization Algorithms

This repository contains the implementation of two Artificial Intelligence search strategies—**Greedy Search** and **A* (A-Star) Search**—applied to a complex task scheduling problem. 

The goal of this project is to assign dependent tasks to specific days while respecting prerequisite constraints (Directed Acyclic Graphs), group-size limits, and optimizing for the lowest total catering cost using a "Global Fixed Menu" rule.

## 📂 Repository Structure

The project is divided into two main components based on the algorithm used:

### `Task_A/` (Greedy Search Algorithm)
This folder contains the baseline Greedy scheduling approach, which attempts to build a valid schedule by making locally optimal choices day-by-day.
* **`Code.py`**: The main driver script for the Greedy algorithm. Includes an interactive CLI menu to test different problem instances and heuristic strategies.
* **`flowchart/flowchart.py`**: A Graphviz script that generates the logical flowchart for the Greedy algorithm.
* **`greedy_flowchart.png`**: The rendered flowchart showing the Parse -> Queue -> Execute loop.
* **`Instance_1.png`, `Instance_2.png`, `Instance_3.png`**: Rendered Dependency Graphs (DAGs) illustrating the topological structures of the 3 test instances used in the project.

### `Task_B/` (A* Search Algorithm)
This folder contains the optimal A* search approach, which navigates a state-space tree to find the absolute mathematically cheapest schedule, balancing project duration against the global menu penalty.
* **`code.py`**: The main driver script for the A* search. Includes a CLI menu, heuristic calculations (volume/depth bounds), Pareto pruning, and a side-by-side comparison with the Greedy baseline.
* **`Flowchart/flowchart.py`**: Graphviz scripts to generate both the main A* logic flowchart and the partial state-space search tree.
* **`task2_astar_schedule.png`**: The rendered logical flowchart for the A* optimization process.
* **`childTree.png`**: A visualization of the Level 1 state-space tree expansion, demonstrating how A* evaluates its first set of child nodes.

---

## ⚙️ Prerequisites & Setup

To run the code and generate the flowcharts, you will need Python installed on your system along with the `graphviz` library.

**1. Install the Python wrapper:**
```bash
pip install graphviz
```

**2. Install the Graphviz Core Software:**
The Python library requires the actual Graphviz executables to render the PNG files. 
* **Windows:** Download and install from [Graphviz.org](https://graphviz.org/download/) (Make sure to add it to your system PATH during installation).
* **Mac:** `brew install graphviz`
* **Linux:** `sudo apt-get install graphviz`

---

## 🚀 How to Run

### Running the Scheduling Algorithms
Navigate to either the `Task_A` or `Task_B` folder in your terminal and execute the main python scripts. Both scripts feature an interactive menu driven by the console.

**To run the Greedy Algorithm:**
```bash
cd Task_A
python Code.py
```

**To run the A* Algorithm (and comparison):**
```bash
cd Task_B
python code.py
```

### Generating the Flowcharts
If you want to re-render the flowcharts or edit the node logic, run the flowchart scripts directly:
```bash
cd Task_A/flowchart
python flowchart.py
```

---

## 📊 Test Instances
Both algorithms are tested against three distinct graph topologies to ensure robustness:
1. **Instance 1 (Hybrid Tree):** The baseline test (11 tasks, Group Size: 2) with mixed constraints.
2. **Instance 2 (Linear Pipeline):** A strict sequential depth test.
3. **Instance 3 (Wide Tree):** A highly parallel layout designed to stress-test the A* "Global Max Menu" cost optimization vs. Greedy speed.
```

Let me know if you need to add any specific student names, ID numbers, or course codes to the top of this file!