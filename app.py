import streamlit as st

st.set_page_config(
    page_title="AI Sales Call Analyzer",
    page_icon="📞",
    layout="wide"
)

st.title("📞 AI Sales Call Analyzer")

st.write("Analyze sales call transcripts using Gemini AI.")

uploaded_file = st.file_uploader(
    "Upload Call Transcript",
    type=["txt"]
)

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")

    st.subheader("Transcript")

    st.text_area(
        "",
        transcript,
        height=300
    )

    if st.button("Analyze Call"):
        st.success("Analysis coming soon...")