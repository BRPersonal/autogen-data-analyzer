import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime


def log(message: str) -> None:
    """Display log entry with current date followed by the message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] — {message}")

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="What is Streamlit?",
    page_icon="🚀",
    layout="centered"
)

# ----------------------------
# Title & intro
# ----------------------------
st.title("🚀 What is Streamlit?")
st.subheader("Build data apps in pure Python — no frontend skills needed")

st.markdown("""
**Streamlit** is an open-source Python framework that lets you build  
**interactive web applications** for data science and ML **very quickly**.

👉 If you know Python, you already know Streamlit.
""")

st.divider()

# ----------------------------
# Key features
# ----------------------------
st.header("✨ Why Streamlit?")

st.markdown("""
- 🐍 **Pure Python** – no HTML, CSS, or JavaScript  
- ⚡ **Instant UI** – widgets auto-generate  
- 🔄 **Reactive** – app reruns automatically on input change  
- 📊 **Great for data & ML** – charts, tables, models  
- 🚀 **Fast to deploy**
""")

# ----------------------------
# Example: basic widget
# ----------------------------
st.header("🧩 Example 1: Widgets")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello {name}! 👋")

age = st.slider("Select your age", 1, 100, 25)
st.write(f"Your age is **{age}**")

# ----------------------------
# Example: data display
# ----------------------------
st.header("📊 Example 2: Data Display")

data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.write("Here is a sample DataFrame:")
st.dataframe(data)

st.write("Line chart generated automatically:")
st.line_chart(data)

# ----------------------------
# Example: conditional logic
# ----------------------------
st.header("🧠 Example 3: Conditional Logic")

show_details = st.checkbox("Show explanation")
if show_details:
    st.info("""
    Streamlit apps rerun **top to bottom**  
    every time a widget value changes.
    """)

# ----------------------------
# Example: progress bar
# ----------------------------
st.header("⏳ Example 4: Progress & Status")

if st.button("Run a fake task"):
    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
        status.text(f"Processing... {i + 1}%")

    st.success("Task completed!")

# ----------------------------
# How it works internally
# ----------------------------
st.header("⚙️ How Streamlit Works")

st.markdown("""
1. You write a **single Python file**
2. Streamlit **executes it top to bottom**
3. UI is built from Python function calls
4. User interaction triggers a **rerun**
""")

# ----------------------------
# Use cases
# ----------------------------
st.header("🎯 Common Use Cases")

st.markdown("""
- Data exploration dashboards  
- ML model demos  
- Internal tools  
- POCs & hackathons  
- Teaching & tutorials
""")

# ----------------------------
# Footer
# ----------------------------
st.divider()
st.caption("Built with ❤️ using Streamlit")

log("Page rendering completed")
