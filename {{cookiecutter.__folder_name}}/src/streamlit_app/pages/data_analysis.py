import streamlit as st
import pandas as pd
from src.streamlit_app.util.data_loader import load_data
from src.streamlit_app.util.data_processor import process_data


def app():
    st.title("Data Analysis")
    data = load_data()
    processed_data = process_data(data)
    st.dataframe(processed_data)
