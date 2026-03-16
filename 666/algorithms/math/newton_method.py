import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

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
    .code-area {
        background: #1e1e1e;
        border-radius: 8px;
        padding: 1rem;
        color: #d4d4d4;
        font-family: 'Consolas', monospace;
        font-size: 0.9rem;
        overflow-x: auto;
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

def newton_method(f, df, x0, tolerance=1e-6, max_iterations=100):
    """Newton's method for finding roots of a function."""
    x = x0
    iterations = []
    values = []
    
    for i in range(max_iterations):
        iterations.append(i)
        values.append(x)
        
        fx = f(x)
        if abs(fx) < tolerance:
            return x, iterations, values
        
        dfx = df(x)
        if dfx == 0:
            break
        
        x = x - fx / dfx
    
    return x, iterations, values

def get_plot_base64(fig):
    """Convert matplotlib figure to base64 string."""
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode()
    buf.close()
    return img_str

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown('''
    **Newton's Method** is an iterative numerical method used to solve equations of the form f(x) = 0.
    
    **Core Idea**: Using Taylor expansion of the function to gradually approximate the root through tangent line approximation.
    
    **Iteration Formula**: xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)
    
    **Key Concepts**:
    - **Initial Guess**: The starting point of the iteration
    - **Tolerance**: The precision standard for convergence determination
    - **Maximum Iterations**: A safety limit to prevent infinite loops
    ''')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Solving Nonlinear Equations**：When analytical solutions are not available
    - **Optimization Problems**：Finding extrema of functions (points where derivative is zero)
    - **Engineering Calculations**：Numerical computations in physics, chemistry, economics, etc.
    - **Machine Learning**：Internal implementation of certain optimization algorithms
    
    **Advantages**：
    - Fast convergence (quadratic convergence)
    - Simple implementation
    
    **Disadvantages**：
    - Sensitive to initial value
    - Requires derivative calculation
    - May not converge or may converge to the wrong root
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Define Target Function** f(x) and its derivative f'(x)
    2. **Select Initial Guess** x₀ (closer to the true root is better)
    3. **Set Tolerance** ε (e.g., 1e-6) and maximum iterations
    4. **Iterative Calculation**：x_{n+1} = x_n - f(x_n) / f'(x_n)
    5. **Check Convergence**：Stop when |f(x_n)| < ε
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 4. Interactive Code Example
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💻 Interactive Code Example</div>', unsafe_allow_html=True)
    
    # Create three-column layout: Code | Input | Result
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

def newton_method(f, df, x0, tolerance=1e-6, max_iterations=100):
    """
    Newton's method for finding roots.
    
    Parameters:
    -----------
    f : function
        Target function
    df : function
        Derivative of f
    x0 : float
        # REPLACE_1: Initial guess value
    tolerance : float
        Convergence tolerance
    max_iterations : int
        # REPLACE_2: Maximum number of iterations
    """
    x = x0
    iterations = []
    values = []
    
    for i in range(max_iterations):
        iterations.append(i)
        values.append(x)
        
        fx = f(x)
        if abs(fx) < tolerance:
            return x, iterations, values
        
        dfx = df(x)
        if dfx == 0:
            break
        
        x = x - fx / dfx
    
    return x, iterations, values

# Define the function: f(x) = x^2 - 4
# Root should be x = 2 or x = -2
def f(x):
    return x**2 - 4

def df(x):
    return 2*x

# Run Newton's method
root, iterations, values = newton_method(
    f, df, 
    x0=REPLACE_1,      # Initial guess
    max_iterations=REPLACE_2  # Max iterations
)

print(f"Root found: {root:.6f}")
print(f"Iterations: {len(iterations)}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Initial Guess**")
        input_x0 = st.number_input("", value=1.0, step=0.1, key="input_x0")
        
        st.write("**Input 2: Maximum Iterations**")
        input_max_iter = st.number_input("", value=20, step=1, min_value=1, max_value=100, key="input_max_iter")
        
        run_button = st.button("▶ Run Code", type="primary")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            # Run code with user input values
            x0 = input_x0
            max_iter = int(input_max_iter)
            
            # Define function
            def f(x):
                return x**2 - 4
            
            def df(x):
                return 2*x
            
            # Run Newton's method
            root, iterations, values = newton_method(f, df, x0, 1e-6, max_iter)
            
            # Display results
            st.markdown('<div class="result-area">', unsafe_allow_html=True)
            st.write(f"**Root Found**: {root:.6f}")
            st.write(f"**Iterations**: {len(iterations)}")
            st.write(f"**Verify f(root)**: {f(root):.2e}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Visualization
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
            
            # Function plot
            x = np.linspace(-3, 3, 100)
            y = f(x)
            ax1.plot(x, y, 'b-', label='f(x) = x² - 4', linewidth=2)
            ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
            ax1.scatter(root, 0, color='red', s=100, zorder=5, label=f'Root: {root:.4f}')
            ax1.scatter(x0, f(x0), color='green', s=100, zorder=5, label=f'Initial: {x0}')
            ax1.set_xlabel('x')
            ax1.set_ylabel('f(x)')
            ax1.set_title('Function Plot')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # Convergence process
            ax2.plot(iterations, values, 'bo-', linewidth=2, markersize=6)
            ax2.axhline(y=root, color='red', linestyle='--', alpha=0.5, label=f'True root: ±2')
            ax2.set_xlabel('Iteration')
            ax2.set_ylabel('x value')
            ax2.set_title('Convergence Process')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 5. More Examples
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔍 More Examples</div>', unsafe_allow_html=True)
    
    example_choice = st.selectbox(
        "Select Example Function",
        ["x² - 4 = 0 (Roots: ±2)", "x³ - 2x - 5 = 0 (Root: ~2.09)", "sin(x) = 0 (Roots: nπ)"]
    )
    
    if example_choice == "x² - 4 = 0 (Roots: ±2)":
        st.write("""
        **Function**: f(x) = x² - 4
        **Derivative**: f'(x) = 2x
        **True Roots**: x = 2 or x = -2
        **Suggested Initial Value**: 1.0 (converges to 2) or -1.0 (converges to -2)
        """)
    elif example_choice == "x³ - 2x - 5 = 0 (Root: ~2.09)":
        st.write("""
        **Function**: f(x) = x³ - 2x - 5
        **Derivative**: f'(x) = 3x² - 2
        **True Root**: x ≈ 2.0946
        **Suggested Initial Value**: 2.0
        """)
    else:
        st.write("""
        **Function**: f(x) = sin(x)
        **Derivative**: f'(x) = cos(x)
        **True Roots**: x = nπ (n is integer)
        **Suggested Initial Value**: 3.0 (converges to π)
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
