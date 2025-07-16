from flask import Flask, render_template, request
import fitz  # PyMuPDF
from utils import analyze_with_llm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf = request.files['pdf']
        if pdf:
            text = extract_text_from_pdf(pdf)
            feedback = analyze_with_llm(text)
            return render_template('result.html', feedback=feedback)

    return render_template('index.html')


def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


if __name__ == '__main__':
    app.run(debug=True)
