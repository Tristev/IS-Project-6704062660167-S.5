import streamlit as st

st.set_page_config(page_title="Neural Network Info", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@300;400;500&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); color: #e2e8f0; }
    section[data-testid="stSidebar"] { background: #1e293b; border-right: 1px solid #334155; }

    .page-header {
        background: linear-gradient(135deg, #4c1d95, #6d28d9);
        border-radius: 16px; padding: 36px; margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(109,40,217,0.3);
    }
    .page-header h1 { color: white; font-size: 2rem; margin: 0; }
    .page-header p { color: #ddd6fe; margin: 8px 0 0; }

    .section-card {
        background: #1e293b; border: 1px solid #334155;
        border-radius: 14px; padding: 28px; margin-bottom: 20px;
    }
    .section-card h2 { color: #a78bfa; font-size: 1.2rem; margin-bottom: 14px; }
    .section-card p, .section-card li { color: #94a3b8; line-height: 1.8; }

    .layer-box {
        background: #0f172a; border-left: 4px solid #7c3aed;
        border-radius: 8px; padding: 16px 20px; margin: 8px 0;
        display: flex; align-items: flex-start; gap: 16px;
    }
    .layer-num { color: #a78bfa; font-weight: 700; font-family: 'Space Grotesk', sans-serif; min-width: 80px; }
    .layer-desc { color: #94a3b8; font-size: 0.9rem; line-height: 1.6; }
    .layer-desc strong { color: #e2e8f0; }

    .tag {
        display: inline-block; background: #2e1065; color: #a78bfa;
        border-radius: 6px; padding: 3px 10px; font-size: 0.8rem; margin: 3px;
    }
    hr { border: none; border-top: 1px solid #334155; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="page-header">
    <h1>🧠 Model 2 — Neural Network</h1>
    <p>Custom-designed deep neural network built with TensorFlow and Keras</p>
</div>
""", unsafe_allow_html=True)


# ── Section 1: What is a Neural Network ──────────────────────
st.markdown("""
<div class="section-card">
    <h2>💡 1. What is a Neural Network?</h2>
    <p>A <strong style="color:#e2e8f0;">Neural Network</strong> is a machine learning model inspired by how the human brain works.
    It is made up of layers of "neurons" (nodes) that are connected to each other.</p>
    <p>Data flows in through the <strong style="color:#e2e8f0;">input layer</strong>, passes through one or more
    <strong style="color:#e2e8f0;">hidden layers</strong> where patterns are learned, and exits through the
    <strong style="color:#e2e8f0;">output layer</strong> which gives the final prediction.</p>
    <p>During training, the network adjusts the strength of connections between neurons (called <strong style="color:#e2e8f0;">weights</strong>)
    to minimize prediction errors — this process is called <strong style="color:#e2e8f0;">backpropagation</strong>.</p>
</div>
""", unsafe_allow_html=True)


# ── Section 2: Dataset ────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>📊 2. Dataset Used</h2>
    <p>The same cleaned Dataset 2 (<strong style="color:#e2e8f0;">Student Performance Factors</strong>) was used for the neural network.</p>
    <ul>
        <li>6,607 student records after cleaning</li>
        <li>19 input features (all text columns encoded, numeric columns scaled)</li>
        <li>Target: Pass (1) or Fail (0) based on Exam_Score ≥ 60</li>
        <li>80% / 20% train-test split</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# ── Section 3: Architecture ───────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>🏗️ 3. Network Architecture</h2>
    <p>The network was custom-designed for this binary classification task (Pass/Fail):</p>
</div>
""", unsafe_allow_html=True)

layers = [
    ("Input Layer", "Dense(128)", "relu", "Receives all 19 features. 128 neurons learn broad patterns from the data. ReLU activation removes negative values, helping the network focus on positive signals."),
    ("Dropout 1", "Dropout(0.3)", "—", "Randomly turns off 30% of neurons during each training step. This prevents the network from memorizing the training data (overfitting)."),
    ("Hidden Layer", "Dense(64)", "relu", "64 neurons refine the patterns learned by the first layer. The network gets more specific here."),
    ("Dropout 2", "Dropout(0.2)", "—", "Randomly turns off 20% of neurons. Lighter dropout since we're deeper in the network."),
    ("Hidden Layer 2", "Dense(32)", "relu", "32 neurons further compress the learned representation into key decision factors."),
    ("Output Layer", "Dense(1)", "sigmoid", "Single neuron with sigmoid activation. Outputs a number between 0 and 1 — the probability of passing. ≥ 0.5 = Pass, < 0.5 = Fail."),
]

for name, config, activation, explanation in layers:
    st.markdown(f"""
    <div class="layer-box">
        <div class="layer-num">{name}</div>
        <div class="layer-desc">
            <strong>{config}</strong> · Activation: <strong>{activation}</strong><br>
            {explanation}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Section 4: Training ───────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="section-card">
    <h2>⚙️ 4. Training Configuration</h2>
    <ul>
        <li><strong style="color:#e2e8f0;">Optimizer:</strong> Adam — automatically adjusts the learning rate during training</li>
        <li><strong style="color:#e2e8f0;">Loss Function:</strong> Binary Crossentropy — measures error for Pass/Fail (0 or 1) predictions</li>
        <li><strong style="color:#e2e8f0;">Epochs:</strong> 50 — the model goes through all training data 50 times</li>
        <li><strong style="color:#e2e8f0;">Batch Size:</strong> 32 — updates weights after every 32 samples</li>
        <li><strong style="color:#e2e8f0;">Validation Split:</strong> 20% of training data is held out each epoch to monitor learning</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# ── Section 5: Development Steps ─────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>🔧 5. Development Steps</h2>
    <ol>
        <li>Load <code>cleaned_df2.csv</code> and separate X (features) and y (result)</li>
        <li>Split 80% train / 20% test using <code>train_test_split</code></li>
        <li>Convert to numpy arrays with <code>.values</code></li>
        <li>Build the model using <code>keras.Sequential()</code> with the layers above</li>
        <li>Compile with <code>optimizer='adam'</code> and <code>loss='binary_crossentropy'</code></li>
        <li>Train with <code>model.fit()</code> for 50 epochs</li>
        <li>Evaluate accuracy on the test set</li>
        <li>Save the trained model as <code>model2_nn.h5</code></li>
    </ol>
</div>
""", unsafe_allow_html=True)


# ── Section 6: Results ────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>📋 6. Model Results</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Test Accuracy", "~87%", help="Percentage of correct Pass/Fail predictions")
with col2:
    st.metric("Epochs Trained", "50")
with col3:
    st.metric("Total Parameters", "~22,000", help="Number of learnable weights in the network")

st.info("💡 Note: Your actual accuracy will appear in the Colab output. Update these numbers to match your real results.")


# ── Section 7: References ─────────────────────────────────────
st.markdown("""
<div class="section-card">
    <h2>🔗 7. References</h2>
    <ul>
        <li>Dataset: <a href="https://www.kaggle.com/datasets/lainguyn123/student-performance-factors" style="color:#a78bfa;">Student Performance Factors — Kaggle</a></li>
        <li>TensorFlow/Keras: <a href="https://www.tensorflow.org/api_docs/python/tf/keras" style="color:#a78bfa;">tensorflow.org</a></li>
        <li>Keras Sequential Model: <a href="https://keras.io/guides/sequential_model/" style="color:#a78bfa;">keras.io</a></li>
        <li>Dropout layer: <a href="https://keras.io/api/layers/regularization_layers/dropout/" style="color:#a78bfa;">Keras Dropout docs</a></li>
        <li>Binary Crossentropy loss: <a href="https://keras.io/api/losses/probabilistic_losses/#binarycrossentropy-class" style="color:#a78bfa;">Keras Loss docs</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)
