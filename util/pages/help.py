import streamlit as st

def help():
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
  
  st.write("# How to obtain your OpenAI API Key!!!")
  st.write("""***""")
  
  st.write("## (I) Creating your OpenAI Account")
  
  st.write(" 1) Visit the [OpenAI website](https://openai.com/)")
  st.write(" 2) Click on the 'Sign Up' or 'Get Starte' button to create an account.")
  st.write(" 3) Follow the instructions to create your account by providing the required information.")
  
  st.write("""***""")
  
  st.write("## (II) Navigating to your OpenAI API")
  
  st.write(" 1) Once you have successfully created your account, search for 'OpenAI API Key' on google and click on first link or click [here](https://platform.openai.com/account/api-keys).")
  st.write(" 2) Login with your details.")
  st.write(" 3) On the main landing page under the heading 'API keys' you will find a button saying 'Create new secret key'. Click on it")
  st.write(" 4) You will be asked to enter a name. Give any name according to your own interest.")
  st.write(" 5) Once you have given the name then click on 'Create secret key'.")
  st.write(" 6) Once you click on 'Create secret key' you will get a new pop-up with your secret key. Your secret key will start with something like - 'sk-<alpha_numeric characters>'.")
  st.write(" 7) Congratulations!!! You have successfully created your OpenAI API Key. Copy this key and paste it when 'ARIAS' ask you to enter your API.")
  
  st.info("Review the pricing and usage details to understand the costs associated with using the API. Make sure to securely store your API key."
          "Treat it like a password and avoid sharing it with unauthorized individuals.", icon="i")
  st.info("OpenAI allows you to have a free $5.00 usage when you sign up for the first time. But this $5.00 free usage has a validity of I guess 1 month. "
          "So make good use of your API as the prompts used in 'ARIAS' to generate 'Summary' or to generate the 'Answers' will cost around $0.02/prompt", icon="i")

  
           
  
  
  
