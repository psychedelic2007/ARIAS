import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import streamlit as st
from streamlit.components.v1 import html
from multiapp import MultiApp
from util.pages.home_page import home_page
from util.pages.arias_streamlit import arias_sum
from util.pages.ask_pdf import arias_ask


app = MultiApp()

app.add_app("Home Page", home_page)
app.add_app("ARIAS Summarizer", arias_sum)
app.add_app("ARIAS Ask", arias_ask)

app.run()