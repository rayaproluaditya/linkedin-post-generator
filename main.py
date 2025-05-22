import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Custom CSS for improved UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0072b1 0%, #ffffff 100%);
        background-attachment: fixed;
        background-size: cover;
        font-family: 'Segoe UI', sans-serif;
        color: #0072b1;
    }

    .title {
        text-align: center;
        font-size: 2.8em;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 1.5rem;
        margin-top: 1rem;
        text-shadow: 1px 1px 3px #0072b1;
    }

    .glass-box {
        background: #ffffff;
        border-radius: 20px;
        padding: 25px 20px;
        box-shadow: 0 8px 32px 0 rgba(23, 38, 135, 0.2);
        border: 1px solid rgba(0, 114, 177, 0.2);
        color: #0072b1;
        margin-top: 1rem;
        font-size: 1.1em;
        line-height: 1.6;
        white-space: pre-wrap;
    }

    div.stButton > button {
        background-color: #ffffff !important;
        color: #0072b1 !important;
        border: none;
        font-size: 1rem;
        padding: 0.6em 2em;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0, 114, 177, 0.2);
        transition: 0.3s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #0072b1 !important;
        color: #ffffff !important;
        transform: scale(1.05);
    }

    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: #ffffff !important;
        color: #0072b1 !important;
        border: 1px solid rgba(0, 114, 177, 0.4) !important;
        border-radius: 10px;
    }

    .stSelectbox svg {
        color: #0072b1 !important;
    }

    .stSelectbox ul {
        background-color: #e6f2fa !important;
        color: #0072b1 !important;
    }

    .stSelectbox ul li:hover {
        background-color: #cce5f6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.markdown('<div class="title">🚀 LinkedIn Post Generator: <span style="color:#ffee58;">Postify</span></div>', unsafe_allow_html=True)

    fs = FewShotPosts()
    tags = fs.get_tags()

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_tag = st.selectbox("✨ Choose Topic", options=tags)
    with col2:
        selected_length = st.selectbox("📏 Length", options=length_options)
    with col3:
        selected_language = st.selectbox("🗣️ Language", options=language_options)

    st.markdown("<br>", unsafe_allow_html=True)

    post = ""
    if st.button("✨ Generate Post"):
        with st.spinner("🛠️ Crafting a powerful LinkedIn post for you..."):
            post = generate_post(selected_length, selected_language, selected_tag)

    # Output in white box with blue text inside
    if post:
        st.markdown(f'<div class="glass-box">{post}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="glass-box" style="text-align:center; color:#999;">Your generated post will appear here ✨</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
