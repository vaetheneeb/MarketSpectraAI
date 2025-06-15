# --- pdf_utils.py ---

import fitz  # PyMuPDF
import re
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Use a valid free Gemini model (non-pro)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def extract_value(text, label, fallback=None):
    match = re.search(rf"{label}[:\s]+[\$RM]?([\d,\.]+)", text, re.IGNORECASE)
    if match:
        try:
            return float(match.group(1).replace(",", ""))
        except:
            return fallback
    return estimate_missing_value(text, label, fallback)

def estimate_missing_value(text, label, fallback):
    try:
        prompt = f"Estimate the company's {label} based on the following report:\n{text}\nGive only a number."
        response = model.generate_content(prompt)
        result = response.text.strip()
        return float(result.replace(',', '').replace('RM', '').strip())
    except Exception as e:
        print(f"[Gemini] Failed for {label}: {e}")
        return fallback

def extract_financial_data(text):
    return {
        "Revenue": extract_value(text, "Revenue"),
        "Gross Profit": extract_value(text, "Gross Profit"),
        "Net Profit": extract_value(text, "Net Profit"),

        "Assets": extract_value(text, "Total Assets"),
        "Liabilities": extract_value(text, "Total Liabilities"),
        "Equity": extract_value(text, "Equity"),
        "Debt-to-Equity Ratio": extract_value(text, "Debt-to-Equity Ratio"),

        "Operating": extract_value(text, "Operating Cash Flow"),
        "Investing": extract_value(text, "Investing Cash Flow"),
        "Financing": extract_value(text, "Financing Cash Flow"),

        "Management Notes": extract_management_notes(text),
        "Guidance": extract_guidance(text),
        "YoY QoQ Compare": extract_comparison_notes(text)
    }

def extract_management_notes(text):
    match = re.search(r"Management Notes\s*[:\-]?\s*(.+)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_guidance(text):
    match = re.search(r"Guidance\s*[:\-]?\s*(.+)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_comparison_notes(text):
    lines = []
    revenue_match = re.search(r"Revenue.*?(\+|\-)?(\d+)%", text, re.IGNORECASE)
    net_profit_match = re.search(r"Net Profit.*?(\+|\-)?(\d+)%", text, re.IGNORECASE)

    if revenue_match:
        trend = "▲" if revenue_match.group(1) != '-' else "▼"
        percent = revenue_match.group(2)
        lines.append(f"- Revenue {trend} {percent}% (🟢 good)" if trend == "▲" else f"- Revenue {trend} {percent}% (🔴 bad)")

    if net_profit_match:
        trend = "▲" if net_profit_match.group(1) != '-' else "▼"
        percent = net_profit_match.group(2)
        lines.append(f"- Net Profit {trend} {percent}% (🟢 good)" if trend == "▲" else f"- Net Profit {trend} {percent}% (🔴 bad)")

    return "<br>".join(lines) if lines else None