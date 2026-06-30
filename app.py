import streamlit as st
from services.gemini_service import analyze_call
from prompts.sales_prompt import SALES_ANALYSIS_PROMPT

import json

from utils.parser import parse_json

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
        with st.spinner("🧠 AI is analyzing the sales conversation..."):

            result = analyze_call(
                SALES_ANALYSIS_PROMPT + transcript
            )

        try:
            analysis = parse_json(result)

            st.success("Analysis Completed!")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Lead Score",
                    f'{analysis["lead_score"]}/100'
                )

            with col2:
                st.metric(
                    "Interest",
                    f'{analysis["interest_level"]}/10'
                )

            with col3:
                st.metric(
                    "Sentiment",
                    analysis["sentiment"]
                )

            with col4:
                st.metric(
                    "Intent",
                    analysis["buying_intent"]
                )    


            st.subheader("📝 Conversation Summary")

            st.info(
                analysis["summary"]
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Customer Persona",
                    analysis["customer_persona"]
                )

            with col2:
                st.metric(
                    "Urgency",
                    analysis["urgency"]
                )

            st.subheader("🚩 Customer Objections")

            for objection in analysis["objections"]:
                st.warning(objection)

            st.subheader("📞 Recommended Follow-up")

            st.success(
                analysis["follow_up"]
            )

            st.subheader("➡ Next Best Action")

            st.info(
                analysis["next_best_action"]
            )

            

        except Exception as e:

            st.error("Unable to parse AI response.")

            st.code(result)

                