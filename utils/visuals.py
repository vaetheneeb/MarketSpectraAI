import streamlit as st
import matplotlib.pyplot as plt
from pdf_utils import extract_financial_data
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def safe_val(v):
    return v if isinstance(v, (int, float)) and v is not None else 0

def generate_visuals(text):
    data = extract_financial_data(text) or {}

    st.subheader("📈 Income Statement")
    st.markdown("Revenue, Gross Profit, Net Profit overview")
    draw_bar_chart(
        ["Revenue", "Gross Profit", "Net Profit"],
        [
            safe_val(data.get("Revenue")),
            safe_val(data.get("Gross Profit")),
            safe_val(data.get("Net Profit")),
        ]
    )

    # ❌ EPS Trend visual removed

    st.subheader("📊 Balance Sheet")
    draw_pie_chart(
        ["Assets", "Liabilities", "Equity"],
        [
            safe_val(data.get("Assets")),
            safe_val(data.get("Liabilities")),
            safe_val(data.get("Equity")),
        ]
    )
    st.markdown("Debt-to-Equity Ratio")
    draw_gauge("Debt-to-Equity Ratio", safe_val(data.get("Debt-to-Equity Ratio")))

    st.subheader("💰 Cash Flow")
    draw_bar_chart(
        ["Operating", "Investing", "Financing"],
        [
            safe_val(data.get("Operating")),
            safe_val(data.get("Investing")),
            safe_val(data.get("Financing")),
        ]
    )

    # ❌ Free Cash Flow Trend visual removed

    st.subheader("📝 Management Notes")
    st.info(data.get("Management Notes") or "No notes provided.")

    st.subheader("📌 Guidance")
    st.markdown(data.get("Guidance") or "No guidance data available.")

    st.subheader("🧠 YoY / QoQ Compare")
    st.markdown(data.get("YoY QoQ Compare") or "No year-over-year or quarter-over-quarter comparison.", unsafe_allow_html=True)


# --- Visual Helpers ---
def draw_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values, color='skyblue')
    st.pyplot(fig)

def draw_line_chart(values, labels, title="Trend"):
    fig, ax = plt.subplots()
    ax.plot(labels, values, marker='o')
    ax.set_title(title)
    st.pyplot(fig)

def draw_pie_chart(labels, sizes):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

def draw_gauge(title, value):
    st.metric(label=title, value=f"{value:.2f}")