import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
from graphviz import Digraph

def generate_policy_evaluation_flowchart():
    # Create a new directed graph
    dot = Digraph(comment='Policy Evaluation Algorithm', format='png')
    dot.attr(rankdir='TB', size='8,10', fontname='Helvetica')
    
    # Node styling
    dot.attr('node', shape='box', style='filled', fillcolor='#F0F0F0', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica')

    # --- DEFINE NODES ---
    dot.node('Start', 'Start', shape='oval', fillcolor='#87CEEB')
    dot.node('Init', 'Initialize V(s) = 0\nfor all s ∈ S\nSpecify Policy π', fillcolor='#E6E6FA')
    
    dot.node('LoopStart', 'Begin Update Sweep\n(New Iteration)', shape='rectangle')
    dot.node('Bellman', 'For each state s:\nV(s) ← Σ P(s\'|s,π(s)) [R(s,π(s)) + γV(s\')]', fillcolor='#FFFACD')
    
    dot.node('CheckConv', 'Is max|V_new - V_old| < θ?', shape='diamond', fillcolor='#FFDAB9')
    dot.node('End', 'End\nReturn Converged V', shape='oval', fillcolor='#90EE90')

    # --- DEFINE EDGES ---
    dot.edge('Start', 'Init')
    dot.edge('Init', 'LoopStart')
    dot.edge('LoopStart', 'Bellman')
    dot.edge('Bellman', 'CheckConv')
    
    dot.edge('CheckConv', 'End', label=' YES')
    dot.edge('CheckConv', 'LoopStart', label=' NO')

    # --- RENDER ---
    output_dir = os.path.dirname(__file__)
    output_path = os.path.join(output_dir, 'policy_evaluation_flow')
    dot.render(output_path, view=False, cleanup=True)
    print(f"Flowchart generated successfully as '{output_path}.png'!")

if __name__ == '__main__':
    generate_policy_evaluation_flowchart()
