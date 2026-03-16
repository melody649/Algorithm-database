import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        balance = self.balance_factor(node)
        
        # Left Left case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        
        # Right Right case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        
        # Left Right case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right Left case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
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
    if not node:
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
    **AVL Tree (Adelson-Velsky and Landis Tree)** is a self-balancing binary search tree.
    
    **Core Properties**:
    - The height difference (balance factor) between left and right subtrees does not exceed 1
    - Both left and right subtrees must also be AVL trees
    - Maintains the properties of a binary search tree
    
    **Key Concepts**:
    - **Balance Factor**: Left subtree height minus right subtree height
    - **Rotation Operations**: Using single and double rotations to maintain balance
    - **Self-Balancing**: Automatically adjusts tree structure during insertion and deletion operations
    
    **Rotation Types**:
    - **Left Rotation**: Handles right-right imbalance
    - **Right Rotation**: Handles left-left imbalance
    - **Left-Right Rotation**: Handles left-right imbalance
    - **Right-Left Rotation**: Handles right-left imbalance
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Scenarios requiring O(log n) time complexity**：Search, insertion, and deletion operations
    - **Real-time Systems**：Need to guarantee performance in worst-case scenarios
    - **Database Indexing**：Requires efficient lookup and update operations
    - **Standard implementation of balanced binary search trees**：As a foundation for other data structures
    
    **Advantages**：
    - Strictly balanced, guarantees O(log n) operation time complexity
    - Suitable for scenarios with frequent insertion, deletion, and searching
    - Relatively simple implementation
    
    **Disadvantages**：
    - Insertion and deletion operations require additional rotation operations
    - Higher memory overhead (needs to store height information)
    - For scenarios with frequent insertions and deletions, rotation operations may impact performance
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Create Empty Tree**：Initialize an empty AVL tree
    2. **Insert Node**：
       - Insert according to binary search tree rules
       - Update heights of nodes along the path
       - Calculate balance factors
       - Perform rotation operations if necessary
    3. **Search Node**：Search according to binary search tree rules
    4. **Delete Node**：
       - Delete according to binary search tree rules
       - Update heights of nodes along the path
       - Calculate balance factors
       - Perform rotation operations if necessary
    5. **Traverse Tree**：Inorder traversal yields a sorted sequence
    
    **Notes**：
    - AVL tree balancing operations are handled automatically
    - No need for manual balance adjustments
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
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        balance = self.balance_factor(node)
        
        # Left Left case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        
        # Right Right case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        
        # Left Right case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right Left case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

# Create AVL tree and insert values
avl = AVLTree()
values = REPLACE_1  # List of values to insert
for v in values:
    avl.insert(v)

print(f"Inorder traversal: {avl.inorder()}")
print(f"Tree height: {avl.height(avl.root)}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Insert Values List**")
        input_values = st.text_input("", value="50, 30, 70, 20, 40, 60, 80, 10, 25, 35", key="avl_values")
        
        run_button = st.button("▶ Run Code", type="primary", key="avl_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Parse input values
                values = [int(v.strip()) for v in input_values.split(",") if v.strip()]
                
                # Create AVL tree
                avl = AVLTree()
                for v in values:
                    avl.insert(v)
                
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write(f"**Inserted Values**: {values}")
                st.write(f"**Inorder Traversal**: {avl.inorder()}")
                st.write(f"**Tree Height**: {avl.height(avl.root)}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization
                if avl.root:
                    fig, ax = plt.subplots(figsize=(12, 8))
                    ax.set_xlim(-8, 8)
                    ax.set_ylim(-8, 1)
                    ax.axis('off')
                    plot_tree(avl.root, 0, 0, 4, ax)
                    ax.set_title('AVL Tree Visualization', fontsize=14, fontweight='bold', pad=20)
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
