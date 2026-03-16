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

def lagrange_interpolation(x_points, y_points, x):
    """Lagrange interpolation function."""
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown('''
    **Lagrange Interpolation** is a method for constructing a polynomial interpolation function through known points.
    
    **Core Idea**: Using Lagrange basis polynomials to build the interpolation polynomial, ensuring that the polynomial exactly matches the given values at the known points.
    
    **Mathematical Formula**: For n+1 known points (x₀, y₀), (x₁, y₁), ..., (xₙ, yₙ), the Lagrange interpolation polynomial is:
    
    P(x) = Σ(yᵢ · Lᵢ(x)) for i from 0 to n
    
    Lagrange basis polynomial:
    Lᵢ(x) = Π((x - xⱼ)/(xᵢ - xⱼ)) for j ≠ i
    
    **Key Concepts**:
    - **Interpolation Points**: Known (x, y) data points
    - **Basis Polynomials**: Polynomials corresponding to each interpolation point, equal to 1 at that point and 0 at others
    - **Runge Phenomenon**: Possible violent oscillations near endpoints when the number of interpolation points increases
    ''')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Numerical Analysis**：Estimating function values between discrete data points
    - **Signal Processing**：Signal reconstruction and recovery
    - **Image Processing**：Image scaling and rotation
    - **Function Approximation**：Approximating complex functions with polynomials
    - **Computer-Aided Design**：Construction of curves and surfaces
    
    **Advantages**：
    - Simple form, easy to understand and implement
    - Directly utilizes information from all known points
    - No need to solve systems of equations
    
    **Disadvantages**：
    - High computational complexity, O(n²) time complexity
    - May exhibit Runge phenomenon when the number of interpolation points increases
    - Adding new interpolation points requires recalculating the entire polynomial
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Prepare Data**：Collect discrete points (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ) for interpolation
    2. **Construct Basis Polynomials**：Create Lagrange basis polynomials for each interpolation point
    3. **Linear Combination**：Multiply basis polynomials by corresponding y values and sum them
    4. **Calculate Interpolation**：Substitute the desired x value into the interpolation polynomial
    
    **Notes**：
    - Interpolation points should be as evenly distributed as possible
    - Avoid extrapolation outside the interpolation interval
    - For a large number of interpolation points, consider using piecewise interpolation (e.g., spline interpolation)
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

def lagrange_interpolation(x_points, y_points, x):
    """Lagrange interpolation function."""
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result

# Define sample points
x_points = REPLACE_1  # x coordinates
y_points = REPLACE_2  # y coordinates

# Generate interpolation points
x_interp = np.linspace(min(x_points), max(x_points), 100)
y_interp = [lagrange_interpolation(x_points, y_points, x) for x in x_interp]

print(f"Interpolation points: {len(x_interp)}")
print(f"First few interpolated values: {y_interp[:3]}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: X Coordinates**")
        input_x = st.text_input("", value="0, 1, 2, 3, 4", key="lagrange_x")
        
        st.write("**Input 2: Y Coordinates**")
        input_y = st.text_input("", value="0, 1, 4, 9, 16", key="lagrange_y")
        
        run_button = st.button("▶ Run Code", type="primary", key="lagrange_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Parse input values
                x_points = [float(x.strip()) for x in input_x.split(",") if x.strip()]
                y_points = [float(y.strip()) for y in input_y.split(",") if y.strip()]
                
                if len(x_points) != len(y_points):
                    st.error("X and Y coordinates must have the same number of points")
                elif len(x_points) < 2:
                    st.error("At least 2 points are required")
                else:
                    # Generate interpolation points
                    x_interp = np.linspace(min(x_points), max(x_points), 100)
                    y_interp = [lagrange_interpolation(x_points, y_points, x) for x in x_interp]
                    
                    st.markdown('<div class="result-area">', unsafe_allow_html=True)
                    st.write(f"**Interpolation Points**: {len(x_interp)}")
                    st.write(f"**Input Points**: {len(x_points)}")
                    st.write(f"**Interpolation Range**: [{min(x_points):.2f}, {max(x_points):.2f}]")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Visualization
                    fig, ax = plt.subplots(figsize=(10, 6))
                    
                    # Plot original points
                    ax.scatter(x_points, y_points, c='#764ba2', s=150, 
                              edgecolors='white', linewidths=2, label='Original Points')
                    
                    # Plot interpolation curve
                    ax.plot(x_interp, y_interp, 'b-', linewidth=3, label='Lagrange Interpolation')
                    
                    ax.set_xlabel('X')
                    ax.set_ylabel('Y')
                    ax.set_title('Lagrange Interpolation')
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
