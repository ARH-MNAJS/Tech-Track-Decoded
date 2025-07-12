# 📦 `pdfkit`

## ✅ What is pdfkit?

**pdfkit** is a Python wrapper around the command-line tool **wkhtmltopdf**, which converts HTML content into **PDF files**. This means you can take any webpage, HTML string, or rendered template and turn it into a downloadable, printable PDF using Python.

It is especially useful when you need to generate reports, invoices, or any printable content dynamically from a web interface or a script.

---

## ✨ Key Features

- Converts HTML strings, local HTML files, or URLs to PDFs
- Maintains CSS styling, fonts, and layout from HTML
- Allows setting page size, orientation, margins, and headers/footers
- Can be used in both server-side and desktop applications
- Supports PDF generation from dynamic HTML templates (like Jinja2)

---

## 📘 Example: pdfkit in Action

Here’s how you could use pdfkit to convert HTML into a PDF file:

1. Import the library: `import pdfkit`
2. Define your HTML content:  
   `html = "<h1>Student Report</h1><p>Name: Aditi<br>Score: 92</p>"`
3. Convert and save as PDF: `pdfkit.from_string(html, "report.pdf")`

This will generate a file named `report.pdf` with the given HTML content properly rendered as a styled PDF document.

You can also convert a local HTML file like this:  
`pdfkit.from_file("page.html", "output.pdf")`

Or even convert a full webpage using its URL:  
`pdfkit.from_url("https://example.com", "page.pdf")`

---

## 🚀 How to Use This in Practice

To use pdfkit, follow these steps:

1. Install pdfkit using `pip install pdfkit`
2. Install the **wkhtmltopdf** tool separately (required backend)
3. Import the module in your script: `import pdfkit`
4. Use one of its methods:
   - `from_string()` to convert raw HTML
   - `from_file()` to convert local HTML files
   - `from_url()` to convert live web pages
5. Save the result to a `.pdf` file

To ensure wkhtmltopdf works, you may need to configure the path using:  
`pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')`

---

## 📊 What Kind of Results Can It Produce?

Using pdfkit, you can produce:

- Beautifully styled reports with headers, tables, and logos
- PDF invoices from dynamic HTML templates
- Downloadable versions of webpages
- Certificates, resumes, or formatted forms

For instance, if you're building a student dashboard with report cards, pdfkit lets you export the HTML report directly into a polished, printable PDF file with minimal effort.

---

## 🧠 Summary

pdfkit is a simple yet powerful way to turn HTML into print-ready PDF documents using Python. It bridges the gap between web content and downloadable documents, making it ideal for automating report generation, form exports, and professional document output in any project.
