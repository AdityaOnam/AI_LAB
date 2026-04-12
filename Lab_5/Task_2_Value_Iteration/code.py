import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

# Add parent directory to sys.path to import shared mdp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.mdp import P, R, STATES, ACTIONS, GAMMA, THETA

def value_iteration(P, R, gamma, theta):
    """
    Computes the optimal value function V* using Bellman Optimality updates.
    Returns: V_star, V_history
    """
    num_states = len(STATES)
    num_actions = len(ACTIONS)
    V = np.zeros(num_states)
    V_history = [V.copy()]
    iterations = 0
    
    while True:
        delta = 0
        V_old = V.copy()
        for s in range(num_states):
            # Q(s, a) = sum_s' P(s'|s,a) * [R(s,a) + gamma * V_old(s')]
            # Since R[s, a] is already immediate reward sum:
            Q_sa = np.zeros(num_actions)
            for a in range(num_actions):
                # Note: 'Search' is not allowed in Charging (state 2). 
                # We handle this by either extremely low reward or just ignoring it, 
                # but following the formula is safer if R[2, 0] is small.
                Q_sa[a] = R[s, a] + gamma * np.sum(P[s, a, :] * V_old)
            
            V[s] = np.max(Q_sa)
            delta = max(delta, abs(V_old[s] - V[s]))
        
        V_history.append(V.copy())
        iterations += 1
        if delta < theta:
            break
            
    print(f"Value Iteration converged in {iterations} iterations.")
    return V, V_history

def extract_policy(V_star, P, R, gamma):
    """
    Greedily extracts the optimal policy from the optimal value function.
    """
    num_states = len(STATES)
    num_actions = len(ACTIONS)
    pi_star = np.zeros(num_states, dtype=int)
    
    for s in range(num_states):
        Q_sa = np.zeros(num_actions)
        for a in range(num_actions):
            Q_sa[a] = R[s, a] + gamma * np.sum(P[s, a, :] * V_star)
        
        pi_star[s] = np.argmax(Q_sa)
        
    return pi_star

def task_2_execution():
    print("\n--- Task 2.1: Implement value_iteration() ---")
    V_star, V_history = value_iteration(P, R, GAMMA, THETA)
    
    print("\nConverged Optimal Value Function V*(s):")
    for s_idx, state in enumerate(STATES):
        print(f"  V*({state:<8}) = {V_star[s_idx]:.4f}")

    print("\n--- Task 2.2: Extract Optimal Policy ---")
    pi_star = extract_policy(V_star, P, R, GAMMA)
    
    print("\nOptimal Policy pi*(s):")
    for s_idx, state in enumerate(STATES):
        print(f"  pi*({state:<8}) = {ACTIONS[pi_star[s_idx]]}")

    print("\n--- Task 2.3: Plot Convergence ---")
    V_history = np.array(V_history)
    plt.figure(figsize=(10, 6))
    linestyles = ['-', '--', '-.']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for s_idx in range(len(STATES)):
        plt.plot(V_history[:, s_idx], label=f'State: {STATES[s_idx]}', 
                 linestyle=linestyles[s_idx], color=colors[s_idx], linewidth=2)
        
    plt.title('Value Iteration Convergence: $V(s)$ across Iterations', fontsize=14)
    plt.xlabel('Iteration Number', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend(fontsize=11)
    
    plot_path = os.path.join(os.path.dirname(__file__), 'plots', 'convergence_plot.png')
    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")

if __name__ == "__main__":
    task_2_execution()
