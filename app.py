from flask import Flask, request, render_template, send_file
import pdfplumber
import pandas as pd
from io import BytesIO
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    if 'pdf_file' not in request.files or request.files['pdf_file'].filename == '':
        return 'No file selected', 400

    pdf_file = request.files['pdf_file']
    tables = []

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                raw_columns = table[0]
                # Ensure unique column names
                unique_columns = []
                seen = {}

                for col in raw_columns:
                    if col not in seen:
                        seen[col] = 1
                        unique_columns.append(col)
                    else:
                        seen[col] += 1
                        unique_columns.append(f"{col}_{seen[col]}")

                df = pd.DataFrame(table[1:], columns=unique_columns)
                tables.append(df)

    if not tables:
        return 'No tables found in PDF', 400

    return render_template('preview.html', tables=tables)

@app.route('/export', methods=['POST'])
def export():
    table_data_json = request.form.get('table_data')

    if not table_data_json:
        return 'No table data received', 400

    try:
        table_data = json.loads(table_data_json)
    except json.JSONDecodeError:
        return 'Invalid table data format', 400

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for i, table in enumerate(table_data):
            df = pd.DataFrame(table['rows'], columns=table['columns'])
            df.to_excel(writer, sheet_name=f'Page_{i+1}', index=False)

    output.seek(0)
    return send_file(output, download_name='edited_output.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
