import streamlit as st
from pdf_utils import extract_text_from_pdf
from utils.visuals import generate_visuals
from pdf_utils import extract_text_from_pdf


st.set_page_config(page_title="Quarterly Report Visualizer", layout="wide")
st.title("📊 MarketSpectra AI: Quarterly Report Visualizer")

uploaded_file = st.file_uploader("Upload Quarterly Report (PDF)", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)
    
    if text:
        with st.spinner("Generating visuals..."):
            generate_visuals(text)
    else:
        st.error("No text could be extracted. Please try another PDF.")