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

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.cost_history = []
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            y_pred = np.dot(X, self.weights) + self.bias
            
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            cost = (1 / (2 * n_samples)) * np.sum((y_pred - y) ** 2)
            self.cost_history.append(cost)
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.write("""
    **Linear Regression** is a supervised learning algorithm used for predicting continuous values.
    
    **Core Idea**: Establish a linear relationship between input variables and output variables by fitting a straight line (or hyperplane).
    
    **Model Formula**: y = wx + b
    - **w (Weight)**: The coefficient of the feature, representing the degree of influence of the feature on the predicted value
    - **b (Bias)**: The intercept, representing the predicted value when all features are 0
    
    **Loss Function**: Mean Squared Error (MSE) = (1/2n) * Σ(y_pred - y)²
    
    **Optimization Method**: Gradient Descent
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **House Price Prediction**: Predicting prices based on house features
    - **Sales Forecasting**: Predicting future sales based on historical data
    - **Trend Analysis**: Analyzing trends in time series data
    - **Risk Assessment**: Predicting financial risks, insurance claims, etc.
    
    **Advantages**:
    - Simple and easy to understand, strong interpretability
    - High computational efficiency
    - Can handle multi-feature data
    
    **Disadvantages**:
    - Can only fit linear relationships
    - Sensitive to outliers
    - Assumes linear correlation between features and target variable
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Prepare Data**: Collect input features X and target values y
    2. **Initialize Parameters**: Set initial values for weights w and bias b (usually 0)
    3. **Select Hyperparameters**:
       - Learning Rate: Controls the step size of parameter updates
       - Iterations: Number of training rounds
    4. **Train Model**: Use gradient descent to optimize parameters
    5. **Predict**: Use the trained model for prediction
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

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples = X.shape[0]
        self.weights = 0
        self.bias = 0
        
        for _ in range(self.n_iterations):
            y_pred = self.weights * X + self.bias
            
            # Gradients
            dw = (1/n_samples) * np.sum(X * (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X):
        return self.weights * X + self.bias

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
# True relationship: y = 2.5x + 3.0 + noise
y = REPLACE_1 * X.flatten() + REPLACE_2 + np.random.randn(100) * 1.0

# Train model
model = LinearRegression(
    learning_rate=REPLACE_3,  # Learning rate
    n_iterations=1000
)
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

print(f"True weights: 2.5, Predicted: {model.weights:.4f}")
print(f"True bias: 3.0, Predicted: {model.bias:.4f}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: True Weight**")
        input_weight = st.number_input("", value=2.5, step=0.1, key="lr_weight")
        
        st.write("**Input 2: True Bias**")
        input_bias = st.number_input("", value=3.0, step=0.1, key="lr_bias")
        
        st.write("**Input 3: Learning Rate**")
        input_lr = st.number_input("", value=0.01, step=0.001, format="%.3f", key="lr_rate")
        
        run_button = st.button("▶ Run Code", type="primary", key="lr_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            # Generate data with user inputs
            np.random.seed(42)
            X = np.random.rand(100, 1) * 10
            y = input_weight * X.flatten() + input_bias + np.random.randn(100) * 1.0
            
            # Train model
            model = LinearRegression(learning_rate=input_lr, n_iterations=1000)
            model.fit(X, y)
            
            y_pred = model.predict(X)
            
            # Metrics
            mse = np.mean((y - y_pred) ** 2)
            r2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2)
            
            st.markdown('<div class="result-area">', unsafe_allow_html=True)
            st.write(f"**True Weight**: {input_weight}")
            st.write(f"**Predicted Weight**: {model.weights:.4f}")
            st.write(f"**True Bias**: {input_bias}")
            st.write(f"**Predicted Bias**: {model.bias:.4f}")
            st.write(f"**MSE**: {mse:.4f}")
            st.write(f"**R² Score**: {r2:.4f}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Visualization
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
            
            # Data and fitted line
            ax1.scatter(X, y, alpha=0.6, label='Data points')
            X_line = np.linspace(0, 10, 100)
            y_line = model.weights * X_line + model.bias
            ax1.plot(X_line, y_line, 'r-', linewidth=2, label=f'y = {model.weights:.2f}x + {model.bias:.2f}')
            ax1.set_xlabel('X')
            ax1.set_ylabel('y')
            ax1.set_title('Linear Regression Fit')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # Residuals
            residuals = y - y_pred
            ax2.scatter(y_pred, residuals, alpha=0.6)
            ax2.axhline(y=0, color='r', linestyle='--')
            ax2.set_xlabel('Predicted values')
            ax2.set_ylabel('Residuals')
            ax2.set_title('Residual Plot')
            ax2.grid(True, alpha=0.3)
            
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("Click the 'Run Code' button on the left to view results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
