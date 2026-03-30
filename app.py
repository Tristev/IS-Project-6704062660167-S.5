import streamlit as st

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #e2e8f0;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #1e293b;
        border-right: 1px solid #334155;
    }

    /* Hero card */
    .hero-card {
        background: linear-gradient(135deg, #1e40af, #7c3aed);
        border-radius: 20px;
        padding: 50px 40px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 20px 60px rgba(124,58,237,0.3);
    }
    .hero-card h1 {
        font-size: 2.8rem;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }
    .hero-card p {
        font-size: 1.1rem;
        color: #c7d2fe;
        max-width: 600px;
        margin: 0 auto;
    }

    /* Info card */
    .info-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 28px;
        height: 100%;
        transition: border-color 0.2s;
    }
    .info-card:hover {
        border-color: #7c3aed;
    }
    .info-card h3 {
        color: #a78bfa;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }
    .info-card p {
        color: #94a3b8;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* Step badge */
    .step-badge {
        display: inline-block;
        background: #7c3aed;
        color: white;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        line-height: 32px;
        text-align: center;
        font-weight: 700;
        margin-right: 10px;
        font-size: 0.9rem;
    }

    /* Divider */
    hr {
        border: none;
        border-top: 1px solid #334155;
        margin: 30px 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
    <h1>🎓 Student Score Predictor</h1>
    <p>An IS 2568 Machine Learning Project — predicting student exam outcomes
    using Ensemble ML and Neural Network models trained on real student data.</p>
</div>
""", unsafe_allow_html=True)

# ── Overview cards ───────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>📊 Datasets</h3>
        <p>2 real Kaggle datasets with missing values, cleaned and merged for training.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🤖 Ensemble ML</h3>
        <p>Voting Classifier combining Random Forest, Gradient Boosting, and Logistic Regression.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🧠 Neural Network</h3>
        <p>Custom-designed deep neural network with dropout layers built with TensorFlow/Keras.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <h3>🌐 Live Demo</h3>
        <p>Enter student data and get a real-time Pass/Fail prediction from both models.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ── Navigation guide ─────────────────────────────────────────
st.markdown("### 📌 How to Navigate")
st.markdown("Use the **sidebar on the left** to go to each page:")

steps = [
    ("1 — ML Model Info", "Read about the Ensemble ML model: data prep, algorithm theory, and results."),
    ("2 — Neural Network Info", "Read about the Neural Network model: architecture, training process, and results."),
    ("3 — ML Demo", "Test the Ensemble ML model live — enter student data and get a prediction."),
    ("4 — NN Demo", "Test the Neural Network model live — same input, different model."),
]

for step, desc in steps:
    st.markdown(f"""
    <div style="display:flex; align-items:flex-start; margin-bottom:16px; background:#1e293b;
                border-radius:12px; padding:16px 20px; border:1px solid #334155;">
        <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#a78bfa;
                    min-width:180px; font-size:0.95rem;">📄 {step}</div>
        <div style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#475569; font-size:0.85rem;">
    IS 2568 Project · Student Score Prediction · Built with Streamlit + TensorFlow + Scikit-learn
</div>
""", unsafe_allow_html=True)
