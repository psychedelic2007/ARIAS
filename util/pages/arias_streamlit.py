import streamlit as st
import openai
import PyPDF2
import tempfile


def arias_sum():
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

    TEMPERATURE_RANGE = (0.0, 1.0)
    DEFAULT_TEMPERATURE = 0.5

    MAX_TOKEN_RANGE = (100, 1000)
    DEFAULT_MAX_TOKENS = 500

    st.write("# Article Research Intelligence and Summarization")

    st.subheader("Please upload your Research Paper")
    uploaded_file = st.file_uploader("Upload", type=["pdf"])
    uploaded_api = st.text_input("Please give your OpenAI API Key")

    temperature = st.slider(
        "Temperature",
        min_value=TEMPERATURE_RANGE[0],
        max_value=TEMPERATURE_RANGE[1],
        value=DEFAULT_TEMPERATURE,
        step=0.1,
        help="Higher values (e.g. 0.8) make the output more random, while lower values (e.g. 0.2) make it more deterministic",
    )
    with st.expander("ℹ️ Temperature Info"):
        st.info("Temperature controls the randomness of the generated text. Higher values make it more random."
                "For example value of 0.8 makes the output more random, while value of 0.2 make it more deterministic")

    max_tokens = st.slider(
        "Max Tokens",
        min_value = MAX_TOKEN_RANGE[0],
        max_value = MAX_TOKEN_RANGE[1],
        value = DEFAULT_MAX_TOKENS,
        step = 100,
        help="Controls the maximum number of tokens (words) in the generated summary. A higher value will result in a longer summary.",
    )
    with st.expander("ℹ️ Max Tokens Info"):
        st.info("Max Tokens controls the length of the generated summary. A higher value produces a longer summary."
                "But it is advised not to go too high as it will cause the language model to throw an InvalidRequestError "
                "suggesting you to reduce the token size.")
    show_submit = st.button("Generate Summary")

    #initialise the current index
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    st.write("""***""")

    if show_submit:
        with st.spinner("ARIAS is compiling your Summary....."):
            openai.api_key = uploaded_api
            p1 = """
                We need you to perform the following modifications to this document, outputting the modified document in full afterwards:

                * Remove anything from the text above which doesn't look like natural language, smooth it out.
                * Words which are wrapped on the next line and hyphenated i.e. morpho-
                phonology should become "morphophonology"
                * All references to figures or tables should be removed
                * All parenthesized text should be removed, e.g. "(Solar-Lezama et al., 2016)"
                * Cover the entire input document above then terminate
                * remove all unnecessary whitespace and carriage returns
                * Only write responses in natural explanatory language, remove all mathematics, notations, symbols etc
                * Remove any empty lines, or lines which only have a few words or symbols on them
                """

            p2 = """
                You are an expert scientific writer/editor who is proficient in understanding science and summarizing it.
                Provide an expert summary of the document in natural language, explaining the main points and summarizing the main ideas. 
                Don't copy the lines from the document. Write the summary in your own words.
                Provide the summary as if you are teaching a 16 year old.
                You should write your summary in natural language, not in the form of a list of bullet points.
                """

            def extract_text_from_pdf(file_path):
                with open(file_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    text = ''
                    for page in range(len(reader.pages)):
                        text += reader.pages[page].extract_text()
                    return text

            def split_into_sentences(text):
                sentences = text.split('. ')
                return sentences

            def summarize_document(sentences, max_tokens=4096):
                summary = ''
                current_tokens = 0
                for sentence in sentences:
                    if current_tokens + len(sentence) < max_tokens:
                        summary += sentence + '. '
                        current_tokens += len(sentence)
                    else:
                        break
                return summary

            if uploaded_file is not None:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_file_path = temp_file.name

                document_text = extract_text_from_pdf(temp_file_path)
                sentences = split_into_sentences(document_text)
                summary = ''

                while len(summary.split()) < 300:
                    new_summary = summarize_document(sentences)
                    summary += new_summary

                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=p1 + summary + p2,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                final_summary = response.choices[0].text.strip()

                st.write(final_summary)