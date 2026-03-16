import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

def plot_tree(node, x, y, dx, ax):
    if node is None:
        return
    
    ax.scatter(x, y, s=800, color='#667eea', edgecolors='white', linewidths=2, zorder=5)
    ax.text(x, y, str(node.key), ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    
    if node.left:
        ax.plot([x, x-dx], [y-1, y-2], 'k-', linewidth=2, alpha=0.6)
        plot_tree(node.left, x-dx, y-2, dx/2, ax)
    
    if node.right:
        ax.plot([x, x+dx], [y-1, y-2], 'k-', linewidth=2, alpha=0.6)
        plot_tree(node.right, x+dx, y-2, dx/2, ax)

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **Binary Search Tree (BST)** is a special type of binary tree data structure.
    
    **Core Properties**:
    - All nodes in the left subtree have values **less than** the root node's value
    - All nodes in the right subtree have values **greater than** the root node's value
    - Both left and right subtrees must also be binary search trees
    
    **Key Concepts**:
    - **Root**: The top node of the tree
    - **Leaf**: Nodes with no children
    - **Depth**: The distance from a node to the root
    - **Inorder Traversal**: Traversing left-root-right, results in a sorted sequence
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Dynamic Searching**：Scenarios requiring frequent insertion, deletion, and searching
    - **Sorting**：Inorder traversal directly yields a sorted sequence
    - **Range Queries**：Quickly finding all elements within a certain range
    - **Database Indexing**：Used as a data structure for database indexes
    
    **Advantages**：
    - Average time complexity of O(log n) for search, insertion, and deletion
    - Simple implementation, clear logic
    - Supports ordered traversal
    
    **Disadvantages**：
    - In the worst case (e.g., inserting sorted data), it degenerates into a linked list with O(n) complexity
    - Requires balancing operations (AVL tree, Red-Black tree) to solve the degeneration problem
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Create Empty Tree**：Initialize an empty binary search tree
    2. **Insert Node**：
       - Start comparing from the root node
       - If less than current node, go left; if greater, go right
       - Find an empty position and insert the new node
    3. **Search Node**：
       - Start comparing from the root node
       - If equal, found; if less, go left; if greater, go right
       - Reaching an empty node means not found
    4. **Traverse Tree**：Inorder traversal yields a sorted sequence
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
- Matplotlib: pip install matplotlib
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

# Create BST and insert values
bst = BinarySearchTree()
values = [REPLACE_1]  # List of values to insert
for v in values:
    bst.insert(v)

# Search for a value
search_key = REPLACE_2  # Value to search
found = bst.search(search_key)

print(f"Inorder traversal: {bst.inorder()}")
print(f"Search {search_key}: {'Found' if found else 'Not found'}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Insert Values List**")
        input_values = st.text_input("", value="50, 30, 70, 20, 40, 60, 80", key="bst_values")
        
        st.write("**Input 2: Search Value**")
        input_search = st.number_input("", value=40, step=1, key="bst_search")
        
        run_button = st.button("▶ Run Code", type="primary", key="bst_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Parse input values
                values = [int(v.strip()) for v in input_values.split(",") if v.strip()]
                
                # Create BST
                bst = BinarySearchTree()
                for v in values:
                    bst.insert(v)
                
                # Search
                found = bst.search(input_search)
                
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write(f"**Inserted Values**: {values}")
                st.write(f"**Inorder Traversal**: {bst.inorder()}")
                st.write(f"**Search {input_search}**: {'✅ Found' if found else '❌ Not found'}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization
                if bst.root:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax.set_xlim(-5, 5)
                    ax.set_ylim(-6, 1)
                    ax.axis('off')
                    plot_tree(bst.root, 0, 0, 3, ax)
                    ax.set_title('Binary Search Tree Visualization', fontsize=14, fontweight='bold', pad=20)
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
