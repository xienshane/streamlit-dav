import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.linear_model import LinearRegression

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------
st.set_page_config(
    page_title="Sleep Health Dashboard",
    page_icon="😴",
    layout="wide"
)

# ----------------------------------------
# CUSTOM CSS
# ----------------------------------------
st.markdown("""
<style>
    body {
        background-color: #faf6ff;
    }
    .section-title {
        font-size: 2rem;
        color: #7d3c98;
        font-weight: bold;
        margin-top: 30px;
        border-left: 6px solid #a569bd;
        padding-left: 12px;
    }
    .card {
        background-color: #f3e9ff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #9b59b6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .profile-card {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        border: 2px solid #d9c4ff;
        text-align: center;
        box-shadow: 0 2px 10px rgba(90,0,120,0.1);
    }
</style>
""", unsafe_allow_html=True)


# ----------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", [
    "📊 Project Overview",
    "🧑‍🤝‍🧑 Group Members",
    "📁 Dataset",
    "⚙️ Clustering Models",
    "📉 Linear Regression"
])


# ==========================================================
# PAGE 1 — PROJECT OVERVIEW
# ==========================================================
if page == "📊 Project Overview":
    st.markdown("<h1 style='text-align:center;color:#8e44ad;'>😴 Sleep Health & Lifestyle — Group Dashboard</h1>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>📁 Dataset Selected</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='card'>
        <h3>🛌 Sleep Health and Lifestyle Dataset</h3>
        <p>From Kaggle — contains sleep duration, stress, physical activity, and other lifestyle factors.</p>
        <a href='https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset' target='_blank'>
            🔗 Open Dataset on Kaggle</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🔧 Methods We Will Use</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
            <h4>📌 K-means Clustering</h4>
            <p>Groups sleep patterns using centroid-based clustering.</p>

            <h4>📌 EM Clustering</h4>
            <p>Gaussian Mixture Model — soft assignments for flexible clusters.</p>

            <h4>📌 DBSCAN</h4>
            <p>Discovers noise and arbitrarily shaped clusters.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <h4>📌 SLINK (Hierarchical)</h4>
            <p>Builds dendrogram relationship structure.</p>

            <h4>📌 Linear Regression</h4>
            <p>Models linear relationships between lifestyle variables.</p>
        </div>
        """, unsafe_allow_html=True)

    # timeline progress
    st.markdown("<div class='section-title'>📈 Project Timeline Progress</div>", unsafe_allow_html=True)

    progress_data = {
        "Dataset Selection": 100,
        "Data Cleaning": 40,
        "Exploratory Analysis": 25,
        "Clustering Models": 10,
        "Regression Modeling": 5,
        "Streamlit UI": 35
    }

    for task, pct in progress_data.items():
        st.write(f"**{task}**")
        st.progress(pct / 100)

    # Placeholder chart
    st.markdown("<div class='section-title'>📊 Sample Placeholder Chart</div>", unsafe_allow_html=True)
    fake_data = np.random.randint(5, 10, 7)
    fig = px.line(x=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                  y=fake_data, markers=True,
                  title="Sample Sleep Hours Visualization")
    st.plotly_chart(fig, use_container_width=True)


# ==========================================================
# PAGE 2 — GROUP MEMBERS
# ==========================================================
elif page == "🧑‍🤝‍🧑 Group Members":
    st.markdown("<h1 style='text-align:center;color:#8e44ad;'>🧑‍🤝‍🧑 Meet the Team</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='profile-card'>
            <h3>Lovely Shane Ong</h3>
            <p>📘 Data Cleaning • Clustering Implementation</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='profile-card'>
            <h3>Group Member 2</h3>
            <p>📘 Model Research • Dataset Analysis</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='profile-card'>
            <h3>Group Member 3</h3>
            <p>📘 Streamlit UI • Visualization</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================================
# PAGE 3 — DATASET
# ==========================================================
elif page == "📁 Dataset":
    st.markdown("<h1 style='color:#8e44ad;'>📁 Upload & Preview Dataset</h1>", unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload Sleep Dataset (CSV)", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.success("Dataset uploaded!")

        st.write("### 🔍 Data Preview")
        st.dataframe(df.head())

        st.write("### 📊 Basic Statistics")
        st.write(df.describe())

        st.write("### 🔢 Column List")
        st.write(df.columns.tolist())

        st.session_state["df"] = df
    else:
        st.info("Upload the dataset to proceed.")


# ==========================================================
# PAGE 4 — CLUSTERING MODELS
# ==========================================================
elif page == "⚙️ Clustering Models":
    st.markdown("<h1 style='color:#8e44ad;'>⚙️ Clustering Analysis</h1>", unsafe_allow_html=True)

    if "df" not in st.session_state:
        st.error("⚠️ Please upload the dataset first in the 'Dataset' page.")
    else:
        df = st.session_state["df"]

        numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

        st.write("### Select Features for Clustering")
        selected = st.multiselect("Choose numeric columns:", numeric_cols)

        algorithm = st.selectbox("Choose clustering method:", [
            "K-means",
            "EM (Gaussian Mixture)",
            "DBSCAN",
            "Hierarchical (SLINK)"
        ])

        if st.button("Run Clustering"):
            data = df[selected].dropna()

            if algorithm == "K-means":
                model = KMeans(n_clusters=3)
                df["Cluster"] = model.fit_predict(data)
            elif algorithm == "EM (Gaussian Mixture)":
                model = GaussianMixture(n_components=3)
                df["Cluster"] = model.fit_predict(data)
            elif algorithm == "DBSCAN":
                model = DBSCAN(eps=1.5, min_samples=5)
                df["Cluster"] = model.fit_predict(data)
            else:  # hierarchical
                model = AgglomerativeClustering(n_clusters=3)
                df["Cluster"] = model.fit_predict(data)

            st.success("Clustering complete!")
            fig = px.scatter(df, x=selected[0], y=selected[1], color=df["Cluster"], title="Cluster Result")
            st.plotly_chart(fig)


# ==========================================================
# PAGE 5 — LINEAR REGRESSION
# ==========================================================
elif page == "📉 Linear Regression":
    st.markdown("<h1 style='color:#8e44ad;'>📉 Linear Regression Model</h1>", unsafe_allow_html=True)

    if "df" not in st.session_state:
        st.error("⚠️ Please upload a dataset first.")
    else:
        df = st.session_state["df"]
        numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

        target = st.selectbox("Target Variable:", numeric_cols)
        feature = st.selectbox("Feature Variable:", numeric_cols)

        if st.button("Run Regression"):
            X = df[[feature]]
            y = df[target]

            model = LinearRegression()
            model.fit(X, y)

            df["Predicted"] = model.predict(X)

            fig = px.scatter(df, x=feature, y=target, title="Linear Regression")
            fig.add_traces(px.line(df, x=feature, y="Predicted").data)

            st.plotly_chart(fig)
            st.write(f"### Coefficient: {model.coef_[0]:.3f}")
            st.write(f"### Intercept: {model.intercept_:.3f}")
