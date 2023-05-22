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
    
    st.markdown("---")

    st.write("# About Me")

    col1, col2 = st.columns([1, 2])
    
    
    with col1:
        image = Image.open('my_avatar.png')
        avatar = image.resize((150, 150))
        
        st.markdown(
        """
        <style>
        .avatar {
            display: inline-block;
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%;
        }
        </style>
        """,
        unsafe_allow_html=True,)
        
        st.image(avatar, use_column_width=True, output_format='PNG')
    
    with col2:
        st.markdown("<h2 style='text-align: center; font-weight: bold;'>Your Name</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>"
                "<a href='https://github.com/psychedelic2007' target='_blank'><img src='github_icon.png' width='30'></a>"
                "<a href='https://scholar.google.com/citations?user=GgF3yTYAAAAJ&hl=en' target='_blank'><img src='google_scholar_icon.png' width='30'></a>"
                "<a href='https://www.researchgate.net/profile/Satyam-Sangeet' target='_blank'><img src='researchgate_icon.png' width='30'></a>"
                "<a href='mailto:satyamsangeet229@gmail.com'><img src='email_icon.png' width='30'></a>"
                "</p>",
                unsafe_allow_html=True)
