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

class KMeans:
    def __init__(self, k=3, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = None
        self.labels = None
    
    def fit(self, X):
        # Initialize centroids randomly
        np.random.seed(42)
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iterations):
            # Assign each data point to the nearest centroid
            self.labels = self._assign_clusters(X)
            
            # Calculate new centroids
            new_centroids = np.array([X[self.labels == i].mean(axis=0) for i in range(self.k)])
            
            # Check convergence
            if np.allclose(self.centroids, new_centroids):
                break
            
            self.centroids = new_centroids
    
    def _assign_clusters(self, X):
        labels = []
        for x in X:
            distances = np.sqrt(np.sum((x - self.centroids) ** 2, axis=1))
            labels.append(np.argmin(distances))
        return np.array(labels)

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **K-means Clustering** is a classic unsupervised learning algorithm.
    
    **Core Idea**: Partition n data points into k clusters, such that data points within a cluster are similar, while data points between clusters are dissimilar.
    
    **Basic Steps**:
    1. Randomly initialize k cluster centroids
    2. Assign each data point to the nearest centroid
    3. Calculate new centroids for each cluster (averages)
    4. Repeat steps 2 and 3 until convergence
    
    **Key Concepts**:
    - **Cluster**: A collection of similar data points
    - **Centroid**: The center point of each cluster
    - **Distance Metric**: Typically Euclidean distance
    - **Convergence**: Centroids no longer change significantly
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Data Grouping**：Grouping similar data for analysis
    - **Market Segmentation**：Dividing markets based on user behavior
    - **Image Segmentation**：Clustering image pixels by color
    - **Anomaly Detection**：Identifying outliers
    - **Dimensionality Reduction Visualization**：Mapping high-dimensional data to low-dimensional space
    
    **Advantages**：
    - Simple algorithm, easy to implement
    - High computational efficiency
    - Suitable for large-scale data
    
    **Disadvantages**：
    - Need to specify k value in advance
    - Sensitive to initial centroid positions
    - Sensitive to outliers
    - Can only discover spherical clusters
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Select k value**：Determine based on domain knowledge or using elbow method
    2. **Prepare data**：Standardize data to avoid scale issues
    3. **Initialize centroids**：Randomly select k data points as initial centroids
    4. **Assign data points**：Assign each point to the nearest centroid
    5. **Update centroids**：Calculate new centroids for each cluster
    6. **Repeat**：Until centroids no longer change significantly
    7. **Analyze results**：Evaluate clustering quality, adjust parameters
    
    **Notes**：
    - Data needs to be standardized
    - May need multiple runs to get stable results
    - For non-spherical clusters, consider other algorithms
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

import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = None
        self.labels = None
    
    def fit(self, X):
        # Initialize centroids randomly
        np.random.seed(42)
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iterations):
            # Assign each data point to the nearest centroid
            self.labels = self._assign_clusters(X)
            
            # Calculate new centroids
            new_centroids = np.array([X[self.labels == i].mean(axis=0) for i in range(self.k)])
            
            # Check convergence
            if np.allclose(self.centroids, new_centroids):
                break
            
            self.centroids = new_centroids
    
    def _assign_clusters(self, X):
        labels = []
        for x in X:
            distances = np.sqrt(np.sum((x - self.centroids) ** 2, axis=1))
            labels.append(np.argmin(distances))
        return np.array(labels)

# Generate sample data
np.random.seed(42)
X = np.vstack([
    np.random.randn(REPLACE_1, 2) + np.array([2, 2]),  # Cluster 1
    np.random.randn(REPLACE_2, 2) + np.array([-2, -2]),  # Cluster 2
    np.random.randn(REPLACE_3, 2) + np.array([2, -2])   # Cluster 3
])

# Run K-means
kmeans = KMeans(k=3, max_iterations=100)
kmeans.fit(X)

print(f"Cluster centroids: {kmeans.centroids}")
print(f"Number of points in each cluster: {np.bincount(kmeans.labels)}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Cluster 1 Sample Count**")
        input_cluster1 = st.number_input("Cluster 1 Sample Count", value=100, min_value=50, max_value=200, step=10, key="kmeans_cluster1")
        
        st.write("**Input 2: Cluster 2 Sample Count**")
        input_cluster2 = st.number_input("Cluster 2 Sample Count", value=100, min_value=50, max_value=200, step=10, key="kmeans_cluster2")
        
        st.write("**Input 3: Cluster 3 Sample Count**")
        input_cluster3 = st.number_input("Cluster 3 Sample Count", value=100, min_value=50, max_value=200, step=10, key="kmeans_cluster3")
        
        run_button = st.button("▶ Run Code", type="primary", key="kmeans_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Generate data
                np.random.seed(42)
                X = np.vstack([
                    np.random.randn(int(input_cluster1), 2) + np.array([2, 2]),
                    np.random.randn(int(input_cluster2), 2) + np.array([-2, -2]),
                    np.random.randn(int(input_cluster3), 2) + np.array([2, -2])
                ])
                
                # Run K-means
                kmeans = KMeans(k=3, max_iterations=100)
                kmeans.fit(X)
                
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write(f"**Total Samples**: {len(X)}")
                st.write(f"**Samples per Cluster**: {np.bincount(kmeans.labels)}")
                st.write(f"**Cluster Centroids**: {kmeans.centroids}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization
                fig, ax = plt.subplots(figsize=(10, 6))
                colors = ['#667eea', '#764ba2', '#f093fb']
                
                for i in range(3):
                    ax.scatter(X[kmeans.labels == i, 0], X[kmeans.labels == i, 1], 
                              c=colors[i], s=100, alpha=0.6, label=f'Cluster {i+1}')
                
                # Plot centroids
                ax.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], 
                          c='black', s=300, marker='*', edgecolors='white', linewidths=2, label='Centroids')
                
                ax.set_xlabel('Feature 1')
                ax.set_ylabel('Feature 2')
                ax.set_title('K-means Clustering', fontsize=14, fontweight='bold', pad=20)
                ax.legend()
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
