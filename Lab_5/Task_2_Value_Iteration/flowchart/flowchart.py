import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
from graphviz import Digraph

def generate_value_iteration_flowchart():
    # Create a new directed graph
    dot = Digraph(comment='Value Iteration Algorithm', format='png')
    dot.attr(rankdir='TB', size='8,10', fontname='Helvetica')
    
    # Node styling
    dot.attr('node', shape='box', style='filled', fillcolor='#F0F0F0', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica')

    # --- DEFINE NODES ---
    dot.node('Start', 'Start', shape='oval', fillcolor='#87CEEB')
    dot.node('Init', 'Initialize V(s) = 0\nfor all s ∈ S', fillcolor='#E6E6FA')
    
    dot.node('LoopStart', 'Begin Update Sweep\n(New Iteration)', shape='rectangle')
    dot.node('BellmanOpt', 'For each state s:\nV(s) ← max_a Σ P(s\'|s,a) [R(s,a,s\') + γV(s\')]', fillcolor='#FFD700')
    
    dot.node('CheckConv', 'Is max|V_new - V_old| < θ?', shape='diamond', fillcolor='#FFDAB9')
    dot.node('Extract', 'Extract Optimal Policy π*\nπ*(s) = argmax_a Q(s,a)', fillcolor='#DDA0DD')
    dot.node('End', 'End\nReturn V* and π*', shape='oval', fillcolor='#90EE90')

    # --- DEFINE EDGES ---
    dot.edge('Start', 'Init')
    dot.edge('Init', 'LoopStart')
    dot.edge('LoopStart', 'BellmanOpt')
    dot.edge('BellmanOpt', 'CheckConv')
    
    dot.edge('CheckConv', 'Extract', label=' YES')
    dot.edge('CheckConv', 'LoopStart', label=' NO')
    dot.edge('Extract', 'End')

    # --- RENDER ---
    output_dir = os.path.dirname(__file__)
    output_path = os.path.join(output_dir, 'value_iteration_flow')
    dot.render(output_path, view=False, cleanup=True)
    print(f"Flowchart generated successfully as '{output_path}.png'!")

if __name__ == '__main__':
    generate_value_iteration_flowchart()
