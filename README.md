# 📊 MarketSpectra AI
MarketSpectra AI is a lightweight, Gemini-powered financial analysis tool that extracts and visualizes key data from company financial reports (PDFs). If specific values are missing, it uses AI inference to estimate them intelligently.


## 🚀 Features
- 📄 Upload **any financial PDF**
- 🔍 Extract metrics like:
  - Revenue, Profit, EPS, Cash Flow
  - Balance Sheet highlights
- 🤖 Gemini 1.5 Flash API:
  - Fills in missing fields with contextual estimation
- 📈 Interactive trend graphs (via Matplotlib/Plotly)

## 🛠️ Tech Stack
- **Streamlit** – Web Interface
- **PyMuPDF (fitz)** – PDF Parsing
- **Google Gemini 1.5 Flash API** – Data Inference
- **Matplotlib / Plotly** – Graphs
- **dotenv** – Local API Key Security

## 📌 Limitations
- Gemini API quotas apply (especially for free tier users)
- Outputs are based on uploaded financial reports. Gemini is only used to estimate values that are missing or not explicitly stated in the document.
- For educational/demonstration use only

## 🔮 Future Improvements
- Conversational AI – Let users ask questions about the uploaded report and visuals (e.g., "How did cash flow change from last quarter?")
- Support for more complex PDF layouts (e.g., multi-column tables, rotated text)
- Advanced visual analytics (e.g., YoY growth, ratio analysis, industry comparisons)
- Contextual risk assessment using NLP on Management Discussion sections
- Export to CSV/Excel for further analysis
- Password-protected upload or user-based session tracking
- Batch upload for multiple reports (quarterly trend comparison)
  
## 📬 Contact
Made by @vaetheneeb. Feel free to fork, explore, and suggest improvements!
