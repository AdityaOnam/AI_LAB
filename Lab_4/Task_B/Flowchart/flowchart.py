from graphviz import Digraph

def generate_astar_partial_tree():
    # Create the directed graph
    dot = Digraph(comment='Partial A* Search Tree (Level 1)', format='png')
    dot.attr(rankdir='TB', size='10,12', fontname='Helvetica')
    
    # Global node styling
    dot.attr('node', fontname='Helvetica', fontsize='11', style='filled', shape='box', rounded='true')
    dot.attr('edge', fontname='Helvetica', fontsize='10')

    # --- NODES ---
    
    # ROOT NODE
    dot.node('root', 'ROOT STATE (Day 0)\nCompleted: None\nMenu Cost: $0\ng(n)=0 | h(n)=0\nf(n) = 0', fillcolor='#f8f9fa')

    # GOOD CHILD (Grouping TC and TC)
    dot.node('child_good', 'CHILD STATE (Day 1)\nSchedule: [A1, A2]\nMenu: 1 TC (Cost $1)\nRemaining Tasks: 9 (Min 5 days)\ng(n) = 1 day * $1 = $1\nh(n) = 5 days * $1 = $5\nf(n) = 6', fillcolor='#d4edda')

    # BAD CHILD (Mixing TC and PM)
    dot.node('child_bad', 'CHILD STATE (Day 1)\nSchedule: [A1, A4]\nMenu: 1 TC, 1 PM (Cost $2)\nRemaining Tasks: 9 (Min 5 days)\ng(n) = 1 day * $2 = $2\nh(n) = 5 days * $2 = $10\nf(n) = 12', fillcolor='#f8d7da')
    
    # ANOTHER CHILD (Doing only 1 task)
    dot.node('child_single', 'CHILD STATE (Day 1)\nSchedule: [A1]\nMenu: 1 TC (Cost $1)\nRemaining Tasks: 10 (Min 5 days)\ng(n) = 1 day * $1 = $1\nh(n) = 5 days * $1 = $5\nf(n) = 6', fillcolor='#fff3cd')

    # Explanatory Note
    dot.node('note', '... 12 more branches\ngenerated just for Day 1 ...\n\nA* will pull the green node\nnext because f(n)=6 is the lowest.', shape='note', style='dashed, filled', fillcolor='white')

    # --- EDGES ---
    dot.edge('root', 'child_good', label=' Branch: A1 & A2', color='darkgreen', fontcolor='darkgreen')
    dot.edge('root', 'child_bad', label=' Branch: A1 & A4', color='red', fontcolor='red')
    dot.edge('root', 'child_single', label=' Branch: A1 only', color='orange', fontcolor='orange')
    
    # Dotted line to the note
    dot.edge('root', 'note', style='dotted', arrowhead='none')

    # --- RENDER ---
    dot.render('astar_partial_tree', view=True)
    print("Graph generated successfully as 'astar_partial_tree.png'!")

if __name__ == '__main__':
    generate_astar_partial_tree()