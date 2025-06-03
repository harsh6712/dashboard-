import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="CRRI PME Dashboard", layout="centered")

# Title
st.title("📊 CRRI PME Project Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload Project Excel File", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("✅ Excel file uploaded successfully.")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Failed to read Excel file: {e}")
else:
    st.info("ℹ️ Please upload an Excel file to get started.")