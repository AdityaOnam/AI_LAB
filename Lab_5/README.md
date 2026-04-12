# Robot Battery MDP - Lab 5

This repository contains implementations of various Markov Decision Process (MDP) algorithms applied to a robot battery management problem.

## 📂 Repository Structure

The project is organized into modular tasks:

### `shared/`
- **`mdp.py`**: A shared module containing the definition of States, Actions, and the $P$ (transition) and $R$ (reward) matrices.

### `Task_1_Policy_Evaluation/`
- Implements Iterative Policy Evaluation to compute $V^\pi(s)$ for a fixed policy.
- Includes a logical flowchart and bar chart visualization of state values.

### `Task_2_Value_Iteration/`
- Implements Value Iteration to find the optimal value function $V^*$.
- Includes a flowchart and line plot showing convergence behavior across iterations.

### `Task_3_Policy_Iteration/`
- Implements the full Policy Iteration loop (Evaluation + Improvement).
- Includes a flowchart, value convergence plot, and a policy evolution heatmap.

### `Bonus_Gymnasium/`
- Implements the MDP as a custom Gymnasium environment.
- Verifies that the environment transitions match the analytical MDP matrices.

### `Task_4_Analysis/`
- **`analysis.md`**: Detailed comparison between Value Iteration and Policy Iteration, and interpretation of the optimal robot behavior.

### `Reports/`
- **`Report.md`**: A comprehensive consolidated report embedding all generated plots and flowcharts.

---

## ⚙️ Setup

1. **Install Dependencies:**
   ```bash
   pip install numpy matplotlib seaborn gymnasium graphviz
   ```
2. **Setup Graphviz:**
   Ensure Graphviz is installed and in your system PATH (the scripts also include an environment path fix for common Windows installations).

## 🚀 How to Run

Navigate to any task directory and run the `code.py` or `flowchart/flowchart.py` scripts:

```bash
# Example: Run Policy Iteration
cd Task_3_Policy_Iteration
python code.py
```

All plots will be saved in a `plots/` subdirectory within each task folder.
