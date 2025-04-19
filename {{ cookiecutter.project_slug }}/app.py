import logging

import streamlit as st

from dotenv import load_dotenv

from src.utils.my_logger import LoggerSetup
from src.streamlit_app.pages import home, data_analysis, visualization

# Initialize logger setup
LoggerSetup()

# Load environment variables
load_dotenv()

LOGGER: logging.Logger = logging.getLogger("main")

PAGES = {"Home": home, "Data Analysis": data_analysis, "Visualization": visualization}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()


if __name__ == "__main__":
    main()
