# 算法数据库网站

一个基于Streamlit构建的交互式算法数据库网站，包含高等数学、数据结构和机器学习领域的经典算法。

## 项目结构

```
666/
├── app.py                          # 主应用程序文件
├── requirements.txt                # 依赖清单
├── README.md                       # 项目说明文档
└── algorithms/                     # 算法模块
    ├── math/                       # 高等数学算法
    │   ├── newton_method.py        # 牛顿法
    │   ├── lagrange_interpolation.py # 拉格朗日插值
    │   ├── gaussian_elimination.py # 高斯消元
    │   └── simpson_integration.py  # 辛普森积分
    ├── data_structures/            # 数据结构算法
    │   ├── binary_search_tree.py   # 二叉搜索树
    │   ├── avl_tree.py             # AVL树
    │   ├── dijkstra_algorithm.py   # Dijkstra算法
    │   └── hash_table.py           # 哈希表
    └── machine_learning/           # 机器学习算法
        ├── linear_regression.py    # 线性回归
        ├── k_nearest_neighbors.py  # K近邻
        ├── k_means_clustering.py   # K均值聚类
        └── principal_component_analysis.py # 主成分分析
```

## 功能特点

- **主页**：展示网站欢迎语和算法类别介绍
- **导航栏**：左侧导航栏包含三个主要类别
- **算法详情页**：每个算法包含原理说明、示例代码、可视化图表和交互控件
- **实时交互**：用户修改参数后实时更新结果和图表

## 本地运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中自动打开，默认地址为 `http://localhost:8501`

## 部署到Streamlit Cloud

### 1. 准备GitHub仓库

将项目代码推送到GitHub仓库：

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/algorithm-database.git
git push -u origin main
```

### 2. 部署到Streamlit Cloud

1. 访问 [Streamlit Cloud](https://streamlit.io/cloud)
2. 使用GitHub账号登录
3. 点击 "New app"
4. 选择你的GitHub仓库
5. 设置主文件路径为 `app.py`
6. 点击 "Deploy"

部署完成后，你将获得一个公开的URL，可以分享给他人访问。

## 算法列表

### 高等数学
- **牛顿法**：求解方程根的迭代算法
- **拉格朗日插值**：通过已知点构造多项式插值函数
- **高斯消元**：求解线性方程组
- **辛普森积分**：数值积分方法

### 数据结构
- **二叉搜索树**：高效的二叉搜索树实现
- **AVL树**：自平衡二叉搜索树
- **Dijkstra算法**：最短路径算法
- **哈希表**：高效的键值对存储结构

### 机器学习
- **线性回归**：预测连续值的回归算法
- **K近邻**：基于距离的分类算法
- **K均值聚类**：无监督聚类算法
- **主成分分析**：降维算法

## 技术栈

- **前端框架**：Streamlit
- **数值计算**：NumPy
- **可视化**：Matplotlib
- **图算法**：NetworkX

## 许可证

MIT License
