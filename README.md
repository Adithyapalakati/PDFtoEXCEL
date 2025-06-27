# 📄 PDF to Excel Converter (Flask)

Convert tabular PDF files into editable Excel spreadsheets using a simple and clean Flask interface.

🔗 **Live Demo:** [https://pdftoexcel-gaev.onrender.com/](https://pdftoexcel-gaev.onrender.com/)

---

## ✨ Features

- 📥 Upload PDF files with tables
- 🔍 Extracts tabular data using `pdfplumber`
- 📊 Converts and downloads as `.xlsx` (Excel)
- 🧼 Clean Bootstrap UI
- 💡 Works entirely on the backend — no third-party APIs needed

---

## 🚀 Tech Stack

- **Backend**: Flask (Python)
- **PDF Parsing**: pdfplumber
- **Excel Export**: pandas
- **Frontend**: HTML + Bootstrap
- **Hosting**: Render

---

## 📁 Project Structure

📦 pdf-to-excel
├── app.py # Flask app entry point
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Upload and result UI
├── static/ # (optional) for custom CSS/JS
└── uploads/ # Temporary PDF storage (ignored in deployment)

