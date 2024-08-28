FIRE BOT Chatbot 

## Overview of the App

This app showcases how we train a model using RAG with california fires (including recent active fires).

- Chatbot 
- Chat with Internet search
- Chat with user feedback



### Get an OpenAI API key
curretly using my Own API key which stored in secrets of streamLit APP, will change after project validation, to accept key while entering 

below are instructions for creating ne
You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.


### Enter the OpenAI API key in Streamlit Community Cloud

To set the OpenAI API key as an environment variable in Streamlit apps, do the following:

1. At the lower right corner, click on `< Manage app` then click on the vertical "..." followed by clicking on `Settings`.
2. This brings the **App settings**, next click on the `Secrets` tab and paste the API key into the text box as follows:

```sh
OPENAI_API_KEY='xxxxxxxxxx'
