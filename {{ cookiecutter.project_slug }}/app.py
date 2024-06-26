import streamlit as st
from src.streamlit_app.pages import home, data_analysis, visualization

PAGES = {"Home": home, "Data Analysis": data_analysis, "Visualization": visualization}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()


if __name__ == "__main__":
    main()
