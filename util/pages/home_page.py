import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

def home_page():

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"]{
            background-color: #b388eb;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    image = Image.open('arias-logo.png')
    st.image(image)

    st.markdown('<h1 style="text-align: center; color: #888888;">'
                '<span style="color: black; font-weight: bold;">A</span>rticle '
                '<span style="color: black; font-weight: bold;">R</span>esearch '
                '<span style="color: black; font-weight: bold;">I</span>ntelligence '
                '<span style="color: black; font-weight: bold;">A</span>nd '
                '<span style="color: black; font-weight: bold;">S</span>ummarization'
                '</h1>',
                unsafe_allow_html=True)

    st.write("""***""")

    st.write("# Overview")

    st.markdown("Having witnessed the remarkable impact of ChatGPT, I embarked on a mission to harness its power for "
    "the realm of research. And thus, ARIAS was born—a brainchild of mine that combines the prowess of ChatGPT with the "
    "world of scholarly articles. ARIAS, short for Article Research Intelligence and Summarization, is a cutting-edge model "
    "that revolutionizes how we interact with research. It empowers users to effortlessly navigate through complex articles "
    "by providing comprehensive summaries and engaging in interactive conversations. With ARIAS, knowledge becomes accessible, "
    "engaging, and dare I say, fun!")

    st.markdown("Join me on this exciting journey as we uncover the true potential of ARIAS and unlock a world of research at our "
    "fingertips. Let's embark on an intellectual adventure like no other and redefine the way we consume and understand "
    "scholarly knowledge. Together, we can conquer the challenges of research and embrace the wonders of ARIAS!")