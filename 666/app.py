import streamlit as st
import os

# Set page title and layout
st.set_page_config(
    page_title="Algorithm Database",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styles
st.markdown("""
<style>
    /* Global styles */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 0 !important;
    }
    
    /* Sidebar styles - dark theme */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    
    [data-testid="stSidebar"] .stRadio > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    /* Main content area */
    .block-container {
        max-width: 1400px;
        padding: 2rem 3rem !important;
    }
    
    /* Hero section */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 3rem;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.95;
        line-height: 1.6;
    }
    
    /* Stats cards */
    .stats-container {
        display: flex;
        gap: 1.5rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    
    .stat-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        flex: 1;
        min-width: 150px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        font-weight: 500;
    }
    
    /* Category cards */
    .category-section {
        margin-bottom: 2rem;
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1.5rem;
        padding-left: 1rem;
        border-left: 4px solid #667eea;
    }
    
    .category-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 1.5rem;
    }
    
    .category-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .category-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        border-color: #667eea;
    }
    
    .category-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .category-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.8rem;
    }
    
    .category-desc {
        font-size: 1rem;
        color: #666;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .category-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .tag {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Algorithm list styles */
    .algo-list-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    .algo-item {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .algo-item:hover {
        background: #e9ecef;
        transform: translateX(5px);
    }
    
    .algo-info h3 {
        margin: 0 0 0.5rem 0;
        color: #333;
        font-size: 1.3rem;
    }
    
    .algo-info p {
        margin: 0;
        color: #666;
        font-size: 1rem;
    }
    
    /* Button styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Back button */
    .back-button {
        background: #6c757d !important;
    }
    
    /* Title styles */
    h1 {
        color: #333 !important;
        font-weight: 700 !important;
    }
    
    h2 {
        color: #444 !important;
        font-weight: 600 !important;
    }
    
    h3 {
        color: #555 !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Home page content
def home_page():
    # Hero section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🧮 Algorithm Database</div>
        <div class="hero-subtitle">
            An interactive algorithm learning platform for computer science and mathematics.<br>
            Transform complex algorithm concepts into intuitive visual experiences to help you deeply understand algorithm principles.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats cards
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">12</div>
            <div class="stat-label">Classic Algorithms</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">3</div>
            <div class="stat-label">Algorithm Categories</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">∞</div>
            <div class="stat-label">Interactive Experience</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">100%</div>
            <div class="stat-label">Open Source</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Algorithm categories
    # Create a row with title and search bar
    search_col1, search_col2 = st.columns([3, 1])
    with search_col1:
        st.markdown('<div class="section-title">📚 Algorithm Categories</div>', unsafe_allow_html=True)
    with search_col2:
        # Search bar for algorithms
        search_query = st.text_input("Search Algorithms", placeholder="Enter algorithm name...", key="search")
    
    # Collect all algorithms for search functionality
    all_algorithms = []
    
# Advanced Mathematics algorithms
math_algorithms = [
    {"name": "Newton's Method", "file": "newton_method.py", "description": "Iterative algorithm for solving equation roots with quadratic convergence", "icon": "🔢", "category": "Advanced Mathematics", "folder": "math"},
    {"name": "Lagrange Interpolation", "file": "lagrange_interpolation.py", "description": "Construct polynomial interpolation function through known points", "icon": "📈", "category": "Advanced Mathematics", "folder": "math"},
    {"name": "Gaussian Elimination", "file": "gaussian_elimination.py", "description": "Classic algorithm for solving linear systems", "icon": "🔢", "category": "Advanced Mathematics", "folder": "math"},
    {"name": "Simpson's Integration", "file": "simpson_integration.py", "description": "High-precision numerical integration method", "icon": "∫", "category": "Advanced Mathematics", "folder": "math"}
]

# Data Structures algorithms
data_algorithms = [
    {"name": "Binary Search Tree", "file": "binary_search_tree.py", "description": "Efficient binary search tree implementation", "icon": "🌲", "category": "Data Structures", "folder": "data_structures"},
    {"name": "AVL Tree", "file": "avl_tree.py", "description": "Self-balancing binary search tree maintaining O(log n) operation complexity", "icon": "⚖️", "category": "Data Structures", "folder": "data_structures"},
    {"name": "Dijkstra's Algorithm", "file": "dijkstra_algorithm.py", "description": "Classic algorithm for solving single-source shortest path in graphs", "icon": "🛣️", "category": "Data Structures", "folder": "data_structures"},
    {"name": "Hash Table", "file": "hash_table.py", "description": "Efficient key-value storage structure with average O(1) time complexity", "icon": "🔑", "category": "Data Structures", "folder": "data_structures"}
]

# Machine Learning algorithms
ml_algorithms = [
    {"name": "Linear Regression", "file": "linear_regression.py", "description": "Supervised learning algorithm for predicting continuous values", "icon": "📉", "category": "Machine Learning", "folder": "machine_learning"},
    {"name": "K-Nearest Neighbors", "file": "k_nearest_neighbors.py", "description": "Distance-based classification algorithm, simple and intuitive", "icon": "👥", "category": "Machine Learning", "folder": "machine_learning"},
    {"name": "K-Means Clustering", "file": "k_means_clustering.py", "description": "Classic unsupervised clustering algorithm", "icon": "🎯", "category": "Machine Learning", "folder": "machine_learning"},
    {"name": "Principal Component Analysis", "file": "pca.py", "description": "Dimensionality reduction algorithm that extracts main features of data", "icon": "📊", "category": "Machine Learning", "folder": "machine_learning"},
    {"name": "Support Vector Machine", "file": "svm.py", "description": "Powerful supervised learning algorithm for classification and regression", "icon": "⚡", "category": "Machine Learning", "folder": "machine_learning"}
]

# Combine all algorithms
all_algorithms = []
all_algorithms.extend(math_algorithms)
all_algorithms.extend(data_algorithms)
all_algorithms.extend(ml_algorithms)

# Calculate actual algorithm count
total_algorithms = len(all_algorithms)

# Stats cards 
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">
        <div class="stat-number">{total_algorithms}</div>
        <div class="stat-label">Classic Algorithms</div>
    </div>
    ...
</div>
""", unsafe_allow_html=True)
    
# Display search results if there's a query
if search_query:
    search_results = [algo for algo in all_algorithms if search_query.lower() in algo['name'].lower()]
    if search_results:
        st.markdown(f"<div style='margin: 1rem 0; padding: 1rem; background: #f8f9fa; border-radius: 10px;'>" 
                   f"<h3 style='margin-top: 0;'>🔍 Search Results ({len(search_results)} found)</h3>" 
                   "</div>", unsafe_allow_html=True)
        
        for algo in search_results:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"""
                <div class="algo-item">
                    <div class="algo-info">
                        <h3>{algo['icon']} {algo['name']}</h3>
                        <p>{algo['description']} <span style='color: #667eea; font-weight: 500;'>[{algo['category']}]</span></p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                if st.button("Learn Now", key=f"search_{algo['file']}"):
                    st.session_state["algorithm"] = algo
                    st.session_state["category"] = algo["category"]
                    st.session_state["folder"] = algo["folder"]
                    st.session_state["page"] = "algorithm_detail"
                    st.rerun()
        else:
            st.markdown(f"<div style='margin: 1rem 0; padding: 1rem; background: #f8f9fa; border-radius: 10px;'>" 
                       f"<h3 style='margin-top: 0;'>🔍 Search Results</h3>" 
                       f"<p>No algorithms found matching '{search_query}'</p>" 
                       "</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="category-card" onclick="window.location.href='?page=math'">
            <div class="category-icon">📐</div>
            <div class="category-title">Advanced Mathematics</div>
            <div class="category-desc">
                Includes numerical analysis, interpolation methods, linear algebra and other classic mathematical algorithms,
                helping to understand the core principles of mathematical computation.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Advanced Mathematics", key="math_btn"):
            st.session_state["page"] = "algorithm_list"
            st.session_state["category"] = "Advanced Mathematics"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="category-card" onclick="window.location.href='?page=data'">
            <div class="category-icon">🌳</div>
            <div class="category-title">Data Structures</div>
            <div class="category-desc">
                Covers core data structures such as trees, graphs, and hash tables,
                demonstrating efficient ways of data organization and access through visualization.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Data Structures", key="data_btn"):
            st.session_state["page"] = "algorithm_list"
            st.session_state["category"] = "Data Structures"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="category-card" onclick="window.location.href='?page=ml'">
            <div class="category-icon">🤖</div>
            <div class="category-title">Machine Learning</div>
            <div class="category-desc">
                From linear regression to clustering analysis,
                master basic machine learning algorithms and their practical applications.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Machine Learning", key="ml_btn"):
            st.session_state["page"] = "algorithm_list"
            st.session_state["category"] = "Machine Learning"
            st.rerun()
    
    # Platform features
    st.markdown('<div class="section-title" style="margin-top: 3rem;">✨ Platform Features</div>', unsafe_allow_html=True)
    
    feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)
    
    with feat_col1:
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📖</div>
            <div style="font-weight: 600; color: #333; margin-bottom: 0.5rem;">Detailed Principles</div>
            <div style="color: #666; font-size: 0.9rem;">Clear algorithm explanations and mathematical derivations</div>
        </div>
        """, unsafe_allow_html=True)
    
    with feat_col2:
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💻</div>
            <div style="font-weight: 600; color: #333; margin-bottom: 0.5rem;">Code Examples</div>
            <div style="color: #666; font-size: 0.9rem;">Runnable Python code</div>
        </div>
        """, unsafe_allow_html=True)
    
    with feat_col3:
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
            <div style="font-weight: 600; color: #333; margin-bottom: 0.5rem;">Real-time Visualization</div>
            <div style="color: #666; font-size: 0.9rem;">Dynamic charts showing algorithm processes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with feat_col4:
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎛️</div>
            <div style="font-weight: 600; color: #333; margin-bottom: 0.5rem;">Parameter Adjustment</div>
            <div style="color: #666; font-size: 0.9rem;">Interactive parameter control</div>
        </div>
        """, unsafe_allow_html=True)

