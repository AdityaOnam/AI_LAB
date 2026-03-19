import collections
import itertools
import heapq
import math

# ==========================================
# --- PARSING & GRAPH SETUP (From Task 1) ---
# ==========================================
def parse_input(input_lines):
    food_costs = {}
    group_size = 1
    assignments = {} 
    
    for line in input_lines:
        parts = line.strip().split()
        if not parts: continue
        if parts[0] == 'C':
            food_costs[parts[1]] = int(parts[2])
        elif parts[0] == 'G':
            group_size = int(parts[1])
        elif parts[0] == 'A':
            a_id = 'A' + parts[1]
            in1, in2 = int(parts[2]), int(parts[3])
            outcome = int(parts[4])
            food = parts[5]
            assignments[a_id] = {'inputs': [in1, in2], 'outcome': outcome, 'food': food}
            
    outcome_to_assignment = {data['outcome']: a_id for a_id, data in assignments.items()}
    
    graph = collections.defaultdict(list)
    prereqs = collections.defaultdict(list)
    
    for a_id, data in assignments.items():
        for inp in data['inputs']:
            if inp in outcome_to_assignment:
                prereq_id = outcome_to_assignment[inp]
                graph[prereq_id].append(a_id)
                prereqs[a_id].append(prereq_id)
                
    return assignments, graph, prereqs, food_costs, group_size

def calculate_leaf_depths(assignments, graph):
    """Calculates the longest path from each node to a leaf for the heuristic."""
    depths = {}
    def get_depth(node):
        if node in depths: 
            return depths[node]
        if not graph[node]:
            depths[node] = 1
            return 1
        depths[node] = 1 + max(get_depth(neighbor) for neighbor in graph[node])
        return depths[node]
        
    for a in assignments:
        get_depth(a)
    return depths


# ==========================================
# --- A* SEARCH IMPLEMENTATION (Task 2) ---
# ==========================================
def menu_cost(menu_counts, food_costs):
    return sum(count * food_costs[food] for food, count in menu_counts.items())

def is_dominated(day, menu, pareto_front, food_keys):
    for (v_day, v_menu) in pareto_front:
        if v_day <= day:
            if all(v_menu.get(f, 0) <= menu.get(f, 0) for f in food_keys):
                return True
    return False

def astar_schedule(assignments, graph, prereqs, food_costs, group_size):
    all_tasks = set(assignments.keys())
    food_keys = list(food_costs.keys())
    depths = calculate_leaf_depths(assignments, graph)
    
    pq = []
    tie_breaker = 0
    
    initial_completed = frozenset()
    initial_menu = {f: 0 for f in food_keys}
    initial_menu_tuple = tuple(initial_menu[f] for f in food_keys)
    
    heapq.heappush(pq, (0, 0, tie_breaker, 0, initial_completed, initial_menu_tuple, []))
    
    visited = collections.defaultdict(list)
    states_explored = 0
    
    while pq:
        f_score, g_score, _, current_day, completed, menu_tuple, schedule = heapq.heappop(pq)
        states_explored += 1
        
        current_max_menu = {f: menu_tuple[i] for i, f in enumerate(food_keys)}
        
        # GOAL CHECK
        if len(completed) == len(all_tasks):
            final_cost = current_day * menu_cost(current_max_menu, food_costs)
            return schedule, current_max_menu, current_day, final_cost, states_explored
            
        available = []
        for task in all_tasks:
            if task not in completed:
                if all(p in completed for p in prereqs[task]):
                    available.append(task)
                    
        max_subset_size = min(group_size, len(available))
        for size in range(1, max_subset_size + 1):
            for daily_tasks in itertools.combinations(available, size):
                
                new_completed = completed.union(daily_tasks)
                new_day = current_day + 1
                
                today_menu_counts = collections.Counter([assignments[t]['food'] for t in daily_tasks])
                new_max_menu = {}
                for f in food_keys:
                    new_max_menu[f] = max(current_max_menu.get(f, 0), today_menu_counts.get(f, 0))
                
                if is_dominated(new_day, new_max_menu, visited[new_completed], food_keys):
                    continue
                visited[new_completed].append((new_day, new_max_menu))
                
                current_menu_cst = menu_cost(new_max_menu, food_costs)
                new_g = new_day * current_menu_cst
                
                uncompleted = all_tasks - new_completed
                if uncompleted:
                    min_days_by_volume = math.ceil(len(uncompleted) / group_size)
                    min_days_by_depth = max(depths[t] for t in uncompleted)
                    predicted_additional_days = max(min_days_by_volume, min_days_by_depth)
                else:
                    predicted_additional_days = 0
                    
                new_h = predicted_additional_days * current_menu_cst
                new_f = new_g + new_h
                
                new_menu_tuple = tuple(new_max_menu[f] for f in food_keys)
                new_schedule = schedule + [list(daily_tasks)]
                
                tie_breaker += 1
                heapq.heappush(pq, (new_f, new_g, tie_breaker, new_day, new_completed, new_menu_tuple, new_schedule))

    return None, None, 0, 0, states_explored

