import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

# Add parent directory to sys.path to import shared mdp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.mdp import P, R, STATES, ACTIONS, GAMMA, THETA

def policy_evaluation(P, R, policy, gamma, theta):
    """
    Computes V^pi(s) for a given fixed policy.
    policy: array of indices [pi(High), pi(Low), pi(Charging)]
    """
    num_states = len(STATES)
    V = np.zeros(num_states)
    iterations = 0
    
    while True:
        delta = 0
        V_old = V.copy()
        for s in range(num_states):
            a = policy[s]
            # Bellman Expectation Equation: 
            # V(s) = sum_s' P(s'|s, pi(s)) * [R(s, pi(s)) + gamma * V(s')]
            # Note: R[s, a] already includes the sum over s' for immediate rewards.
            v_new = R[s, a] + gamma * np.sum(P[s, a, :] * V_old)
            V[s] = v_new
            delta = max(delta, abs(V_old[s] - V[s]))
        
        iterations += 1
        if delta < theta:
            break
            
    print(f"Policy Evaluation converged in {iterations} iterations.")
    return V

def task_1_execution():
    print("--- Task 1.1: Build and Verify MDP ---")
    # P and R are already built in shared.mdp. Import verification logic if needed.
    # Verify sum of P[s, a, :]
    for s in range(len(STATES)):
        for a in range(len(ACTIONS)):
            p_sum = np.sum(P[s, a, :])
            assert np.isclose(p_sum, 1.0), f"P[{STATES[s]}, {ACTIONS[a]}] sum is {p_sum}, expected 1.0"
    print("MDP Verification: Sum of P[s, a, :] is 1.0 for all (s, a).")
    print("\nReward Array R[s, a]:")
    print(R)

    print("\n--- Task 1.2: Implement policy_evaluation() ---")
    # Policy: High -> Search (0), Low -> Wait (1), Charging -> Wait (1)
    pi = [0, 1, 1] 
    V_pi = policy_evaluation(P, R, pi, GAMMA, THETA)
    
    print("\nConverged Value Function V^pi(s):")
    for s_idx, state in enumerate(STATES):
        print(f"  V^pi({state:<8}) = {V_pi[s_idx]:.4f}")

    print("\n--- Task 1.3: Plot ---")
    plt.figure(figsize=(8, 5))
    colors = ['#87CEEB', '#FFDAB9', '#90EE90']
    bars = plt.bar(STATES, V_pi, color=colors, edgecolor='black', alpha=0.8)
    plt.title(r'Policy Evaluation: $V^\pi(s)$ for Robot Battery MDP', fontsize=14)
    plt.xlabel('State', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add values on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom', fontweight='bold')

    plot_path = os.path.join(os.path.dirname(__file__), 'plots', 'value_bar_chart.png')
    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")

if __name__ == "__main__":
    task_1_execution()
