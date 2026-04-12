import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
from graphviz import Digraph

def generate_policy_iteration_flowchart():
    # Create a new directed graph
    dot = Digraph(comment='Policy Iteration Algorithm', format='png')
    dot.attr(rankdir='TB', size='8,10', fontname='Helvetica')
    
    # Node styling
    dot.attr('node', shape='box', style='filled', fillcolor='#F0F0F0', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica')

    # --- DEFINE NODES ---
    dot.node('Start', 'Start', shape='oval', fillcolor='#87CEEB')
    dot.node('Init', 'Initialize initial policy π\n(e.g., all states take "Wait")', fillcolor='#E6E6FA')
    
    dot.node('Eval', '1. Policy Evaluation\nCompute V^π using iterative updates\nuntil convergence', fillcolor='#B0E0E6')
    dot.node('Improve', '2. Policy Improvement\nExtract new greedy policy π\'\nπ\'(s) = argmax_a Q^π(s,a)', fillcolor='#DDA0DD')
    
    dot.node('CheckStable', 'Is π\' == π?\n(Policy Stable?)', shape='diamond', fillcolor='#FFDAB9')
    dot.node('Update', 'Set π = π\'', fillcolor='#FFFACD')
    dot.node('End', 'End\nReturn Optimal π* and V*', shape='oval', fillcolor='#90EE90')

    # --- DEFINE EDGES ---
    dot.edge('Start', 'Init')
    dot.edge('Init', 'Eval')
    dot.edge('Eval', 'Improve')
    dot.edge('Improve', 'CheckStable')
    
    dot.edge('CheckStable', 'End', label=' YES')
    dot.edge('CheckStable', 'Update', label=' NO')
    dot.edge('Update', 'Eval')

    # --- RENDER ---
    output_dir = os.path.dirname(__file__)
    output_path = os.path.join(output_dir, 'policy_iteration_flow')
    dot.render(output_path, view=False, cleanup=True)
    print(f"Flowchart generated successfully as '{output_path}.png'!")

if __name__ == '__main__':
    generate_policy_iteration_flowchart()
