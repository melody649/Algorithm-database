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

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        
        # Initialize weights and bias
        self.w = np.zeros(n_features)
        self.b = 0
        
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_[idx]))
                    self.b -= self.lr * y_[idx]
    
    def predict(self, X):
        linear_output = np.dot(X, self.w) - self.b
        return np.sign(linear_output)

def plot_decision_boundary(svm, X, y, ax):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3)
    ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolors='k')
    
    # Plot support vectors
    w = svm.w
    b = svm.b
    x = np.linspace(x_min, x_max, 100)
    y_hyperplane = (-w[0] * x + b) / w[1]
    y_margin1 = (-w[0] * x + b + 1) / w[1]
    y_margin2 = (-w[0] * x + b - 1) / w[1]
    
    ax.plot(x, y_hyperplane, 'k-')
    ax.plot(x, y_margin1, 'k--')
    ax.plot(x, y_margin2, 'k--')

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **Support Vector Machine (SVM)** is a supervised machine learning algorithm used for classification and regression tasks.
    
    **Core Idea**: Find the optimal hyperplane that maximally separates different classes in the feature space.
    
    **Key Concepts**:
    - **Hyperplane**: A decision boundary that separates different classes
    - **Support Vectors**: The data points closest to the hyperplane that influence its position
    - **Margin**: The distance between the hyperplane and the nearest support vectors
    - **Kernel Function**: Transforms data to a higher-dimensional space where it becomes linearly separable
    
    **Types of SVM**:
    - **Linear SVM**: For linearly separable data
    - **Non-linear SVM**: For non-linearly separable data using kernel functions
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Image Classification**：Handwritten digit recognition, object detection
    - **Text Classification**：Spam detection, sentiment analysis, document categorization
    - **Bioinformatics**：Protein structure prediction, gene expression analysis
    - **Financial Analysis**：Credit risk assessment, fraud detection
    - **Medical Diagnosis**：Disease classification, medical image analysis
    
    **Advantages**：
    - Effective in high-dimensional spaces
    - Works well with small training datasets
    - Versatile through different kernel functions
    - Provides clear geometric interpretation
    
    **Disadvantages**：
    - Computationally intensive for large datasets
    - Requires careful parameter tuning
    - Less effective for noisy datasets with overlapping classes
    - Black box model (difficult to interpret)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Prepare Data**：Collect and preprocess data, split into training and test sets
    2. **Feature Scaling**：Standardize features to have zero mean and unit variance
    3. **Choose Kernel**：Select appropriate kernel function (linear, polynomial, RBF, etc.)
    4. **Tune Parameters**：Adjust C (regularization parameter) and kernel parameters
    5. **Train Model**：Fit SVM to training data
    6. **Evaluate Performance**：Test on validation set, adjust parameters if needed
    7. **Make Predictions**：Use trained model on new data
    
    **Notes**：
    - Sensitive to feature scaling
    - Parameter tuning is crucial for performance
    - For large datasets, consider using SGD-based SVM implementations
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

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        
        # Initialize weights and bias
        self.w = np.zeros(n_features)
        self.b = 0
        
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_[idx]))
                    self.b -= self.lr * y_[idx]
    
    def predict(self, X):
        linear_output = np.dot(X, self.w) - self.b
        return np.sign(linear_output)

# Generate sample data
np.random.seed(42)
X = np.vstack([
    np.random.randn(REPLACE_1, 2) + np.array([2, 2]),  # Class 1
    np.random.randn(REPLACE_2, 2) + np.array([-2, -2])  # Class 0
])
y = np.hstack([np.ones(REPLACE_1), np.zeros(REPLACE_2)])

# Train SVM
svm = SVM(learning_rate=0.001, lambda_param=0.01, n_iters=1000)
svm.fit(X, y)

# Predict
predictions = svm.predict(X)
accuracy = np.mean(predictions == np.where(y <= 0, -1, 1))
print(f"Accuracy: {accuracy:.2f}")
print(f"Weights: {svm.w}")
print(f"Bias: {svm.b}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Class 1 Sample Count**")
        input_class1 = st.number_input("Class 1 Sample Count", value=100, min_value=50, max_value=200, step=10, key="svm_class1")
        
        st.write("**Input 2: Class 0 Sample Count**")
        input_class2 = st.number_input("Class 0 Sample Count", value=100, min_value=50, max_value=200, step=10, key="svm_class2")
        
        st.write("**Input 3: Regularization Parameter**")
        input_lambda = st.slider("Regularization Parameter", 0.001, 0.1, 0.01, step=0.001, key="svm_lambda")
        
        run_button = st.button("▶ Run Code", type="primary", key="svm_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Generate data
                np.random.seed(42)
                X = np.vstack([
                    np.random.randn(int(input_class1), 2) + np.array([2, 2]),
                    np.random.randn(int(input_class2), 2) + np.array([-2, -2])
                ])
                y = np.hstack([np.ones(int(input_class1)), np.zeros(int(input_class2))])
                
                # Train SVM
                svm = SVM(learning_rate=0.001, lambda_param=input_lambda, n_iters=1000)
                svm.fit(X, y)
                
                # Predict
                predictions = svm.predict(X)
                accuracy = np.mean(predictions == np.where(y <= 0, -1, 1))
                
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write(f"**Total Samples**: {len(X)}")
                st.write(f"**Accuracy**: {accuracy:.2f}")
                st.write(f"**Weights**: {svm.w}")
                st.write(f"**Bias**: {svm.b}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization
                fig, ax = plt.subplots(figsize=(8, 6))
                plot_decision_boundary(svm, X, y, ax)
                ax.set_title('SVM Decision Boundary')
                ax.set_xlabel('Feature 1')
                ax.set_ylabel('Feature 2')
                st.pyplot(fig)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
