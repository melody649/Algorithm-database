import streamlit as st
import importlib

# =============================================================================
# Global Constants - Algorithm Data
# =============================================================================

ALGORITHMS = {
    "Advanced Mathematics": {
        "folder": "math",
        "icon": "📐",
        "items": [
            {"name": "Newton's Method", "file": "newton_method.py", "description": "Iterative algorithm for solving equation roots with quadratic convergence", "icon": "🔢"},
            {"name": "Lagrange Interpolation", "file": "lagrange_interpolation.py", "description": "Construct polynomial interpolation function through known points", "icon": "📈"},
            {"name": "Gaussian Elimination", "file": "gaussian_elimination.py", "description": "Classic algorithm for solving linear systems", "icon": "🔢"},
            {"name": "Simpson's Integration", "file": "simpson_integration.py", "description": "High-precision numerical integration method", "icon": "∫"}
        ]
    },
    "Data Structures": {
        "folder": "data_structures",
        "icon": "🌳",
        "items": [
            {"name": "Binary Search Tree", "file": "binary_search_tree.py", "description": "Efficient binary search tree implementation", "icon": "🌲"},
            {"name": "AVL Tree", "file": "avl_tree.py", "description": "Self-balancing binary search tree maintaining O(log n) operation complexity", "icon": "⚖️"},
            {"name": "Dijkstra's Algorithm", "file": "dijkstra_algorithm.py", "description": "Classic algorithm for solving single-source shortest path in graphs", "icon": "🛣️"},
            {"name": "Hash Table", "file": "hash_table.py", "description": "Efficient key-value storage structure with average O(1) time complexity", "icon": "🔑"}
        ]
    },
    "Machine Learning": {
        "folder": "machine_learning",
        "icon": "🤖",
        "items": [
            {"name": "Linear Regression", "file": "linear_regression.py", "description": "Supervised learning algorithm for predicting continuous values", "icon": "📉"},
            {"name": "K-Nearest Neighbors", "file": "k_nearest_neighbors.py", "description": "Distance-based classification algorithm, simple and intuitive", "icon": "👥"},
            {"name": "K-Means Clustering", "file": "k_means_clustering.py", "description": "Classic unsupervised clustering algorithm", "icon": "🎯"},
            {"name": "Principal Component Analysis", "file": "pca.py", "description": "Dimensionality reduction algorithm that extracts main features of data", "icon": "📊"},
            {"name": "Support Vector Machine", "file": "svm.py", "description": "Powerful supervised learning algorithm for classification and regression", "icon": "⚡"}
        ]
    }
}

# Flatten all algorithms for search functionality
ALL_ALGOS = []
for cat, data in ALGORITHMS.items():
    for algo in data["items"]:
        algo_copy = algo.copy()
        algo_copy["category"] = cat
        algo_copy["folder"] = data["folder"]
        ALL_ALGOS.append(algo_copy)

# =============================================================================
# Page Configuration
# =============================================================================

