import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Set page styles
st.markdown("""
<style>
    .section-box {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1rem;
    }
    .input-area {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        border: 2px solid #e9ecef;
    }
    .result-area {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        border: 2px solid #667eea;
    }
    /* Remove default Streamlit containers that cause extra white boxes */
    .stMarkdown {
        margin: 0 !important;
        padding: 0 !important;
    }
    .stMarkdown > div {
        margin: 0 !important;
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

def dijkstra(graph, start):
    """Dijkstra's algorithm for shortest path."""
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    
    for _ in range(n):
        # Find node with minimum distance
        min_dist = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i
        
        if u == -1:
            break
        
        visited[u] = True
        
        # Update neighbors
        for v in range(n):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
    
    return distances

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **Dijkstra's Algorithm** is a classic algorithm used to find the shortest path from a single source in a graph.
    
    **Core Idea**: Using a greedy strategy, each time select the unvisited node with the shortest distance from the start, then update the distances of its neighbor nodes.
    
    **Basic Steps**:
    1. Initialize distance array, set distance to start node as 0, others as infinity
    2. Repeat the following steps:
       - Select the unvisited node with the shortest distance from the start
       - Mark this node as visited
       - Update the distances of its neighbor nodes
    3. Until all nodes are visited or no more progress can be made
    
    **Key Concepts**:
    - **Single-source Shortest Path**: Shortest paths from one start node to all other nodes
    - **Greedy Algorithm**: Making locally optimal choices at each step
    - **Priority Queue**: Used to efficiently select the node with the shortest distance
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Map Navigation**：Calculating shortest routes
    - **Network Routing**：Packet routing algorithms
    - **Traffic Planning**：Optimal route planning
    - **Game Development**：AI pathfinding
    - **Network Analysis**：Shortest paths in social networks
    
    **Advantages**：
    - High efficiency, time complexity of O(V²), can be optimized to O(E log V) with priority queue
    - Simple implementation, clear logic
    - Suitable for both directed and undirected graphs
    
    **Disadvantages**：
    - Cannot handle negative weight edges
    - Time complexity may be high for large graphs
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Construct Graph**：Represent the graph using adjacency matrix or adjacency list
    2. **Initialize**：Set the start node and initialize the distance array
    3. **Select Node**：Choose the unvisited node with the smallest current distance
    4. **Update Distances**：Update the distances of all neighbors of this node
    5. **Mark Visited**：Mark this node as visited
    6. **Repeat**：Until all nodes are visited
    7. **Output Result**：Obtain the shortest distances from the start to all other nodes
    
    **Notes**：
    - The graph should not have negative weight edges
    - For large graphs, using a priority queue is recommended for optimization
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 4. Interactive Code Example
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💻 Interactive Code Example</div>', unsafe_allow_html=True)
    
    col_code, col_input, col_result = st.columns([2, 1, 2])
    
    with col_code:
        st.markdown("**Code Section**")
        code_template = '''"""
Requirements:
- Python 3.7+
- NumPy: pip install numpy
- Matplotlib: pip install matplotlib
- NetworkX: pip install networkx
"""

import numpy as np

def dijkstra(graph, start):
    """Dijkstra's algorithm for shortest path."""
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    
    for _ in range(n):
        # Find node with minimum distance
        min_dist = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i
        
        if u == -1:
            break
        
        visited[u] = True
        
        # Update neighbors
        for v in range(n):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
    
    return distances

# Define graph as adjacency matrix
graph = REPLACE_1  # Adjacency matrix
start_node = REPLACE_2  # Start node

# Run Dijkstra's algorithm
distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for i, dist in enumerate(distances):
    print(f"Node {i}: {dist}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Adjacency Matrix**")
        input_graph = st.text_area("", value="0, 4, 0, 0, 0, 0, 0, 8, 0; 4, 0, 8, 0, 0, 0, 0, 11, 0; 0, 8, 0, 7, 0, 4, 0, 0, 2; 0, 0, 7, 0, 9, 14, 0, 0, 0; 0, 0, 0, 9, 0, 10, 0, 0, 0; 0, 0, 4, 14, 10, 0, 2, 0, 0; 0, 0, 0, 0, 0, 2, 0, 1, 6; 8, 11, 0, 0, 0, 0, 1, 0, 7; 0, 0, 2, 0, 0, 0, 6, 7, 0", key="dijkstra_graph")
        
        st.write("**Input 2: Start Node**")
        input_start = st.number_input("", value=0, min_value=0, step=1, key="dijkstra_start")
        
        run_button = st.button("▶ Run Code", type="primary", key="dijkstra_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Parse input graph
                rows = [row.strip() for row in input_graph.split(";") if row.strip()]
                graph = []
                for row in rows:
                    elements = [int(e.strip()) for e in row.split(",") if e.strip()]
                    graph.append(elements)
                graph = np.array(graph)
                
                if graph.shape[0] != graph.shape[1]:
                    st.error("Adjacency matrix must be square")
                else:
                    # Run Dijkstra's algorithm
                    distances = dijkstra(graph, int(input_start))
                    
                    st.markdown('<div class="result-area">', unsafe_allow_html=True)
                    st.write(f"**Start Node**: {int(input_start)}")
                    st.write("**Shortest Distances**:")
                    for i, dist in enumerate(distances):
                        st.write(f"Node {i}: {dist}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Visualization
                    G = nx.Graph()
                    n = len(graph)
                    
                    # Add nodes
                    for i in range(n):
                        G.add_node(i)
                    
                    # Add edges
                    for i in range(n):
                        for j in range(i+1, n):
                            if graph[i][j] > 0:
                                G.add_edge(i, j, weight=graph[i][j])
                    
                    # Position nodes
                    pos = nx.spring_layout(G, seed=42)
                    
                    # Draw graph
                    fig, ax = plt.subplots(figsize=(10, 6))
                    
                    # Draw nodes
                    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='#667eea', ax=ax)
                    
                    # Draw edges
                    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray', ax=ax)
                    
                    # Draw labels
                    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
                    
                    # Draw edge labels
                    edge_labels = nx.get_edge_attributes(G, 'weight')
                    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
                    
                    # Highlight start node
                    nx.draw_networkx_nodes(G, pos, nodelist=[int(input_start)], node_size=700, node_color='#764ba2', ax=ax)
                    
                    ax.set_title(f'Dijkstra\'s Algorithm - Start Node {int(input_start)}', fontsize=14, fontweight='bold', pad=20)
                    ax.axis('off')
                    
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
