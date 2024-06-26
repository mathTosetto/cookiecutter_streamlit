import streamlit as st
from ..utils.data_loader import load_data
from ..utils.data_processor import process_data


def app():
    st.title("Data Analysis")
    data = load_data()
    processed_data = process_data(data)
    st.dataframe(processed_data)
