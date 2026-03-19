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

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If key doesn't exist, add it
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
    def display(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Bucket {i}: {bucket}")
        return result

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **Hash Table** is an efficient key-value pair storage data structure.
    
    **Core Idea**: Using a hash function to map keys to array index positions, achieving average O(1) time complexity for insert, search, and delete operations.
    
    **Basic Principles**:
    1. **Hash Function**: Converts keys of any length to fixed-length hash values
    2. **Hash Collision**: Different keys may map to the same index position
    3. **Collision Resolution**: Common methods include chaining (linked lists) and open addressing
    
    **Key Concepts**:
    - **Bucket**: A position in the hash table used to store key-value pairs
    - **Load Factor**: Ratio of stored elements to hash table size
    - **Hash Collision**: Situation where different keys produce the same hash value
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Data requiring fast lookup**：Caches, dictionaries, symbol tables
    - **Database indexing**：Accelerating data queries
    - **Cache systems**：Browser caches, CPU caches
    - **Counters**：Word frequency statistics
    - **Set operations**：Deduplication, intersection, union
    
    **Advantages**：
    - Average O(1) time complexity
    - Simple implementation, easy to use
    - Suitable for large-scale data
    
    **Disadvantages**：
    - Need to handle hash collisions
    - May have low space utilization
    - Hash function selection affects performance
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Initialization**：Create a hash table with fixed size
    2. **Insertion**：Calculate key's index via hash function, then store key-value pair
    3. **Search**：Calculate key's index via hash function, then search in corresponding bucket
    4. **Deletion**：Calculate key's index via hash function, then remove from corresponding bucket
    5. **Resizing**：When load factor is too high, need to resize to maintain performance
    
    **Notes**：
    - Choose appropriate hash function to reduce collisions
    - Set initial size appropriately to balance space and time
    - Pay attention to handling hash collisions
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
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If key doesn't exist, add it
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False

# Create hash table
table = HashTable(size=REPLACE_1)  # Hash table size

# Insert key-value pairs
pairs = REPLACE_2  # List of (key, value) pairs
for key, value in pairs:
    table.insert(key, value)

# Search for a key
search_key = REPLACE_3  # Key to search
result = table.search(search_key)

print(f"Search result for {search_key}: {result}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Hash Table Size**")
        input_size = st.number_input("", value=10, min_value=5, max_value=20, step=1, key="hash_size")
        
        st.write("**Input 2: Key-Value Pairs**")
        input_pairs = st.text_area("", value="apple, 1; banana, 2; orange, 3; grape, 4; cherry, 5", key="hash_pairs")
        
        st.write("**Input 3: Search Key**")
        input_search = st.text_input("", value="banana", key="hash_search")
        
        run_button = st.button("▶ Run Code", type="primary", key="hash_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Parse input pairs
                pairs = []
                for pair in input_pairs.split(";"):
                    if pair.strip():
                        key, value = pair.split(",")
                        pairs.append((key.strip(), int(value.strip())))
                
                # Create hash table
                table = HashTable(size=int(input_size))
                for key, value in pairs:
                    table.insert(key, value)
                
                # Search
                result = table.search(input_search)
                
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write(f"**Hash Table Size**: {int(input_size)}")
                st.write(f"**Inserted Key-Value Pairs**: {pairs}")
                st.write(f"**Search Key '{input_search}'**: {'Found value: ' + str(result) if result is not None else 'Not found'}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # Create horizontal bars for each bucket
                bucket_heights = [len(bucket) for bucket in table.table]
                buckets = list(range(len(bucket_heights)))
                
                ax.barh(buckets, bucket_heights, color='#667eea')
                ax.set_xlabel('Number of Elements')
                ax.set_ylabel('Bucket Index')
                ax.set_title('Hash Table Bucket Distribution', fontsize=14, fontweight='bold', pad=20)
                ax.grid(True, alpha=0.3, axis='x')
                
                # Add labels for elements
                for i, bucket in enumerate(table.table):
                    if bucket:
                        labels = [f"{k}:{v}" for k, v in bucket]
                        ax.text(len(bucket) + 0.1, i, f"{labels}", va='center')
                
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
