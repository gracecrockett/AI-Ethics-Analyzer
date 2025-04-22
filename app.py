import streamlit as st
from gpt_ethics import run_gpt_analysis

st.set_page_config(page_title="AI Ethics Analyzer (GPT-4)", layout="centered")
st.title("🧠 AI Ethics Analyzer with GPT-4")
st.write("Enter an AI use case and receive a quick ethical evaluation.")

use_case = st.text_area("Describe your AI use case:")

if st.button("Analyze"):
    if use_case.strip():
        with st.spinner("Analyzing with GPT-4..."):
            result = run_gpt_analysis(use_case)
            st.subheader("GPT-4 Ethics Evaluation")
            st.markdown(result)
    else:
        st.warning("Please enter a use case.")
