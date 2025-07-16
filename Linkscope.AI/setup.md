# 🛠️ Flask Setup Guide (Windows, macOS, Linux)

This guide walks you through setting up **Flask**, a lightweight web framework for Python. The instructions are designed for complete setup on **Windows**, **macOS**, and **Linux**, using virtual environments to keep everything clean and organized.

---

## 📋 Prerequisites

Before installing Flask, ensure your system has:

- **Python 3.8 or higher**
- **pip** (Python package manager, comes with Python)
- **Internet connection**

We’ll use **virtual environments** to keep your Flask projects isolated from system-wide packages.

---

## 🪟 Windows Setup

### 1. ✅ Install Python

1. Download from: https://www.python.org/downloads/windows/
2. Run the installer:
   - **Check** `Add Python to PATH`
   - Click **Install Now**

### 2. ✅ Verify Python and pip

Open Command Prompt (`Win + R`, type `cmd`, press Enter):

```bash
python --version
pip --version
```

You should see something like:

```
Python 3.11.x
pip 23.x.x
```

### 3. ✅ Create a Virtual Environment

Navigate to your project directory:

```bash
cd path\to\your\project
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. ✅ Install Flask

With the virtual environment activated:

```bash
pip install flask
```

### 5. ✅ Create a Flask App

Create a file named `app.py` and add this:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
```

### 6. ✅ Run the Flask App

In the same terminal, run:

```bash
set FLASK_APP=app.py
flask run
```

Open your browser and go to `http://127.0.0.1:5000/`

---

## 🍎 macOS Setup

### 1. ✅ Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. ✅ Install Python 3

```bash
brew install python
```

Verify installation:

```bash
python3 --version
```

### 3. ✅ Create a Virtual Environment

```bash
cd path/to/your/project
python3 -m venv venv
source venv/bin/activate
```

### 4. ✅ Install Flask

```bash
pip install flask
```

### 5. ✅ Create and Run Flask App

Create `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
```

Run it:

```bash
export FLASK_APP=app.py
flask run
```

Visit: `http://127.0.0.1:5000/`

---

## 🐧 Linux Setup (Ubuntu/Debian)

### 1. ✅ Update System

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. ✅ Install Python 3 and pip

```bash
sudo apt install python3 python3-pip python3-venv -y
```

### 3. ✅ Create and Activate Virtual Environment

```bash
cd /path/to/your/project
python3 -m venv venv
source venv/bin/activate
```

### 4. ✅ Install Flask

```bash
pip install flask
```

### 5. ✅ Create and Run Flask App

Create `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
```

Run it:

```bash
export FLASK_APP=app.py
flask run
```

Go to `http://127.0.0.1:5000/` in your browser.

---

## 🧠 Troubleshooting

- If `flask` is not recognized, make sure your virtual environment is activated.
- If browser doesn't open automatically, manually go to `http://127.0.0.1:5000/`

---

## ✅ Summary

- Always activate your virtual environment before working on a Flask project.
- Use `flask run` to start the development server.
- Use `@app.route()` to define routes in your app.

Now you’re ready to start building with **Flask**! 🚀
