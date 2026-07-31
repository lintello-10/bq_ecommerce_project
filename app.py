import streamlit as st
import pandas as pd
import joblib

# Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="E-commerce Conversion Predictor",
    page_icon="🛍️",
    layout="wide", # Uses the full width of the screen
    initial_sidebar_state="expanded"
)

# Customing CSS to inject some aesthetic styling
st.markdown("""
    <style>
    /* Make the predict button span full width and look modern */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #FF6666;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Model Loading Strategy
@st.cache_resource # Caches the model so it loads only once per session
def load_model():
    return joblib.load('xgboost_ecommerce_pipeline.pkl')

# Safely load the pipeline
try:
    pipeline = load_model()
except Exception as e:
    st.error(f"Error loading the model: {e}. Please ensure 'xgboost_ecommerce_pipeline.pkl' is in the same directory.")
    st.stop()

# Main Application Header
st.title("🛍️ E-commerce Conversion Dashboard ")
st.markdown("### Predict the likelihood of a user completing a purchase based on their session activity.")
st.divider() # Adds a clean horizontal line

# Sidebar for User Inputs
st.sidebar.header("⚙️ User Session Activity")
st.sidebar.markdown("Adjust the sliders to simulate user behavior.")

def get_user_inputs():
    # Numerical sliders for user session metrics
    view_item = st.sidebar.slider("Number of items viewed", min_value=0, max_value=50, value=5)
    add_to_cart = st.sidebar.slider("Number of items added to cart", min_value=0, max_value=20, value=1)
    begin_checkout = st.sidebar.slider("Number of checkout attempts", min_value=0, max_value=10, value=0)
    
    # Categorical selectors
    device_category = st.sidebar.selectbox("Device Category", ["desktop", "mobile", "tablet"])
    traffic_medium = st.sidebar.selectbox("Traffic Medium", ["organic", "cpc", "referral", "none"])
    
    # Top 10 countries mapping
    country_mapping = {
        "Bahrain": 0,
        "Macao": 1,
        "Malta": 2,
        "Lebanon": 3,
        "Costa Rica": 4,
        "Mongolia": 5,
        "Dominican Republic": 6,
        "Kazakhstan": 7,
        "Georgia": 8,
        "Nigeria": 9
    }
    
    selected_country_name = st.sidebar.selectbox("Country", list(country_mapping.keys()))
    country_encoded = country_mapping[selected_country_name]

    # Pack all inputs into a DataFrame matching the training columns exactly
    features = pd.DataFrame({
        'count_view_item': [view_item],
        'count_add_to_cart': [add_to_cart],
        'count_begin_checkout': [begin_checkout],
        'device_category': [device_category],
        'traffic_medium': [traffic_medium],
        'country_encoded': [country_encoded]
    })
    return features

input_df = get_user_inputs()

# Main Dashboard Layout (Columns)
col1, col2 = st.columns([2, 1]) # Column 1 is twice as wide as Column 2

with col1:
    st.subheader("📊 Current Session Metrics")
    # Displaying metrics in sub-columns for a dashboard feel
    m1, m2, m3 = st.columns(3)
    m1.metric(label="👁️ Views", value=input_df['count_view_item'][0])
    m2.metric(label="🛒 Cart Additions", value=input_df['count_add_to_cart'][0])
    m3.metric(label="💳 Checkouts Begun", value=input_df['count_begin_checkout'][0])
    
    st.markdown("---")
    
    # 7. Prediction Trigger
    if st.button("🔮 Predict Conversion Likelihood"):
        with st.spinner("Analyzing behavior patterns..."):
            # Executing prediction
            prediction = pipeline.predict(input_df)
            prediction_proba = pipeline.predict_proba(input_df)
            
            # Extracting probability for class 1 (Buyer)
            buyer_probability = prediction_proba[0][1] * 100
            
            # Displaying aesthetic results based on the threshold
            if prediction[0] == 1:
                st.success(f"**High Conversion Probability!** The model predicts this user will buy.")
                st.balloons() # Fun animation for success
            else:
                st.warning(f"**Low Conversion Probability.** The model predicts this user will drop off.")
            
            # Displaying confidence gauge
            st.info(f"Model Confidence (Probability of buying): **{buyer_probability:.1f}%**")

with col2:
    # Optional: Displaying raw data or additional insights
    st.subheader("💡 Tips")
    st.info("Users who add items to the cart but don't begin checkout might be waiting for a discount code.")