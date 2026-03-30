import streamlit as st

st.set_page_config(page_title="ML Model Info", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@300;400;500&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); color: #e2e8f0; }
    section[data-testid="stSidebar"] { background: #1e293b; border-right: 1px solid #334155; }

    .page-header {
        background: linear-gradient(135deg, #065f46, #047857);
        border-radius: 16px; padding: 36px; margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(4,120,87,0.3);
    }
    .page-header h1 { color: white; font-size: 2rem; margin: 0; }
    .page-header p { color: #a7f3d0; margin: 8px 0 0; }

    .section-card {
        background: #1e293b; border: 1px solid #334155;
        border-radius: 14px; padding: 28px; margin-bottom: 20px;
    }
    .section-card h2 { color: #34d399; font-size: 1.2rem; margin-bottom: 14px; }
    .section-card p, .section-card li { color: #94a3b8; line-height: 1.8; }

    .model-box {
        background: #0f172a; border: 1px solid #334155;
        border-radius: 10px; padding: 18px; margin: 10px 0;
    }
    .model-box h4 { color: #6ee7b7; margin: 0 0 8px; font-family: 'Space Grotesk', sans-serif; }
    .model-box p { color: #94a3b8; font-size: 0.9rem; margin: 0; }

    .tag {
        display: inline-block; background: #064e3b; color: #34d399;
        border-radius: 6px; padding: 3px 10px; font-size: 0.8rem;
        margin: 3px; font-family: 'Space Grotesk', sans-serif;
    }
    hr { border: none; border-top: 1px solid #334155; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1>🤖 Model 1 — Ensemble Machine Learning</h1>
    <p>How the Voting Classifier was built, trained, and evaluated</p>
</div>
""", unsafe_allow_html=True)


# ── Section 1: Datasets ──────────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>📊 1. Data Sources</h2>
    <p>Two datasets were used for this project:</p>
    <ul>
        <li><strong style="color:#e2e8f0;">Dataset 1 — Students Performance in Exams</strong><br>
            Source: Kaggle (spscientist) · 1,000 rows · 8 columns<br>
            Features: gender, race/ethnicity, parental education, lunch type, test preparation, math/reading/writing scores</li>
        <br>
        <li><strong style="color:#e2e8f0;">Dataset 2 — Student Performance Factors</strong><br>
            Source: Kaggle (lainguyn123) · 6,607 rows · 20 columns<br>
            Features: hours studied, attendance, parental involvement, sleep hours, motivation level, exam score, and more</li>
    </ul>
    <p>Dataset 2 was used as the primary training dataset because it is larger and contains more relevant features.</p>
</div>
""", unsafe_allow_html=True)


# ── Section 2: Data Preparation ──────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>🧹 2. Data Preparation Steps</h2>
    <p>The following steps were applied to clean and prepare the data:</p>
    <ol>
        <li><strong style="color:#e2e8f0;">Explore missing values</strong> — used <code>isnull().sum()</code> to find gaps in Teacher_Quality, Parental_Education_Level, and Distance_from_Home</li>
        <li><strong style="color:#e2e8f0;">Fill missing values</strong> — replaced with the most common value (mode) for each column</li>
        <li><strong style="color:#e2e8f0;">Encode text columns</strong> — converted 13 categorical text columns to numbers using LabelEncoder (e.g. "Male"→1, "Female"→0)</li>
        <li><strong style="color:#e2e8f0;">Scale numeric columns</strong> — applied StandardScaler to Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Tutoring_Sessions, Physical_Activity</li>
        <li><strong style="color:#e2e8f0;">Create target column</strong> — Exam_Score ≥ 60 → Pass (1), else Fail (0)</li>
    </ol>
</div>
""", unsafe_allow_html=True)


# ── Section 3: Algorithm Theory ──────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>📐 3. Algorithm Theory — Voting Ensemble</h2>
    <p>An <strong style="color:#e2e8f0;">Ensemble model</strong> combines multiple models so their predictions are merged into one final result. This is more accurate than using any single model alone, because different models learn different patterns.</p>
    <p>We used a <strong style="color:#e2e8f0;">Soft Voting Classifier</strong> — each model outputs a probability score (not just "yes/no"), and the average probability is used to make the final decision.</p>
    <br>
    <p>The three models inside the ensemble:</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="model-box">
        <h4>🌲 Random Forest</h4>
        <p>Builds many decision trees on random subsets of the data, then averages their results. Strong against overfitting.</p>
        <br><span class="tag">100 trees</span><span class="tag">Ensemble base</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="model-box">
        <h4>📈 Gradient Boosting</h4>
        <p>Builds trees one by one, where each new tree learns from the errors of the previous one. Very accurate on structured data.</p>
        <br><span class="tag">100 estimators</span><span class="tag">Sequential learning</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="model-box">
        <h4>📊 Logistic Regression</h4>
        <p>A classic, simple statistical model for binary classification (Pass/Fail). Fast and interpretable. Provides a strong baseline.</p>
        <br><span class="tag">Linear boundary</span><span class="tag">Probabilistic</span>
    </div>
    """, unsafe_allow_html=True)


# ── Section 4: Development Steps ─────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="section-card">
    <h2>🔧 4. Development Steps</h2>
    <ol>
        <li>Load <code>cleaned_df2.csv</code></li>
        <li>Separate features (X) and target label (y = result column)</li>
        <li>Split 80% training / 20% testing using <code>train_test_split</code></li>
        <li>Create 3 base models: RandomForestClassifier, GradientBoostingClassifier, LogisticRegression</li>
        <li>Combine into <code>VotingClassifier(voting='soft')</code></li>
        <li>Train with <code>ensemble.fit(X_train, y_train)</code></li>
        <li>Evaluate on test set using accuracy score and classification report</li>
        <li>Save the trained model as <code>model1_ensemble.pkl</code> using pickle</li>
    </ol>
</div>
""", unsafe_allow_html=True)


# ── Section 5: Results ────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>📋 5. Model Results</h2>
    <p>After training, the model was evaluated on the 20% test set (unseen data).</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Test Accuracy", "~89%", help="Percentage of correct Pass/Fail predictions")
with col2:
    st.metric("Training Size", "5,285 rows", help="80% of 6,607 samples")
with col3:
    st.metric("Test Size", "1,322 rows", help="20% of 6,607 samples")

st.info("💡 Note: Your actual accuracy will appear in the Colab output when you run the model notebook. Update these numbers to match your real results.")


# ── Section 6: References ─────────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>🔗 6. References</h2>
    <ul>
        <li>Dataset 1: <a href="https://www.kaggle.com/datasets/spscientist/students-performance-in-exams" style="color:#34d399;">Students Performance in Exams — Kaggle</a></li>
        <li>Dataset 2: <a href="https://www.kaggle.com/datasets/lainguyn123/student-performance-factors" style="color:#34d399;">Student Performance Factors — Kaggle</a></li>
        <li>Scikit-learn VotingClassifier: <a href="https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier" style="color:#34d399;">scikit-learn.org</a></li>
        <li>Random Forest: <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html" style="color:#34d399;">RandomForestClassifier docs</a></li>
        <li>Gradient Boosting: <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html" style="color:#34d399;">GradientBoostingClassifier docs</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)
