import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 主成分分析实现
class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None
        self.explained_variance_ratio = None
    
    def fit(self, X):
        # 标准化数据
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # 计算协方差矩阵
        cov_matrix = np.cov(X_centered.T)
        
        # 计算特征值和特征向量
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        
        # 排序特征向量（按特征值降序）
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # 选择前n_components个主成分
        self.components = eigenvectors[:, :self.n_components]
        
        # 计算解释方差比例
        total_variance = np.sum(eigenvalues)
        self.explained_variance_ratio = eigenvalues[:self.n_components] / total_variance
    
    def transform(self, X):
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

# 主函数
def main():
    st.write("""
    # 主成分分析
    
    主成分分析（Principal Component Analysis，PCA）是一种降维算法，它通过线性变换将原始数据映射到一个新的坐标系中，使得数据在新坐标系的第一个坐标（第一主成分）上的方差最大，第二个坐标（第二主成分）上的方差次大，以此类推。
    
    ## 算法原理
    1. **标准化**：将数据减去均值，使数据中心化
    2. **计算协方差矩阵**：协方差矩阵描述了数据各维度之间的相关性
    3. **特征值分解**：计算协方差矩阵的特征值和特征向量
    4. **选择主成分**：选择特征值最大的前k个特征向量作为主成分
    5. **投影**：将原始数据投影到主成分空间
    
    ## 优缺点
    - **优点**：降低数据维度，减少计算量，去除噪声
    - **缺点**：只能捕捉线性关系，主成分的可解释性较差
    """)
    
    # 交互控件
    st.sidebar.header("参数设置")
    
    # 数据生成参数
    n_samples = st.sidebar.slider("样本数量", min_value=50, max_value=300, value=150)
    n_features = st.sidebar.slider("原始特征数", min_value=3, max_value=10, value=5)
    
    # 模型参数
    n_components = st.sidebar.slider("主成分数", min_value=2, max_value=5, value=2)
    
    # 生成数据
    np.random.seed(42)
    
    # 生成具有相关性的数据
    mean = np.zeros(n_features)
    cov = np.random.rand(n_features, n_features)
    cov = np.dot(cov, cov.T)  # 确保协方差矩阵正定
    
    X = np.random.multivariate_normal(mean, cov, n_samples)
    
    # 训练模型
    model = PCA(n_components=n_components)
    X_transformed = model.fit_transform(X)
    
    # 显示结果
    st.subheader("运行结果")
    st.write(f"原始数据维度: {X.shape}")
    st.write(f"降维后数据维度: {X_transformed.shape}")
    st.write("各主成分解释方差比例:")
    for i, ratio in enumerate(model.explained_variance_ratio):
        st.write(f"主成分 {i+1}: {ratio:.4f} ({ratio*100:.2f}%)")
    
    total_explained = np.sum(model.explained_variance_ratio)
    st.write(f"累计解释方差比例: {total_explained:.4f} ({total_explained*100:.2f}%)")
    
    # 代码展示
    st.subheader("示例代码")
    code = """
class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None
        self.explained_variance_ratio = None
    
    def fit(self, X):
        # 标准化数据
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # 计算协方差矩阵
        cov_matrix = np.cov(X_centered.T)
        
        # 计算特征值和特征向量
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        
        # 排序特征向量（按特征值降序）
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # 选择前n_components个主成分
        self.components = eigenvectors[:, :self.n_components]
        
        # 计算解释方差比例
        total_variance = np.sum(eigenvalues)
        self.explained_variance_ratio = eigenvalues[:self.n_components] / total_variance
    
    def transform(self, X):
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

# 使用示例
X = np.random.randn(100, 5)
pca = PCA(n_components=2)
X_transformed = pca.fit_transform(X)
print(f"原始维度: {X.shape}, 降维后: {X_transformed.shape}")
"""
    st.code(code, language="python")
    
    # 可视化
    st.subheader("可视化")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 绘制解释方差比例
    ax1.bar(range(1, n_components + 1), model.explained_variance_ratio, alpha=0.8)
    ax1.set_title("各主成分解释方差比例")
    ax1.set_xlabel("主成分")
    ax1.set_ylabel("解释方差比例")
    ax1.set_xticks(range(1, n_components + 1))
    ax1.grid(True)
    
    # 绘制降维后的数据（如果是2维）
    if n_components >= 2:
        ax2.scatter(X_transformed[:, 0], X_transformed[:, 1], alpha=0.6, s=50)
        ax2.set_title("PCA降维结果（前两个主成分）")
        ax2.set_xlabel("主成分 1")
        ax2.set_ylabel("主成分 2")
        ax2.grid(True)
    else:
        ax2.text(0.5, 0.5, "请选择至少2个主成分以查看降维结果", ha='center', va='center', fontsize=12)
        ax2.set_title("PCA降维结果")
    
    st.pyplot(fig)