# ==========================================
# --- GREEDY ALGORITHM (For Comparison) ---
# ==========================================
def greedy_schedule(assignments, prereqs, food_costs, group_size):
    """A basic Greedy algorithm to compare against the A* optimal."""
    all_tasks = set(assignments.keys())
    completed = set()
    schedule = []
    
    while len(completed) < len(all_tasks):
        available = []
        for task in all_tasks:
            if task not in completed:
                if all(p in completed for p in prereqs[task]):
                    available.append(task)
        
        # Greedy Choice: Sort alphabetically, grab up to Group Size
        available.sort()
        daily_tasks = available[:group_size]
        schedule.append(daily_tasks)
        completed.update(daily_tasks)
        
    # Calculate costs using the same logic as A* for a fair comparison
    food_keys = list(food_costs.keys())
    max_menu = {f: 0 for f in food_keys}
    
    for day_tasks in schedule:
        today_counts = collections.Counter([assignments[t]['food'] for t in day_tasks])
        for f in food_keys:
            max_menu[f] = max(max_menu.get(f, 0), today_counts.get(f, 0))
            
    total_days = len(schedule)
    total_cost = total_days * menu_cost(max_menu, food_costs)
    
    return schedule, total_days, total_cost

# ==========================================
# --- OUTPUT FORMATTING & EXECUTION --------
# ==========================================
def format_menu(menu_dict):
    return "<" + ", ".join([f"{count} {food}" for food, count in menu_dict.items() if count > 0]) + ">"

def run_task_2_comparison(input_text, instance_name):
    lines = input_text.strip().split('\n')
    assignments, graph, prereqs, food_costs, group_size = parse_input(lines)
    
    print(f"\n==========================================")
    print(f" RUNNING INSTANCE: {instance_name}")
    print(f"==========================================")
    
    # 1. Run Greedy
    print("\n[1] Running Greedy Algorithm Baseline...")
    greedy_sch, greedy_days, greedy_cost = greedy_schedule(assignments, prereqs, food_costs, group_size)
    
    # 2. Run A*
    print("[2] Executing A* Search (Finding optimal)...")
    opt_schedule, opt_menu, opt_days, opt_cost, states = astar_schedule(assignments, graph, prereqs, food_costs, group_size)
    
    # 3. Required Outputs
    print(f"\n--- REQUIRED OUTPUT FOR TASK 2 ---")
    print(f"Total States Explored: {states}\n")
    
    print("Day-by-Day Assignment List & Daily Menus:")
    for day, tasks in enumerate(opt_schedule, 1):
        # Calculate daily isolated cost
        day_counts = collections.Counter([assignments[t]['food'] for t in tasks])
        day_cost = menu_cost(day_counts, food_costs)
        print(f"  Day {day}: {', '.join(tasks)} ")
        print(f"         Daily Menu: {format_menu(day_counts)} | Daily Cost: {day_cost}")
        
    print(f"\nGlobal Max Menu Required: {format_menu(opt_menu)}")
    
    print(f"\n>>> OPTIMAL A* SUMMARY <<<")
    print(f"Total Days: {opt_days}")
    print(f"Total Food Cost: {opt_cost}")
    
    print(f"\n>>> COMPARISON WITH GREEDY <<<")
    print(f"Greedy Cost: {greedy_cost} | A* Cost: {opt_cost}  -> Cost Savings: {greedy_cost - opt_cost}")
    print(f"Greedy Days: {greedy_days} | A* Days: {opt_days}  -> Day Difference: {greedy_days - opt_days}")
    print("==========================================\n")

# ==========================================
# --- 3 TEST INSTANCES ---------------------
# ==========================================

# Instance 1: The original sample provided
INSTANCE_1 = """
C TC 1
C DF 1
C PM 1
C GJ 1
G 2
A 1 1 3 7 TC
A 2 4 2 8 TC
A 3 1 3 9 TC
A 4 2 3 10 PM
A 5 7 8 11 TC
A 6 4 6 12 TC
A 7 6 9 13 PM
A 8 10 5 14 GJ
A 9 1 11 15 DF
A 10 3 12 16 TC
A 11 15 16 17 DF
"""

# Instance 2: A small, linear pipeline (to test depth constraints)
INSTANCE_2 = """
C Pizza 5
C Burger 3
C Salad 2
G 2
A 1 0 0 10 Pizza
A 2 10 0 20 Burger
A 3 20 0 30 Salad
A 4 30 0 40 Pizza
A 5 40 0 50 Burger
"""

# Instance 3: A wider tree with highly variable food costs (tests parallel scheduling)
INSTANCE_3 = """
C Steak 10
C Soup 2
C Bread 1
G 3
A 1 0 0 10 Soup
A 2 0 0 20 Bread
A 3 0 0 30 Soup
A 4 10 20 40 Steak
A 5 20 30 50 Steak
A 6 40 50 60 Soup
A 7 40 50 70 Bread
"""

# ==========================================
# --- MENU DRIVEN CLI ----------------------
# ==========================================
def main():
    while True:
        print("\n=== SCHEDULING ALGORITHM MENU ===")
        print("1. Run Instance 1 (Original PDF Sample)")
        print("2. Run Instance 2 (Linear Pipeline)")
        print("3. Run Instance 3 (Wide Tree/Parallel)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            run_task_2_comparison(INSTANCE_1, "Instance 1 (Original)")
        elif choice == '2':
            run_task_2_comparison(INSTANCE_2, "Instance 2 (Linear)")
        elif choice == '3':
            run_task_2_comparison(INSTANCE_3, "Instance 3 (Wide Tree)")
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()