import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# CYBERPUNK DEEP DARK THEME CSS
# -------------------------------------------------------
st.markdown("""
<style>
#MainMenu, footer, header

/* Deep Cyber Background */
.stApp {
    background: radial-gradient(circle at top right, #1E1B4B, #0F172A 60%);
    color: #F8FAFC;
}

/* Sidebar Custom Styling */
section[data-testid="stSidebar"] {
    background-color: #0B0F19 !important;
    border-right: 1px solid #1E293B;
}

/* Stunning Hero Header Card */
.hero {
    background: linear-gradient(135deg, #1E1B4B 0%, #311042 100%);
    padding: 40px;
    border-radius: 24px;
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 300px; height: 300px;
    background: rgba(236, 72, 153, 0.15);
    filter: blur(80px);
    border-radius: 50%;
}

.title {
    font-size: 42px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.5px;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 18px;
    color: #94A3B8;
}

/* Cyber Glass Card Panels */
.card {
    background: rgba(15, 23, 42, 0.6);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    height: 260px;
}

.card:hover {
    transform: translateY(-8px);
    border-color: rgba(99, 102, 241, 0.4);
    box-shadow: 0 15px 35px rgba(99, 102, 241, 0.15);
}

.card h2 {
    font-size: 24px !important;
    font-weight: 700 !important;
    margin-bottom: 15px !important;
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #38BDF8;
    margin-top: 40px;
    margin-bottom: 20px;
}

.custom-bullet {
    padding: 8px 12px;
    margin: 6px 0;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.02);
    border-left: 3px solid #6366F1;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Hero Component
st.markdown("""
<div class="hero">
    <div class="title">🎯 Customer Segmentation Dashboard</div>
    <div class="subtitle">Understand your customers better with RFM Analysis and K-Means Clustering</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">📖 Core Objectives</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="card">
        <h2 style="color: #FBBF24;">🎯 Business Intent</h2>
        <div class="custom-bullet">✔ Behavioral Profiling</div>
        <div class="custom-bullet">✔ Identify Premium Cohorts</div>
        <div class="custom-bullet">✔ Maximize Attrition Protection</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h2 style="color: #34D399;">🤖 ML Engineering</h2>
        <div class="custom-bullet">✔ Mathematical RFM Metrics</div>
        <div class="custom-bullet">✔ Optimal Elbow Optimization</div>
        <div class="custom-bullet">✔ K-Means Clustering Core</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h2 style="color: #38BDF8;">📊 Interactive UI</h2>
        <div class="custom-bullet">✔ High-Contrast Graphing</div>
        <div class="custom-bullet">✔ Dynamic Metric Filtering</div>
        <div class="custom-bullet">✔ Instant Report Generation</div>
    </div>
    """, unsafe_allow_html=True)