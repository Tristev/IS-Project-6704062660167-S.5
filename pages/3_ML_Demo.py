import streamlit as st
import pickle
import numpy as np
import os

st.set_page_config(page_title="ML Demo", page_icon="🤖", layout="wide")

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

    .result-pass {
        background: linear-gradient(135deg, #064e3b, #065f46);
        border: 2px solid #34d399; border-radius: 16px; padding: 30px;
        text-align: center; margin-top: 20px;
    }
    .result-fail {
        background: linear-gradient(135deg, #450a0a, #7f1d1d);
        border: 2px solid #f87171; border-radius: 16px; padding: 30px;
        text-align: center; margin-top: 20px;
    }
    .result-title { font-size: 2.5rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; }
    .result-subtitle { color: #94a3b8; font-size: 1rem; margin-top: 8px; }

    .input-section {
        background: #1e293b; border: 1px solid #334155;
        border-radius: 14px; padding: 24px; margin-bottom: 20px;
    }
    .input-section h3 { color: #34d399; font-size: 1rem; margin-bottom: 16px; font-family: 'Space Grotesk', sans-serif; }
    hr { border: none; border-top: 1px solid #334155; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <h1>🤖 Test Ensemble ML Model</h1>
    <p>Fill in student information below and click Predict to get a Pass/Fail result</p>
</div>
""", unsafe_allow_html=True)


# ── Load models ───────────────────────────────────────────────
@st.cache_resource
def load_models():
    with open('model1_ensemble.pkl', 'rb') as f:
        ensemble = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    return ensemble, scaler, label_encoders

try:
    ensemble, scaler, label_encoders = load_models()
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Could not load model files. Make sure model1_ensemble.pkl, scaler.pkl, and label_encoders.pkl are in the same folder as app.py.\n\nError: {e}")
    st.stop()


# ── Helper: encode a text value using saved encoder ───────────
def encode(col, value):
    le = label_encoders[col]
    return int(le.transform([value])[0])


# ── Input Form ────────────────────────────────────────────────
st.markdown("### 📝 Enter Student Information")

with st.container():
    st.markdown('<div class="input-section"><h3>👤 Personal Information</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        internet = st.selectbox("Internet Access at Home", ["Yes", "No"])
    with col3:
        school_type = st.selectbox("School Type", ["Public", "Private"])
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-section"><h3>📚 Study Habits</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        hours_studied = st.slider("Hours Studied per Week", 1, 44, 20)
    with col2:
        attendance = st.slider("Attendance (%)", 60, 100, 80)
    with col3:
        sleep_hours = st.slider("Sleep Hours per Night", 4, 10, 7)
    col4, col5 = st.columns(2)
    with col4:
        tutoring = st.slider("Tutoring Sessions per Month", 0, 8, 2)
    with col5:
        physical = st.slider("Physical Activity (hours/week)", 0, 6, 3)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-section"><h3>🏠 Family & Background</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        parental_inv = st.selectbox("Parental Involvement", ["High", "Medium", "Low"])
    with col2:
        family_income = st.selectbox("Family Income Level", ["High", "Medium", "Low"])
    with col3:
        parental_edu = st.selectbox("Parental Education Level", ["Postgraduate", "College", "High School"])
    col4, col5 = st.columns(2)
    with col4:
        distance = st.selectbox("Distance from Home to School", ["Near", "Moderate", "Far"])
    with col5:
        learning_dis = st.selectbox("Learning Disabilities", ["No", "Yes"])
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-section"><h3>🎯 Academic Environment</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        access_res = st.selectbox("Access to Learning Resources", ["High", "Medium", "Low"])
    with col2:
        motivation = st.selectbox("Motivation Level", ["High", "Medium", "Low"])
    with col3:
        teacher_q = st.selectbox("Teacher Quality", ["High", "Medium", "Low"])
    col4, col5 = st.columns(2)
    with col4:
        extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    with col5:
        peer_influence = st.selectbox("Peer Influence", ["Positive", "Neutral", "Negative"])
    st.markdown('</div>', unsafe_allow_html=True)

previous_scores = st.slider("Previous Exam Score (0–100)", 50, 100, 70)


# ── Predict ───────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮 Predict with Ensemble Model", use_container_width=True):

    # Build the input feature array in the SAME order as training columns
    # Numeric cols that were scaled: Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Tutoring_Sessions, Physical_Activity
    num_values = np.array([[hours_studied, attendance, sleep_hours, previous_scores, tutoring, physical]])
    scaled_nums = scaler.transform(num_values)[0]

    # Encode all text columns
    features = {
        'Hours_Studied':            scaled_nums[0],
        'Attendance':               scaled_nums[1],
        'Parental_Involvement':     encode('Parental_Involvement', parental_inv),
        'Access_to_Resources':      encode('Access_to_Resources', access_res),
        'Extracurricular_Activities': encode('Extracurricular_Activities', extracurricular),
        'Sleep_Hours':              scaled_nums[2],
        'Previous_Scores':          scaled_nums[3],
        'Motivation_Level':         encode('Motivation_Level', motivation),
        'Internet_Access':          encode('Internet_Access', internet),
        'Tutoring_Sessions':        scaled_nums[4],
        'Family_Income':            encode('Family_Income', family_income),
        'Teacher_Quality':          encode('Teacher_Quality', teacher_q),
        'School_Type':              encode('School_Type', school_type),
        'Peer_Influence':           encode('Peer_Influence', peer_influence),
        'Physical_Activity':        scaled_nums[5],
        'Learning_Disabilities':    encode('Learning_Disabilities', learning_dis),
        'Parental_Education_Level': encode('Parental_Education_Level', parental_edu),
        'Distance_from_Home':       encode('Distance_from_Home', distance),
        'Gender':                   encode('Gender', gender),
    }

    X_input = np.array([list(features.values())])
    prediction = ensemble.predict(X_input)[0]
    probability = ensemble.predict_proba(X_input)[0]

    pass_prob = round(probability[1] * 100, 1)
    fail_prob = round(probability[0] * 100, 1)

    if prediction == 1:
        st.markdown(f"""
        <div class="result-pass">
            <div class="result-title" style="color:#34d399;">✅ PASS</div>
            <div class="result-subtitle">The model predicts this student will pass the exam</div>
            <br>
            <div style="color:#6ee7b7; font-size:1.2rem; font-weight:600;">
                Pass Probability: {pass_prob}% &nbsp;|&nbsp; Fail Probability: {fail_prob}%
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-fail">
            <div class="result-title" style="color:#f87171;">❌ FAIL</div>
            <div class="result-subtitle">The model predicts this student will not pass the exam</div>
            <br>
            <div style="color:#fca5a5; font-size:1.2rem; font-weight:600;">
                Pass Probability: {pass_prob}% &nbsp;|&nbsp; Fail Probability: {fail_prob}%
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.progress(pass_prob / 100, text=f"Pass: {pass_prob}%")
    with col2:
        st.progress(fail_prob / 100, text=f"Fail: {fail_prob}%")
