import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Group Project Progress",
    page_icon="🛌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS Styling ----------------
st.markdown("""
<style>
/* Main header */
.main-header {
    font-size: 3rem;
    color: #6a1b9a;
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Segoe UI', sans-serif;
}

/* Section headers */
.section-header {
    font-size: 2rem;
    color: #8e44ad;
    border-bottom: 2px solid #8e44ad;
    padding-bottom: 0.5rem;
    margin-top: 2rem;
    font-family: 'Segoe UI', sans-serif;
}

/* Cards */
.card {
    background-color: #f5f0fa;
    border-left: 5px solid #9b59b6;
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}

/* Metrics style */
.metric-card {
    background-color: #e0d9f0;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    color: #6a1b9a;
    font-weight: bold;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}

/* Footer */
.footer {
    color: gray;
    text-align: center;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown('<div class="main-header">🛌 Group Project: Sleep Health Analysis</div>', unsafe_allow_html=True)
st.markdown("---")

# ---------------- Project Overview ----------------
st.subheader("Project Overview")
st.write("""
We are analyzing the **Sleep Health and Lifestyle Dataset** from Kaggle:  
[Dataset Link](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
""")
st.write("""
Our project goal is to explore sleep patterns using several **computational methods**:
""")
st.markdown("""
- **K-means Clustering**  
- **EM Clustering**  
- **DBScan Clustering**  
- **SLINK Clustering (Hierarchical)**  
- **Linear Regression**
""")

# ---------------- Group Progress ----------------
st.subheader("Current Progress")
st.write("""
Our focus is on **data cleaning and preparation**.  
We’ve practiced **data manipulation** and **basic visualizations** using `pandas` and `matplotlib`.
""")

# ---------------- Sample Data Preview ----------------
st.subheader("Sample Dataset Preview")
data = {
    "ID": [1, 2, 3, 4, 5],
    "Age": [25, 30, 22, 28, 35],
    "Sleep Duration (hrs)": [7, 6, 8, 5, 7],
    "Exercise (hrs/week)": [3, 1, 2, 4, 1],
    "Stress Level": [2, 4, 3, 5, 3]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# ---------------- Placeholder Visualizations ----------------
st.subheader("Example Visualizations")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(df, x="Sleep Duration (hrs)", nbins=5,
                        title="Distribution of Sleep Duration", color_discrete_sequence=["#9b59b6"])
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(df, x="Exercise (hrs/week)", y="Sleep Duration (hrs)",
                      size="Stress Level", color="Stress Level",
                      color_continuous_scale="Purples", size_max=25,
                      title="Sleep Duration vs Exercise")
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- Clustering Methods ----------------
st.subheader("Clustering Methods Progress")

cluster_cols = st.columns(4)
cluster_names = ["K-means", "EM", "DBScan", "SLINK"]
cluster_values = [3, 4, 3, "Hierarchical Tree"]

for i, col in enumerate(cluster_cols):
    col.markdown(f'<div class="metric-card">{cluster_names[i]}<br><h3>{cluster_values[i]}</h3></div>', unsafe_allow_html=True)

# ---------------- Linear Regression Placeholder ----------------
st.subheader("Linear Regression Placeholder")
st.write("We will analyze linear relationships between variables. Example formula:")
st.latex(r"Sleep\ Duration = \beta_0 + \beta_1 \cdot Exercise + \beta_2 \cdot Stress + \epsilon")

# ---------------- Footer ----------------
st.markdown("---")
st.markdown('<p class="footer">Made with 💜 using Streamlit • Group Project 2025</p>', unsafe_allow_html=True)
