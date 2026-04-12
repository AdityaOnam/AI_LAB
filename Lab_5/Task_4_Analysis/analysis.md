# Task 4 | Analysis and Interpretation

### 4.1 Compare Value Iteration and Policy Iteration
- **Convergence Speed:** 
    - **Value Iteration** took **142 iterations** to converge to within $\theta = 10^{-6}$.
    - **Policy Iteration** took only **2 iterations** to stabilize the optimal policy.
- **Explanation:** 
    - Policy Iteration (PI) operates in the finite space of deterministic policies ($2^3 = 8$ possible policies in this case). Since each improvement step is guaranteed to not decrease the value and there are finitely many policies, it converges very rapidly.
    - Value Iteration (VI) operates in the continuous space of value functions. It approaches the optimal value function $V^*$ asymptotically, requiring many sweeps to drop below the convergence threshold $\theta$.

### 4.2 Convergence Behavior
- **Trend:** $V(s)$ increases monotonically across iterations for all states. This is expected as the Bellman updates propagate the rewards (mostly positive) throughout the state space.
- **Update Difference:**
    - **Policy Evaluation** updates use a fixed action $\pi(s)$, following a linear system of equations.
    - **Value Iteration** uses the max operator ($\max_a Q(s,a)$), which makes the update non-linear and focused on finding the upper bound of the Bellman equation directly.

### 4.3 Optimal Policy Interpretation
- **Optimal Policy:**
    - `High` → **Search**
    - `Low` → **Search**
    - `Charging` → **Wait**
- **Intuition:** 
    - **High:** Searching has high immediate reward (+4) and high probability (0.7) of staying High.
    - **Low:** Searching has a mix of +4 and -3 rewards, but leads back to High or stays Low. Waiting only gives +1. The long-term discounted rewards of Search outweigh the risk/penalty.
    - **Charging:** Search is not allowed, so **Wait** is the only logical choice. It transitions back to `High` with 0 immediate reward but opens up high future rewards.

### 4.4 Practical Insight
- Such a policy is useful for real-world battery-powered robots because it balances **productivity** (searching for trash/cans) with **sustainability** (recharging). The policy tells the robot exactly when the "risk" of operation at low battery is worth the payoff, and defines a clear path to recovery (Charging -> High).
