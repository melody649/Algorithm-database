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

def simpson_integration(f, a, b, n):
    """Simpson's rule for numerical integration."""
    if n % 2 != 0:
        n += 1  # n must be even
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    # Simpson's rule: (h/3) * [y0 + 4y1 + 2y2 + 4y3 + ... + 2y(n-2) + 4y(n-1) + yn]
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[-1])
    
    return integral, x, y

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown('''
    **Simpson's Rule** is a high-precision numerical integration method.
    
    **Core Idea**: Divide the integration interval into an even number of subintervals, approximate the integrand with quadratic polynomials (parabolas) on each subinterval, then sum to get the integral approximation.
    
    **Mathematical Formula**: For interval [a, b], divided into n subintervals (n even), step size h = (b - a)/n
    
    ∫ₐᵇ f(x) dx ≈ (h/3) × [f(a) + 4f(a+h) + 2f(a+2h) + 4f(a+3h) + ... + 2f(b-2h) + 4f(b-h) + f(b)]
    
    **Key Concepts**:
    - **Parabolic Approximation**: Fitting quadratic polynomials on each subinterval
    - **Even Intervals**: Requires an even number of intervals to ensure correct parabolic fitting
    - **Accuracy**: Simpson's rule is exact for polynomial functions
    ''')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Numerical Integration**：Calculating approximate values of definite integrals
    - **Scientific Computing**：Integration calculations in physics, engineering, etc.
    - **Probability and Statistics**：Integration of probability density functions
    - **Differential Equations**：Integration steps in numerical methods
    
    **Advantages**：
    - High accuracy, fast convergence rate (O(h⁴))
    - Exact for polynomial functions
    - High computational efficiency
    
    **Disadvantages**：
    - Requires an even number of intervals
    - May have reduced accuracy for highly oscillatory functions
    - Requires the integrand to be continuous on the interval
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Determine Integration Interval**：Determine the lower and upper limits a and b
    2. **Select Number of Intervals**：Choose an even number of subintervals n (larger n gives higher accuracy)
    3. **Calculate Step Size**：h = (b - a) / n
    4. **Calculate Sampling Points**：Uniformly sample n+1 points in the interval [a, b]
    5. **Apply Simpson's Formula**：Calculate the integral approximation
    6. **Estimate Error**：Estimate the integration error if needed
    
    **Notes**：
    - Ensure the integrand is continuous on the interval
    - For complex functions, a larger n may be needed for sufficient accuracy
    - Consider using adaptive Simpson's method to automatically adjust interval division
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

def simpson_integration(f, a, b, n):
    """Simpson's rule for numerical integration."""
    if n % 2 != 0:
        n += 1  # n must be even
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    # Simpson's rule
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[-1])
    
    return integral

# Define function
def f(x):
    return x**2  # Example function: x²

# Integration parameters
a = REPLACE_1  # Lower limit
b = REPLACE_2  # Upper limit
n = REPLACE_3  # Number of intervals (even)

# Compute integral
result = simpson_integration(f, a, b, n)

print(f"Integral of x² from {a} to {b}: {result}")
print(f"Analytical solution: {b**3/3 - a**3/3}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Lower Limit**")
        input_a = st.number_input("", value=0.0, step=0.1, key="simpson_a")
        
        st.write("**Input 2: Upper Limit**")
        input_b = st.number_input("", value=1.0, step=0.1, key="simpson_b")
        
        st.write("**Input 3: Number of Intervals (even)**")
        input_n = st.number_input("", value=10, min_value=2, step=2, key="simpson_n")
        
        run_button = st.button("▶ Run Code", type="primary", key="simpson_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                if input_a >= input_b:
                    st.error("Lower limit must be less than upper limit")
                else:
                    # Define function
                    def f(x):
                        return x**2
                    
                    # Compute integral
                    result, x, y = simpson_integration(f, input_a, input_b, int(input_n))
                    
                    # Analytical solution
                    analytical = (input_b**3/3 - input_a**3/3)
                    error = abs(result - analytical)
                    
                    st.markdown('<div class="result-area">', unsafe_allow_html=True)
                    st.write(f"**Numerical Integral Result**: {result:.6f}")
                    st.write(f"**Analytical Solution**: {analytical:.6f}")
                    st.write(f"**Absolute Error**: {error:.2e}")
                    st.write(f"**Number of Intervals**: {int(input_n)}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Visualization
                    fig, ax = plt.subplots(figsize=(10, 6))
                    
                    # Plot function
                    x_plot = np.linspace(input_a, input_b, 100)
                    y_plot = f(x_plot)
                    ax.plot(x_plot, y_plot, 'b-', linewidth=2, label='f(x) = x²')
                    
                    # Plot Simpson's approximation
                    ax.scatter(x, y, c='#764ba2', s=50, label='Simpson Points')
                    
                    # Fill area
                    ax.fill_between(x_plot, y_plot, alpha=0.2, label='Integral Area')
                    
                    ax.set_xlabel('x')
                    ax.set_ylabel('f(x)')
                    ax.set_title(f'Simpson\'s Integration (n={int(input_n)})')
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
