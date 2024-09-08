import pandas as pd
import streamlit as st
from openai import OpenAI
import random

def chat_gpt(key, sys_prompt):
    client = OpenAI(
        api_key=key)
    initial_prompt = {
        'role': 'system',
        'content': sys_prompt
    }

    if not st.session_state.get('chat_messages'):
        st.session_state['chat_messages'] = [initial_prompt]
    else:
        st.session_state['chat_messages'][0] = initial_prompt

    prompt = st.chat_input('Ask your question', key = random.randint(0,10000000))
    if prompt:
        st.session_state['chat_messages'].append({
            'role': 'user',
            'content': prompt
        })

    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=st.session_state['chat_messages'],
    )
    st.session_state['chat_messages'].append({
        'role':
        'assistant',
        'content':
        completion.choices[0].message.content
    })

    chat_container = st.container(border=True, height=400)

    for message in st.session_state['chat_messages'][1:]:
        chat_message = chat_container.chat_message(message['role'])
        chat_message.write(message['content'])
def gpt_2(key):
    prompt = st.chat_input('Ask your question',key=123)
    client = OpenAI(
        api_key=key)
    initial_prompt = {
        'role': 'user',
        'content': prompt,
    }
    print(prompt)
cont = st.container()
st.text("Ask the AI anything. For example, you can ask it to generate a mnemonic.")
chat_gpt("Insert OpenAI Key Here", "You are an AI used in a password manager app. Please provide support and advice. The app has 4 menus on the sidebar, Home, Generate Password, Export Password, and AI. All of them do exactly what you would think they would. Provide support if the user has questions.")

    
    

