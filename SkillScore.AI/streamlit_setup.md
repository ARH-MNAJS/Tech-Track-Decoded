# 🛠️ Streamlit Setup Guide (Windows, macOS, Linux)

This guide walks you through setting up **Streamlit** on your computer from scratch — for **Windows**, **macOS**, and **Linux** users. No prior environment setup is assumed.

---

## 📋 Prerequisites

Before installing Streamlit, you need:

- **Python 3.8 or higher**
- **pip** (comes with Python)
- **Virtual environment** (optional but highly recommended)
- **Internet connection**

We will install Streamlit in an isolated virtual environment to keep your system clean.

---

## 🪟 Windows Setup

### 1. ✅ Install Python

1. Go to: https://www.python.org/downloads/windows/
2. Click **"Download Python 3.x.x"** for Windows.
3. Run the installer:
   - **Check the box**: `Add Python to PATH`
   - Click **Install Now**

### 2. ✅ Verify Python and pip

Open Command Prompt (press `Win + R`, type `cmd`, hit Enter) and run:

```bash
python --version
pip --version
```

You should see something like:

```
Python 3.11.x
pip 23.x.x
```

### 3. ✅ Create a Virtual Environment (Recommended)

Navigate to your project folder:

```bash
cd path\to\your\project
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

You’ll see `(venv)` in your terminal prompt.

### 4. ✅ Install Streamlit

Now install Streamlit using pip:

```bash
pip install streamlit
```

### 5. ✅ Run a Test App

Create a file called `app.py` with the following content:

```python
import streamlit as st
st.title("Hello Streamlit!")
```

Run it:

```bash
streamlit run app.py
```

Your browser should open the app automatically.

---

## 🍎 macOS Setup

### 1. ✅ Install Homebrew (if not installed)

Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. ✅ Install Python 3

```bash
brew install python
```

Check version:

```bash
python3 --version
```

### 3. ✅ Create a Virtual Environment

Navigate to your project folder:

```bash
cd path/to/your/project
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 4. ✅ Install Streamlit

```bash
pip install streamlit
```

### 5. ✅ Run Streamlit App

Create `app.py` and run:

```bash
streamlit run app.py
```

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

Verify:

```bash
python3 --version
pip3 --version
```

### 3. ✅ Create and Activate Virtual Environment

```bash
cd /path/to/your/project
python3 -m venv venv
source venv/bin/activate
```

### 4. ✅ Install Streamlit

```bash
pip install streamlit
```

### 5. ✅ Run Test App

Create `app.py` and run:

```bash
streamlit run app.py
```

---

## 🧠 Troubleshooting

- If `streamlit` command is not found, ensure your virtual environment is activated.
- If the browser doesn’t open automatically, check your terminal for a local URL and open it manually.

---

## ✅ Summary

- Always use a virtual environment for Streamlit projects.
- Use `streamlit run app.py` to launch your app.
- Edit the `app.py` file and refresh the browser to see changes.

You’re all set! 🎉 Happy building with **Streamlit**.
