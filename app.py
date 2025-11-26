import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Group Project Progress",
    page_icon="🛌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Header ----------------
st.markdown("<h1 style='text-align:center; color:#6a1b9a;'>Group Project: Sleep Health Analysis</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- Project Overview ----------------
st.subheader("Project Overview")
st.write("""
We are working on analyzing the **Sleep Health and Lifestyle Dataset** available on Kaggle:  
[Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
""")

st.write("""
Our project goal is to apply several **computational and statistical methods** to gain insights into sleep health patterns:
""")
st.markdown("""
- **K-means Clustering:** Partition data points into distinct clusters.  
- **EM Clustering:** Model-based clustering for varying cluster sizes/densities.  
- **DBScan Clustering:** Discover clusters of arbitrary shape and detect outliers.  
- **SLINK Clustering:** Hierarchical clustering to build a dendrogram.  
- **Linear Regression:** Quantify linear relationships between variables.  
""")

# ---------------- Group Progress ----------------
st.subheader("Group Progress")
st.write("""
Currently, we are focusing on **data cleaning and preparation**.  
We have practiced and implemented basic data manipulation and visualizations using **pandas** and **matplotlib**.
""")

# ---------------- Static Example Data ----------------
st.subheader("Sample Data Preview")
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

# Histogram of Sleep Duration
fig1 = px.histogram(df, x="Sleep Duration (hrs)", nbins=5, title="Distribution of Sleep Duration")
st.plotly_chart(fig1, use_container_width=True)

# Scatter plot: Sleep vs Exercise
fig2 = px.scatter(df, x="Exercise (hrs/week)", y="Sleep Duration (hrs)", size="Stress Level",
                  color="Stress Level", title="Sleep Duration vs Exercise", size_max=20)
st.plotly_chart(fig2, use_container_width=True)

# ---------------- Placeholder for Clustering ----------------
st.subheader("Clustering Placeholder")
st.write("Here we will display results from K-means, EM, DBScan, and SLINK clustering once implemented.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("K-means Clusters", "3")
col2.metric("EM Clusters", "4")
col3.metric("DBScan Clusters", "3")
col4.metric("SLINK Clusters", "Hierarchical Tree")

# ---------------- Placeholder for Regression ----------------
st.subheader("Linear Regression Placeholder")
st.write("We will analyze linear relationships between variables. Example placeholder:")
st.latex(r"Sleep\ Duration = \beta_0 + \beta_1 \cdot Exercise + \beta_2 \cdot Stress + \epsilon")

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with 💜 using Streamlit • Group Project 2025</p>", unsafe_allow_html=True)
