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

class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None
    
    def fit(self, X):
        # Mean centering
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Covariance matrix
        cov_matrix = np.cov(X_centered.T)
        
        # Eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort eigenvectors by eigenvalues (descending)
        sorted_indices = np.argsort(eigenvalues)[::-1]
        self.components = eigenvectors[:, sorted_indices[:self.n_components]]
    
    def transform(self, X):
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **Principal Component Analysis (PCA)** is a commonly used dimensionality reduction technique.
    
    **Core Idea**: Through linear transformation, project high-dimensional data into a low-dimensional space while preserving the main information of the data.
    
    **Basic Steps**:
    1. Data centering
    2. Calculate covariance matrix
    3. Solve for eigenvalues and eigenvectors of the covariance matrix
    4. Select the top k eigenvectors corresponding to the largest eigenvalues
    5. Project data onto the space formed by these eigenvectors
    
    **Key Concepts**:
    - **Principal Component**: Direction of maximum data variance
    - **Eigenvalue**: Indicates the importance of a principal component
    - **Eigenvector**: Direction of a principal component
    - **Variance Explained**: Proportion of variance explained by each principal component
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Data Dimensionality Reduction**：Reduce feature dimensions, speed up model training
    - **Data Visualization**：Map high-dimensional data to 2D or 3D space
    - **Feature Extraction**：Extract most informative features
    - **Noise Removal**：Remove noise by preserving main components
    - **Data Compression**：Reduce data storage and transmission costs
    
    **Advantages**：
    - Simple algorithm, easy to implement
    - High computational efficiency
    - Strong interpretability
    - Parameter-free learning
    
    **Disadvantages**：
    - Linear dimensionality reduction, may not capture nonlinear relationships
    - Sensitive to data scaling
    - Physical meaning of features may be unclear
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Data Standardization**：Standardize the data
    2. **Calculate Covariance Matrix**：Analyze correlations between features
    3. **Solve for Eigenvalues and Eigenvectors**：Determine principal component directions
    4. **Select Principal Components**：Choose top k components based on eigenvalue magnitude
    5. **Data Projection**：Project original data onto principal component space
    6. **Analyze Results**：Evaluate dimensionality reduction effect, explain principal component meanings
    
    **Notes**：
    - Data needs to be standardized
    - Choose appropriate number of principal components
    - Pay attention to explaining the physical meaning of principal components
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

class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None
    
    def fit(self, X):
        # Mean centering
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Covariance matrix
        cov_matrix = np.cov(X_centered.T)
        
        # Eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort eigenvectors by eigenvalues (descending)
        sorted_indices = np.argsort(eigenvalues)[::-1]
        self.components = eigenvectors[:, sorted_indices[:self.n_components]]
    
    def transform(self, X):
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)

# Generate sample data
np.random.seed(42)
X = np.vstack([
    np.random.randn(REPLACE_1, 2) + np.array([2, 2]),  # Cluster 1
    np.random.randn(REPLACE_2, 2) + np.array([-2, -2])  # Cluster 2
])

# Run PCA
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)

print(f"Original shape: {X.shape}")
print(f"Transformed shape: {X_pca.shape}")
print(f"Components: {pca.components}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Cluster 1 Sample Count**")
        input_cluster1 = st.number_input("", value=100, min_value=50, max_value=200, step=10, key="pca_cluster1")
        
        st.write("**Input 2: Cluster 2 Sample Count**")
        input_cluster2 = st.number_input("", value=100, min_value=50, max_value=200, step=10, key="pca_cluster2")
        
        run_button = st.button("▶ Run Code", type="primary", key="pca_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Generate data
                np.random.seed(42)
                X = np.vstack([
                    np.random.randn(int(input_cluster1), 2) + np.array([2, 2]),
                    np.random.randn(int(input_cluster2), 2) + np.array([-2, -2])
                ])
                
                # Run PCA
                pca = PCA(n_components=2)
                pca.fit(X)
                X_pca = pca.transform(X)
                
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write(f"**Original Data Shape**: {X.shape}")
                st.write(f"**Transformed Shape**: {X_pca.shape}")
                st.write(f"**Principal Components**: {pca.components}")
                st.write(f"**Mean**: {pca.mean}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
                
                # Original data
                ax1.scatter(X[:int(input_cluster1), 0], X[:int(input_cluster1), 1], 
                           c='#667eea', s=100, alpha=0.6, label='Cluster 1')
                ax1.scatter(X[int(input_cluster1):, 0], X[int(input_cluster1):, 1], 
                           c='#764ba2', s=100, alpha=0.6, label='Cluster 2')
                ax1.set_xlabel('Feature 1')
                ax1.set_ylabel('Feature 2')
                ax1.set_title('Original Data', fontsize=14, fontweight='bold', pad=20)
                ax1.legend()
                ax1.grid(True, alpha=0.3)
                
                # PCA transformed data
                ax2.scatter(X_pca[:int(input_cluster1), 0], X_pca[:int(input_cluster1), 1], 
                           c='#667eea', s=100, alpha=0.6, label='Cluster 1')
                ax2.scatter(X_pca[int(input_cluster1):, 0], X_pca[int(input_cluster1):, 1], 
                           c='#764ba2', s=100, alpha=0.6, label='Cluster 2')
                ax2.set_xlabel('Principal Component 1')
                ax2.set_ylabel('Principal Component 2')
                ax2.set_title('PCA Transformed Data', fontsize=14, fontweight='bold', pad=20)
                ax2.legend()
                ax2.grid(True, alpha=0.3)
                
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
