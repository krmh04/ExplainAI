import openai
import streamlit as st

def summarize(prompt):
   # augmented_prompt = f"summarize this text: {prompt}"
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful research assistant."},
        {"role": "user", "content": f"Summarize this: {prompt}"},
        ],
        )
        st.session_state["summary"] = response["choices"][0]["message"]["content"]
    except:
        st.write('There was an error =(')