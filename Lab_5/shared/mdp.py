import numpy as np

# MDP Constants
STATES = ['High', 'Low', 'Charging']
ACTIONS = ['Search', 'Wait']

GAMMA = 0.9
THETA = 1e-6

# P[s, a, s']
# s: 0=High, 1=Low, 2=Charging
# a: 0=Search, 1=Wait
P = np.zeros((3, 2, 3))

# High (0)
P[0, 0, 0] = 0.7  # Search -> High
P[0, 0, 1] = 0.3  # Search -> Low
P[0, 1, 0] = 1.0  # Wait -> High

# Low (1)
P[1, 0, 0] = 0.4  # Search -> High (recharge)
P[1, 0, 1] = 0.6  # Search -> Low
P[1, 1, 1] = 1.0  # Wait -> Low

# Charging (2)
P[2, 1, 0] = 1.0  # Wait -> High
# Search is not allowed in Charging. 
# We'll set it to stay in Charging to make the sum 1.0, but we won't use it.
P[2, 0, 2] = 1.0  

# R[s, a]
# Calculating immediate reward R[s, a] = sum_s' P(s'|s,a) * R(s,a,s')
R = np.zeros((3, 2))

# High
R[0, 0] = 0.7 * 4 + 0.3 * 4  # Search
R[0, 1] = 1.0 * 1            # Wait

# Low
R[1, 0] = 0.4 * (-3) + 0.6 * 4 # Search
R[1, 1] = 1.0 * 1              # Wait

# Charging
R[2, 1] = 1.0 * 0              # Wait
R[2, 0] = -10.0                # Search (Penalty for illegal action)

def verify_mdp():
    print("Verifying MDP Setup...")
    print("\nStates:", STATES)
    print("Actions:", ACTIONS)
    
    print("\nSum of probabilities P[s, a, :] (Should be 1.0):")
    for s_idx, state in enumerate(STATES):
        for a_idx, action in enumerate(ACTIONS):
            p_sum = np.sum(P[s_idx, a_idx, :])
            print(f"  P[{state}, {action}, :] sum = {p_sum:.2f}")
            
    print("\nReward Array R[s, a]:")
    print(R)

if __name__ == "__main__":
    verify_mdp()