# Algorithm list page
def algorithm_list(category):
    # Page title
    category_icons = {
        "Advanced Mathematics": "📐",
        "Data Structures": "🌳",
        "Machine Learning": "🤖"
    }
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 16px; padding: 2rem; color: white; margin-bottom: 2rem;">
        <div style="font-size: 2.5rem; font-weight: 700;">{category_icons.get(category, '📚')} {category}</div>
        <div style="font-size: 1.1rem; opacity: 0.9; margin-top: 0.5rem;">
            Select an algorithm below to start learning
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display different algorithms based on category
    if category == "Advanced Mathematics":
        algorithms = [
            {"name": "Newton's Method", "file": "newton_method.py", "description": "Iterative algorithm for solving equation roots with quadratic convergence", "icon": "🔢"},
            {"name": "Lagrange Interpolation", "file": "lagrange_interpolation.py", "description": "Construct polynomial interpolation function through known points", "icon": "📈"},
            {"name": "Gaussian Elimination", "file": "gaussian_elimination.py", "description": "Classic algorithm for solving linear systems", "icon": "🔢"},
            {"name": "Simpson's Integration", "file": "simpson_integration.py", "description": "High-precision numerical integration method", "icon": "∫"}
        ]
        folder = "math"
    
    elif category == "Data Structures":
        algorithms = [
            {"name": "Binary Search Tree", "file": "binary_search_tree.py", "description": "Efficient binary search tree implementation", "icon": "🌲"},
            {"name": "AVL Tree", "file": "avl_tree.py", "description": "Self-balancing binary search tree maintaining O(log n) operation complexity", "icon": "⚖️"},
            {"name": "Dijkstra's Algorithm", "file": "dijkstra_algorithm.py", "description": "Classic algorithm for solving single-source shortest path in graphs", "icon": "🛣️"},
            {"name": "Hash Table", "file": "hash_table.py", "description": "Efficient key-value storage structure with average O(1) time complexity", "icon": "🔑"}
        ]
        folder = "data_structures"
    
    elif category == "Machine Learning":
        algorithms = [
            {"name": "Linear Regression", "file": "linear_regression.py", "description": "Supervised learning algorithm for predicting continuous values", "icon": "📉"},
            {"name": "K-Nearest Neighbors", "file": "k_nearest_neighbors.py", "description": "Distance-based classification algorithm, simple and intuitive", "icon": "👥"},
            {"name": "K-Means Clustering", "file": "k_means_clustering.py", "description": "Classic unsupervised clustering algorithm", "icon": "🎯"},
            {"name": "Principal Component Analysis", "file": "pca.py", "description": "Dimensionality reduction algorithm that extracts main features of data", "icon": "📊"},
            {"name": "Support Vector Machine", "file": "svm.py", "description": "Powerful supervised learning algorithm for classification and regression", "icon": "⚡"}
        ]
        folder = "machine_learning"
    
    # Display algorithm list
    for algo in algorithms:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="algo-item">
                <div class="algo-info">
                    <h3>{algo['icon']} {algo['name']}</h3>
                    <p>{algo['description']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("Start Learning", key=algo["file"]):
                st.session_state["algorithm"] = algo
                st.session_state["category"] = category
                st.session_state["folder"] = folder
                st.session_state["page"] = "algorithm_detail"
                st.rerun()

# Algorithm detail page
def algorithm_detail():
    if "algorithm" not in st.session_state:
        st.error("Please select an algorithm first")
        return
    
    algo = st.session_state["algorithm"]
    category = st.session_state["category"]
    folder = st.session_state["folder"]
    
    # Algorithm title
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 16px; padding: 2rem; color: white; margin-bottom: 2rem;">
        <div style="font-size: 2rem; font-weight: 700;">{algo.get('icon', '🔹')} {algo['name']}</div>
        <div style="font-size: 1rem; opacity: 0.9; margin-top: 0.5rem;">{algo['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Try to import and run the algorithm file
    try:
        # Build module path
        module_path = f"algorithms.{folder}.{algo['file'].replace('.py', '')}"
        # Dynamically import module
        import importlib
        algo_module = importlib.import_module(module_path)
        # Call module's main function
        algo_module.main()
    except Exception as e:
        st.error(f"Failed to load algorithm: {e}")
        st.write("Please ensure the algorithm file is properly implemented with a main function.")

# Sidebar navigation
st.sidebar.markdown("""
<div style="color: white; padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.2); margin-bottom: 1rem;">
    <div style="font-size: 1.5rem; font-weight: 700;">🧮 Algorithm Database</div>
    <div style="font-size: 0.9rem; opacity: 0.8; margin-top: 0.3rem;">Interactive Learning Platform</div>
</div>
""", unsafe_allow_html=True)

# Navigation options
options = ["Home", "Advanced Mathematics", "Data Structures", "Machine Learning"]

# Get current page
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Sidebar selection
selection = st.sidebar.radio("Select Page", options, index=0 if st.session_state["page"] == "home" else (
    1 if st.session_state["page"] in ["algorithm_list", "algorithm_detail"] and st.session_state.get("category") == "Advanced Mathematics" else
    2 if st.session_state["page"] in ["algorithm_list", "algorithm_detail"] and st.session_state.get("category") == "Data Structures" else
    3 if st.session_state["page"] in ["algorithm_list", "algorithm_detail"] and st.session_state.get("category") == "Machine Learning" else 0
))

# Handle navigation
if selection == "Home":
    st.session_state["page"] = "home"
    home_page()
elif st.session_state.get("page") == "algorithm_detail":
    algorithm_detail()
elif selection in ["Advanced Mathematics", "Data Structures", "Machine Learning"]:
    st.session_state["page"] = "algorithm_list"
    st.session_state["category"] = selection
    algorithm_list(selection)

# If current page is algorithm detail, show back button
if st.session_state.get("page") == "algorithm_detail":
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("← Back to Algorithm List"):
        st.session_state["page"] = "algorithm_list"
        st.rerun()
