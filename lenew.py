import streamlit as st
import random
import time

#from google.colab import userdata
#open_ai_key = userdata.get('open_ai_key')
from openai import OpenAI
client = OpenAI(api_key=st.secrets["open_ai_key"])
#client = OpenAI(api_key=open_ai_key)

import os

#os.environ["OPENAI_API_KEY"] = open_ai_key
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import chromedriver_autoinstaller
from llama_index.core import VectorStoreIndex, download_loader
from llama_index.readers.web import WholeSiteReader

service = Service(ChromeDriverManager().install())


# Streamed response emulator
def response_generator(query):
  # Initialize ChromeDriver and ensure compatibility
  #chromedriver_autoinstaller.install()  # Automatically install the compatible chromedr
  #configure chrome options
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  #driver = webdriver.Chrome(options=options) #initialize ChromeDriver
  driver = webdriver.Chrome(service=service, options=options)
  
  # Initialize the scraper with a prefix URL and maximum depth
  try:
     scraper = WholeSiteReader(
      prefix="https://www.fire.ca.gov/",  # Example prefix
      max_depth=6,
      driver=driver # Pass the configured driver to the WholeSiteReader
     )
      # Start scraping from a base URL
     documents = scraper.load_data(
        base_url="https://www.fire.ca.gov/"
     )  # Example base URL
     index = VectorStoreIndex.from_documents(documents)
     query_engine = index.as_query_engine()
     response = query_engine.query(query)
  except Exception as e:
        # Log or handle the exception
        response = f"An error occurred: {e}"
  
  finally:
     driver.quit()
  return response

st.title("FireBot chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
         st.markdown(prompt)
    # Generate and display assistant response
    response = response_generator(prompt)
  
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        #response = st.write_stream(response_generator(message["content"]))
         st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