st.set_page_config(
    page_title="Algorithm Database",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# Custom CSS (unchanged, keep as original)
# =============================================================================

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

# =============================================================================
# Helper Functions
# =============================================================================

def get_algorithms_by_category(category):
    """Return algorithm list for a given category."""
    return ALGORITHMS[category]["items"]

# =============================================================================
# Page Rendering Functions
# =============================================================================

def home_page():
    """Render the home page."""
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
    
    # Search and stats
    search_col1, search_col2 = st.columns([3, 1])
    with search_col1:
        st.markdown('<div class="section-title">📚 Algorithm Categories</div>', unsafe_allow_html=True)
    with search_col2:
        search_query = st.text_input("Search Algorithms", placeholder="Enter algorithm name...", key="search_home")
    
    # Stats cards
    total_algos = len(ALL_ALGOS)
    st.markdown(f"""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">{total_algos}</div>
            <div class="stat-label">Classic Algorithms</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{len(ALGORITHMS)}</div>
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
    
    # Search results
    if search_query:
        search_results = [algo for algo in ALL_ALGOS if search_query.lower() in algo['name'].lower()]
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
                    # Use a unique key that includes category to avoid collisions
                    if st.button("Learn Now", key=f"search_{algo['category']}_{algo['file']}"):
                        st.session_state["algorithm"] = algo
                        st.session_state["category"] = algo["category"]
                        st.session_state["folder"] = algo["folder"]
                        st.session_state["page"] = "algorithm_detail"
                        st.rerun()
    
    # Category cards
    col1, col2, col3 = st.columns(3)
    categories = list(ALGORITHMS.keys())
    
    with col1:
        cat = categories[0]
        data = ALGORITHMS[cat]
        st.markdown(f"""
        <div class="category-card">
            <div class="category-icon">{data['icon']}</div>
            <div class="category-title">{cat}</div>
            <div class="category-desc">
                Includes numerical analysis, interpolation methods, linear algebra and other classic mathematical algorithms,
                helping to understand the core principles of mathematical computation.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Explore {cat}", key="math_btn"):
            st.session_state["page"] = "algorithm_list"
            st.session_state["category"] = cat
            st.rerun()
    
    with col2:
        cat = categories[1]
        data = ALGORITHMS[cat]
        st.markdown(f"""
        <div class="category-card">
            <div class="category-icon">{data['icon']}</div>
            <div class="category-title">{cat}</div>
            <div class="category-desc">
                Covers core data structures such as trees, graphs, and hash tables,
                demonstrating efficient ways of data organization and access through visualization.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Explore {cat}", key="data_btn"):
            st.session_state["page"] = "algorithm_list"
            st.session_state["category"] = cat
            st.rerun()
    
    with col3:
        cat = categories[2]
        data = ALGORITHMS[cat]
        st.markdown(f"""
        <div class="category-card">
            <div class="category-icon">{data['icon']}</div>
            <div class="category-title">{cat}</div>
            <div class="category-desc">
                From linear regression to clustering analysis,
                master basic machine learning algorithms and their practical applications.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Explore {cat}", key="ml_btn"):
            st.session_state["page"] = "algorithm_list"
            st.session_state["category"] = cat
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

def algorithm_list(category):
    """Render the list of algorithms for a given category."""
    data = ALGORITHMS[category]
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 16px; padding: 2rem; color: white; margin-bottom: 2rem;">
        <div style="font-size: 2.5rem; font-weight: 700;">{data['icon']} {category}</div>
        <div style="font-size: 1.1rem; opacity: 0.9; margin-top: 0.5rem;">
            Select an algorithm below to start learning
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Optional search within category
    search_query = st.text_input("Search in this category", placeholder="Enter algorithm name...", key=f"search_{category}")
    
    algorithms = data["items"]
    if search_query:
        algorithms = [a for a in algorithms if search_query.lower() in a["name"].lower()]
        if not algorithms:
            st.info("No matching algorithms found.")
    
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
            if st.button("Start Learning", key=f"{category}_{algo['file']}"):
                algo_with_meta = algo.copy()
                algo_with_meta["category"] = category
                algo_with_meta["folder"] = data["folder"]
                st.session_state["algorithm"] = algo_with_meta
                st.session_state["category"] = category
                st.session_state["folder"] = data["folder"]
                st.session_state["page"] = "algorithm_detail"
                st.rerun()

def algorithm_detail():
    """Render the detail page for a selected algorithm."""
    if "algorithm" not in st.session_state:
        st.error("Please select an algorithm first")
        return
    
    algo = st.session_state["algorithm"]
    category = st.session_state["category"]
    folder = st.session_state["folder"]
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 16px; padding: 2rem; color: white; margin-bottom: 2rem;">
        <div style="font-size: 2rem; font-weight: 700;">{algo.get('icon', '🔹')} {algo['name']}</div>
        <div style="font-size: 1rem; opacity: 0.9; margin-top: 0.5rem;">{algo['description']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Dynamic import and execution with improved error handling
    try:
        module_name = f"algorithms.{folder}.{algo['file'].replace('.py', '')}"
        algo_module = importlib.import_module(module_name)
        
        # Check if main function exists
        if not hasattr(algo_module, "main"):
            st.error(f"The algorithm module '{algo['file']}' does not have a 'main()' function. Please implement it.")
            return
        
        # Execute the main function
        algo_module.main()
        
    except ModuleNotFoundError:
        st.error(f"Algorithm file '{algo['file']}' not found in 'algorithms/{folder}/'. Please ensure the file exists.")
    except AttributeError as e:
        st.error(f"The algorithm module is missing a required component: {e}")
    except Exception as e:
        st.error(f"An error occurred while running the algorithm: {e}")
        # Optionally display full traceback in an expander for debugging
        with st.expander("Show error details"):
            st.exception(e)

# =============================================================================
# Sidebar Navigation
# =============================================================================

st.sidebar.markdown("""
<div style="color: white; padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.2); margin-bottom: 1rem;">
    <div style="font-size: 1.5rem; font-weight: 700;">🧮 Algorithm Database</div>
    <div style="font-size: 0.9rem; opacity: 0.8; margin-top: 0.3rem;">Interactive Learning Platform</div>
</div>
""", unsafe_allow_html=True)

# Navigation options
options = ["Home"] + list(ALGORITHMS.keys())

# Use session_state to manage navigation selection
if "nav_selection" not in st.session_state:
    st.session_state.nav_selection = "Home"

# Sidebar radio (store selection in session_state)
selected = st.sidebar.radio("Select Page", options, key="nav_radio", index=options.index(st.session_state.nav_selection))

# Update session_state when selection changes
if selected != st.session_state.nav_selection:
    st.session_state.nav_selection = selected
    # Reset page state based on selection
    if selected == "Home":
        st.session_state["page"] = "home"
    else:
        st.session_state["page"] = "algorithm_list"
        st.session_state["category"] = selected
    st.rerun()

# =============================================================================
# Main Routing Logic
# =============================================================================

# Determine current page from session_state (default to home)
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Render appropriate page
if st.session_state["page"] == "home":
    home_page()
elif st.session_state["page"] == "algorithm_list":
    if "category" in st.session_state and st.session_state["category"] in ALGORITHMS:
        algorithm_list(st.session_state["category"])
    else:
        st.error("Invalid category. Returning to home.")
        st.session_state["page"] = "home"
        st.rerun()
elif st.session_state["page"] == "algorithm_detail":
    algorithm_detail()
    # Add back button in sidebar
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("← Back to Algorithm List"):
        st.session_state["page"] = "algorithm_list"
        st.rerun()
else:
    # Fallback
    st.session_state["page"] = "home"
    home_page()