# Algorithm Database Guidelines

## 项目结构

```
666/
├── app.py                # 主应用文件
├── algorithms/           # 算法目录
│   ├── math/             # 高等数学算法
│   │   ├── newton_method.py
│   │   ├── lagrange_interpolation.py
│   │   ├── gaussian_elimination.py
│   │   └── simpson_integration.py
│   ├── data_structures/  # 数据结构算法
│   │   ├── binary_search_tree.py
│   │   ├── avl_tree.py
│   │   ├── dijkstra_algorithm.py
│   │   └── hash_table.py
│   └── machine_learning/ # 机器学习算法
│       ├── k_means_clustering.py
│       └── pca.py
└── requirements.txt      # 依赖文件
```

## 一、添加新算法

### 步骤1：创建算法文件

1. **选择分类目录**：根据算法类型选择相应的目录
   - 高等数学：`algorithms/math/`
   - 数据结构：`algorithms/data_structures/`
   - 机器学习：`algorithms/machine_learning/`

2. **创建新文件**：在对应目录中创建新的Python文件，命名格式为`algorithm_name.py`（小写，下划线分隔）

### 步骤2：编写算法代码

使用以下模板编写算法文件：

```python
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
</style>
""", unsafe_allow_html=True)

class AlgorithmName:
    def __init__(self, parameter1=default_value, parameter2=default_value):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        # 初始化其他属性
    
    def method1(self, input_data):
        # 实现算法逻辑
        pass

def main():
    # 1. Noun Explanation
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Noun Explanation</div>', unsafe_allow_html=True)
    st.write("""
    **Algorithm Name** is a brief description of the algorithm.
    
    **Core Idea**：Brief explanation of the core idea.
    
    **Basic Steps**：
    1. Step 1
    2. Step 2
    3. Step 3
    
    **Key Concepts**：
    - Concept 1
    - Concept 2
    - Concept 3
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Application Scenarios
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Application Scenarios</div>', unsafe_allow_html=True)
    st.write("""
    - Scenario 1
    - Scenario 2
    - Scenario 3
    
    **Advantages**：
    - Advantage 1
    - Advantage 2
    
    **Disadvantages**：
    - Disadvantage 1
    - Disadvantage 2
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. Usage Method
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Usage Method</div>', unsafe_allow_html=True)
    st.write("""
    1. Step 1
    2. Step 2
    3. Step 3
    
    **Notes**：
    - Note 1
    - Note 2
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

# Algorithm implementation here
'''
        st.code(code_template, language='python')
    
    with col_input:
        st.markdown("**Input Section**")
        st.markdown('<div class="input-area">', unsafe_allow_html=True)
        
        # Add input widgets here
        input_param1 = st.number_input("Parameter 1", value=default_value)
        
        run_button = st.button("▶ Run Code", type="primary", key="algorithm_run")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_result:
        st.markdown("**Run Result**")
        
        if run_button:
            try:
                # Algorithm implementation and visualization here
                st.markdown('<div class="result-area">', unsafe_allow_html=True)
                st.write("**Results here**")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Visualization code here
                fig, ax = plt.subplots(figsize=(10, 6))
                # Plot code here
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Click the 'Run Code' button on the left to see results")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
```

### 步骤3：更新app.py文件

1. **打开app.py文件**
2. **找到算法列表**：在文件中找到对应分类的算法列表
3. **添加新算法**：按照现有格式添加新算法的名称和文件路径

例如，在数学算法部分添加新算法：

```python
math_algorithms = [
    {"name": "Newton's Method", "file": "algorithms/math/newton_method.py"},
    {"name": "Lagrange Interpolation", "file": "algorithms/math/lagrange_interpolation.py"},
    {"name": "Gaussian Elimination", "file": "algorithms/math/gaussian_elimination.py"},
    {"name": "Simpson Integration", "file": "algorithms/math/simpson_integration.py"},
    {"name": "New Algorithm", "file": "algorithms/math/new_algorithm.py"}  # 添加新算法
]
```

## 二、扩充新大类

### 步骤1：创建新分类目录

1. **在algorithms目录下创建新目录**，例如 `algorithms/statistics/`
2. **在新目录中创建算法文件**，遵循与其他分类相同的结构

### 步骤2：更新app.py文件

1. **添加新分类到侧边栏**：

```python
# 在sidebar_options中添加新分类
sidebar_options = ["Home", "Advanced Mathematics", "Data Structures", "Machine Learning", "Statistics"]
```

2. **添加新分类的算法列表**：

```python
# 添加新分类的算法列表
statistics_algorithms = [
    {"name": "Algorithm 1", "file": "algorithms/statistics/algorithm1.py"},
    {"name": "Algorithm 2", "file": "algorithms/statistics/algorithm2.py"}
]
```

3. **更新导航逻辑**：

```python
# 在导航逻辑中添加新分类
elif selection == "Statistics":
    st.session_state["page"] = "algorithm_list"
    st.session_state["category"] = selection
    algorithm_list(selection)
```

4. **更新algorithm_list函数**：

在algorithm_list函数中添加新分类的处理：

```python
elif category == "Statistics":
    algorithms = statistics_algorithms
```

## 三、最佳实践

1. **代码风格**：
   - 使用英文编写所有内容
   - 保持代码风格一致
   - 添加适当的注释

2. **可视化**：
   - 为每个算法添加可视化图表
   - 使用matplotlib库创建图表
   - 确保图表美观且信息丰富

3. **交互性**：
   - 提供用户输入控件
   - 实时更新结果
   - 处理错误情况

4. **文档**：
   - 提供清晰的算法说明
   - 包含适用场景和优缺点
   - 提供详细的使用方法

## 四、常见问题解决

1. **模块导入错误**：
   - 确保所有必要的库都已安装
   - 检查文件路径是否正确

2. **可视化不显示**：
   - 确保使用st.pyplot()显示图表
   - 检查matplotlib代码是否正确

3. **导航不工作**：
   - 确保在app.py中正确添加了算法
   - 检查文件路径是否正确

4. **样式问题**：
   - 确保复制了完整的CSS样式
   - 保持与现有页面一致的布局

## 五、启动应用

1. **打开命令行终端**
2. **导航到项目目录**：
   ```
   cd C:\Users\l\Desktop\666
   ```
3. **启动Streamlit应用**：
   ```
   streamlit run app.py
   ```
4. **在浏览器中访问**：
   - 打开终端中显示的本地URL（通常是 http://localhost:8501）

## 六、团队协作建议

1. **分工明确**：
   - 每个成员负责特定分类的算法
   - 定期同步进度

2. **代码审查**：
   - 在添加新算法前进行代码审查
   - 确保代码质量和一致性

3. **版本控制**：
   - 考虑使用Git进行版本控制
   - 避免直接修改主分支

4. **测试**：
   - 添加新算法后测试功能
   - 确保所有页面正常显示

---

**注意**：请严格按照本指南的格式和步骤进行操作，以保持项目的一致性和可维护性。如有任何问题，请参考现有算法的实现或咨询团队成员。