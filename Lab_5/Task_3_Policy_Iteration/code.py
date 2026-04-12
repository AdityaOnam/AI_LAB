import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add parent directory to sys.path to import shared mdp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.mdp import P, R, STATES, ACTIONS, GAMMA, THETA

# Reuse policy_evaluation from Task 1 (imported here for self-containment/modularity)
def policy_evaluation(P, R, policy, gamma, theta):
    num_states = len(STATES)
    V = np.zeros(num_states)
    while True:
        delta = 0
        V_old = V.copy()
        for s in range(num_states):
            a = policy[s]
            V[s] = R[s, a] + gamma * np.sum(P[s, a, :] * V_old)
            delta = max(delta, abs(V_old[s] - V[s]))
        if delta < theta:
            break
    return V

def policy_improvement(V, P, R, gamma):
    """
    Updates the policy greedily using the current value function.
    Returns: new_policy, stable (bool)
    """
    num_states = len(STATES)
    num_actions = len(ACTIONS)
    new_policy = np.zeros(num_states, dtype=int)
    
    for s in range(num_states):
        Q_sa = np.zeros(num_actions)
        for a in range(num_actions):
            Q_sa[a] = R[s, a] + gamma * np.sum(P[s, a, :] * V)
        new_policy[s] = np.argmax(Q_sa)
        
    return new_policy

def policy_iteration(P, R, gamma, theta):
    """
    Alternates between Policy Evaluation and Policy Improvement until stabilization.
    """
    num_states = len(STATES)
    # Start with initial policy: all 'Wait' (index 1)
    policy = np.ones(num_states, dtype=int)
    
    V_history = []
    Pi_history = [policy.copy()]
    
    iterations = 0
    while True:
        # 1. Policy Evaluation
        V = policy_evaluation(P, R, policy, gamma, theta)
        V_history.append(V.copy())
        
        # 2. Policy Improvement
        new_policy = policy_improvement(V, P, R, gamma)
        
        # Check stability
        if np.array_equal(new_policy, policy):
            stable = True
        else:
            stable = False
            
        iterations += 1
        print(f"Iteration {iterations}: Policy = {[ACTIONS[a] for a in policy]}, V = {V}")
        
        if stable:
            print(f"Policy Iteration converged in {iterations} iterations.")
            break
            
        policy = new_policy.copy()
        Pi_history.append(policy.copy())

    return policy, V, V_history, Pi_history

def task_3_execution():
    print("\n--- Task 3.1 & 3.2: Implement Policy Iteration ---")
    pi_star, V_star, V_history, Pi_history = policy_iteration(P, R, GAMMA, THETA)
    
    print("\nFinal Optimal Policy pi*(s):")
    for s_idx, state in enumerate(STATES):
        print(f"  pi*({state:<8}) = {ACTIONS[pi_star[s_idx]]}")

    print("\n--- Task 3.3 (a): Plot V^pi Convergence ---")
    V_history = np.array(V_history)
    plt.figure(figsize=(10, 5))
    for s_idx in range(len(STATES)):
        plt.plot(range(1, len(V_history)+1), V_history[:, s_idx], marker='o', label=f'State: {STATES[s_idx]}')
    
    plt.title('Policy Iteration: $V^\pi(s)$ across Policy Steps', fontsize=14)
    plt.xlabel('Policy Iteration Step', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.xticks(range(1, len(V_history)+1))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plot_path_v = os.path.join(os.path.dirname(__file__), 'plots', 'pi_convergence_v.png')
    os.makedirs(os.path.dirname(plot_path_v), exist_ok=True)
    plt.savefig(plot_path_v)
    print(f"V convergence plot saved to {plot_path_v}")

    print("\n--- Task 3.3 (b): Policy Heatmap ---")
    Pi_history = np.array(Pi_history) # shape (steps, states)
    # Transpose for (states, steps)
    data = Pi_history.T 
    
    plt.figure(figsize=(8, 4))
    # 0 = Search, 1 = Wait
    sns.heatmap(data, annot=True, cmap='YlGnBu', cbar=False,
                xticklabels=range(1, len(Pi_history)+1),
                yticklabels=STATES)
    plt.title('Policy Evolution (0=Search, 1=Wait)', fontsize=14)
    plt.xlabel('Iteration Step', fontsize=12)
    plt.ylabel('State', fontsize=12)
    
    plot_path_pi = os.path.join(os.path.dirname(__file__), 'plots', 'policy_heatmap.png')
    plt.savefig(plot_path_pi)
    print(f"Policy heatmap saved to {plot_path_pi}")

if __name__ == "__main__":
    task_3_execution()
