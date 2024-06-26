import streamlit as st
import plotly.express as px
from ..utils.data_loader import load_data


def app():
    st.title("Data Visualization")
    data = load_data()
    fig = px.scatter(data, x="feature1", y="feature2", color="category")
    st.plotly_chart(fig)
