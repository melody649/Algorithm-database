import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

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

class KNearestNeighbors:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predictions = []
        for x in X:
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
            k_indices = np.argsort(distances)[:self.k]
            k_nearest_labels = self.y_train[k_indices]
            most_common = Counter(k_nearest_labels).most_common(1)
            predictions.append(most_common[0][0])
        return np.array(predictions)

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.write("""
    **K-Nearest Neighbors (KNN)** is an instance-based learning algorithm used for classification and regression.
    
    **Core Idea**: Calculate the distance between the sample to be predicted and training samples, find the K nearest neighbors, and then make predictions based on the neighbors' labels.
    
    **Key Concepts**:
    - **K Value**: The number of neighbors selected. Smaller K makes the model more complex, larger K makes it simpler
    - **Distance Metric**: Commonly Euclidean Distance
    - **Voting Mechanism**: Majority voting for classification problems, average for regression problems
    
    **Distance Formula**: d(x, y) = √Σ(xᵢ - yᵢ)²
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Recommendation Systems**: Recommending based on similar user behavior
    - **Image Recognition**: Handwritten digit recognition, face recognition
    - **Medical Diagnosis**: Diagnosing diseases based on symptom features
    - **Text Classification**: News categorization, sentiment analysis
    
    **Advantages**:
    - Simple and intuitive, no training process required
    - Suitable for multi-class classification problems
    - No assumptions about data distribution
    
    **Disadvantages**:
    - Computationally intensive, requires storing all training data
    - Sensitive to K value selection
    - Sensitive to outliers
    - Poor performance on high-dimensional data (curse of dimensionality)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Prepare Data**: Collect labeled training data
    2. **Select K Value**: Usually choose the optimal K value through cross-validation
    3. **Calculate Distances**: Compute distances between the sample to be predicted and all training samples
    4. **Find K Nearest Neighbors**: Sort by distance and select the K nearest
    5. **Predict**:
       - Classification: Majority vote determines the class
       - Regression: Calculate the average of K neighbors
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
from collections import Counter

class KNearestNeighbors:
    def __init__(self, k=3):
        self.k = k
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predictions = []
        for x in X:
            # Calculate distances
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
            # Find k nearest neighbors
            k_indices = np.argsort(distances)[:self.k]
            k_nearest_labels = self.y_train[k_indices]
            # Vote
            most_common = Counter(k_nearest_labels).most_common(1)
            predictions.append(most_common[0][0])
        return np.array(predictions)

# Generate sample data
np.random.seed(42)
n_samples = REPLACE_1  # Number of samples per class

# Class 0: centered at (2, 2)
X_class0 = np.random.randn(n_samples, 2) + np.array([2, 2])
# Class 1: centered at (6, 6)
X_class1 = np.random.randn(n_samples, 2) + np.array([6, 6])

X_train = np.vstack([X_class0, X_class1])
y_train = np.array([0] * n_samples + [1] * n_samples)

# Create and train model
knn = KNearestNeighbors(k=REPLACE_2)  # K value
knn.fit(X_train, y_train)

# Predict new point
new_point = np.array([[REPLACE_3, REPLACE_4]])  # X, Y coordinates
prediction = knn.predict(new_point)

print(f"Prediction for point {new_point[0]}: Class {prediction[0]}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Samples per class**")
        input_samples = st.number_input("", value=20, min_value=5, max_value=50, step=5, key="knn_samples")
        
        st.write("**Input 2: K value**")
        input_k = st.number_input("", value=3, min_value=1, max_value=10, step=1, key="knn_k")
        
        st.write("**Input 3: Prediction point X coordinate**")
        input_x = st.number_input("", value=4.0, step=0.5, key="knn_x")
        
        st.write("**Input 4: Prediction point Y coordinate**")
        input_y = st.number_input("", value=4.0, step=0.5, key="knn_y")
        
        run_button = st.button("▶ Run Code", type="primary", key="knn_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            # Generate data
            np.random.seed(42)
            n_samples = int(input_samples)
            
            X_class0 = np.random.randn(n_samples, 2) + np.array([2, 2])
            X_class1 = np.random.randn(n_samples, 2) + np.array([6, 6])
            
            X_train = np.vstack([X_class0, X_class1])
            y_train = np.array([0] * n_samples + [1] * n_samples)
            
            # Train model
            knn = KNearestNeighbors(k=int(input_k))
            knn.fit(X_train, y_train)
            
            # Predict
            new_point = np.array([[input_x, input_y]])
            prediction = knn.predict(new_point)
            
            # Calculate distances for visualization
            distances = np.sqrt(np.sum((X_train - new_point[0]) ** 2, axis=1))
            k_indices = np.argsort(distances)[:int(input_k)]
            
            st.markdown('<div class="result-area">', unsafe_allow_html=True)
            st.write(f"**Prediction Point**: ({input_x}, {input_y})")
            st.write(f"**Predicted Class**: Class {prediction[0]}")
            st.write(f"**K Value**: {int(input_k)}")
            st.write(f"**Nearest Neighbor Distance**: {distances[k_indices[0]]:.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Visualization
            fig, ax = plt.subplots(figsize=(8, 8))
            
            # Plot training data
            ax.scatter(X_class0[:, 0], X_class0[:, 1], c='#667eea', label='Class 0', alpha=0.6, s=100)
            ax.scatter(X_class1[:, 0], X_class1[:, 1], c='#764ba2', label='Class 1', alpha=0.6, s=100)
            
            # Plot new point
            color = '#667eea' if prediction[0] == 0 else '#764ba2'
            ax.scatter(new_point[0, 0], new_point[0, 1], c=color, marker='*', s=500, 
                      edgecolors='black', linewidths=2, label=f'Prediction: Class {prediction[0]}', zorder=5)
            
            # Draw lines to k nearest neighbors
            for idx in k_indices:
                ax.plot([new_point[0, 0], X_train[idx, 0]], 
                       [new_point[0, 1], X_train[idx, 1]], 
                       'k--', alpha=0.3, linewidth=1)
            
            ax.set_xlabel('Feature 1')
            ax.set_ylabel('Feature 2')
            ax.set_title(f'KNN Classification (K={int(input_k)})')
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_aspect('equal')
            
            st.pyplot(fig)
        else:
            st.info("Click the 'Run Code' button on the left to view results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
