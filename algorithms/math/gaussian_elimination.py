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

def gaussian_elimination(A, b):
    """Gaussian elimination to solve Ax = b."""
    n = len(b)
    
    # Augmented matrix
    augmented = np.hstack([A, b.reshape(-1, 1)])
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        max_row = i + np.argmax(np.abs(augmented[i:, i]))
        if augmented[max_row, i] == 0:
            return None  # Singular matrix
        
        # Swap rows
        augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # Eliminate below
        for j in range(i+1, n):
            factor = augmented[j, i] / augmented[i, i]
            augmented[j, i:] -= factor * augmented[i, i:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], x[i+1:n])) / augmented[i, i]
    
    return x, augmented

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.markdown("""
    **Gaussian Elimination** is a classic algorithm used to solve systems of linear equations.
    
    **Core Idea**: Through a series of row operations, transform the augmented matrix of the linear system into upper triangular form, then solve for the unknowns through back substitution.
    
    **Basic Steps**:
    1. **Forward Elimination**: Transform the matrix into upper triangular form
    2. **Back Substitution**: Start from the last equation and solve for each unknown sequentially
    
    **Key Concepts**:
    - **Pivot**: Non-zero element used to eliminate other elements in the column
    - **Row Exchange**: To avoid division by zero or reduce rounding errors
    - **Augmented Matrix**: Combining the coefficient matrix and constant terms into a single matrix
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - **Linear Algebra**：Solving systems of linear equations
    - **Matrix Inversion**：By constructing an identity matrix as the right-hand side constant term
    - **Determinant Calculation**：By transforming the matrix into upper triangular form
    - **Engineering Calculations**：Structural analysis, circuit analysis, etc.
    - **Numerical Analysis**：Foundation for other numerical methods
    
    **Advantages**：
    - Simple and straightforward algorithm, easy to implement
    - High computational efficiency, O(n³) time complexity
    - Suitable for small to medium-sized systems
    
    **Disadvantages**：
    - High computational cost for large systems
    - Sensitive to rounding errors
    - May be unstable for ill-conditioned matrices
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. **Construct Augmented Matrix**：Combine the coefficient matrix A and constant terms b into an augmented matrix
    2. **Forward Elimination**：
       - For each column, find the pivot (element with the largest absolute value)
       - Swap rows to place the pivot in the current row
       - Use the pivot to eliminate all elements below
    3. **Back Substitution**：
       - Start from the last equation and solve for the last unknown
       - Substitute upward sequentially to solve for other unknowns
    4. **Verify Solution**：Substitute the solution back into the original system to verify correctness
    
    **Notes**：
    - Avoid division by zero (select pivot)
    - Be aware of rounding error accumulation
    - For large systems, consider more stable methods
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

def gaussian_elimination(A, b):
    """Gaussian elimination to solve Ax = b."""
    n = len(b)
    
    # Augmented matrix
    augmented = np.hstack([A, b.reshape(-1, 1)])
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        max_row = i + np.argmax(np.abs(augmented[i:, i]))
        if augmented[max_row, i] == 0:
            return None  # Singular matrix
        
        # Swap rows
        augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # Eliminate below
        for j in range(i+1, n):
            factor = augmented[j, i] / augmented[i, i]
            augmented[j, i:] -= factor * augmented[i, i:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], x[i+1:n])) / augmented[i, i]
    
    return x

# Define system
A = REPLACE_1  # Coefficient matrix
b = REPLACE_2  # Constant terms

# Solve
x = gaussian_elimination(A, b)

print(f"Solution: {x}")
print(f"Verification: A @ x = {A @ x}")
print(f"Expected: {b}")
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        st.write("**Input 1: Coefficient Matrix (rows separated by semicolons)**")
        input_A = st.text_input("", value="1, 2, 3; 4, 5, 6; 7, 8, 10", key="gaussian_A")
        
        st.write("**Input 2: Constant Terms**")
        input_b = st.text_input("", value="6; 15; 28", key="gaussian_b")
        
        run_button = st.button("▶ Run Code", type="primary", key="gaussian_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Parse input values
                rows = [row.strip() for row in input_A.split(";") if row.strip()]
                A = []
                for row in rows:
                    elements = [float(e.strip()) for e in row.split(",") if e.strip()]
                    A.append(elements)
                A = np.array(A)
                
                b = np.array([float(e.strip()) for e in input_b.split(";") if e.strip()])
                
                if A.shape[0] != A.shape[1]:
                    st.error("Coefficient matrix must be square")
                elif A.shape[0] != len(b):
                    st.error("Number of rows in coefficient matrix must match length of constant terms")
                else:
                    # Solve
                    x, augmented = gaussian_elimination(A, b)
                    
                    if x is None:
                        st.error("Matrix is singular, no solution or infinitely many solutions")
                    else:
                        # Verification
                        verification = A @ x
                        error = np.max(np.abs(verification - b))
                        
                        st.markdown('<div class="result-area">', unsafe_allow_html=True)
                        st.write(f"**Solution**: {x}")
                        st.write(f"**Verification A@x**: {verification}")
                        st.write(f"**Expected**: {b}")
                        st.write(f"**Maximum Error**: {error:.2e}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Visualization of the augmented matrix
                        fig, ax = plt.subplots(figsize=(10, 6))
                        ax.axis('off')
                        
                        # Create table
                        table_data = []
                        for i in range(len(augmented)):
                            row = []
                            for j in range(len(augmented[i])-1):
                                row.append(f"{augmented[i, j]:.2f}")
                            row.append("|")
                            row.append(f"{augmented[i, -1]:.2f}")
                            table_data.append(row)
                        
                        table = ax.table(cellText=table_data, 
                                        colLabels=[f'x{i+1}' for i in range(len(augmented))] + ['|', 'b'],
                                        cellLoc='center',
                                        loc='center')
                        
                        table.auto_set_font_size(False)
                        table.set_fontsize(10)
                        table.scale(1, 1.5)
                        
                        ax.set_title('Augmented Matrix After Gaussian Elimination', 
                                   fontsize=14, fontweight='bold', pad=20)
                        
                        st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
