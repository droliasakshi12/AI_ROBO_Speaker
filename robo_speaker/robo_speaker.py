import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage, AIMessage
import pyttsx3

load_dotenv(dotenv_path=r"C:\Users\data\OneDrive\Desktop\study\practical world projects\python_projects\robo_speaker\api.env")


@st.cache_resource
def get_model():
    return ChatGroq(groq_api_key=os.getenv("groq_api_key"), model_name="llama-3.1-8b-instant")


model = get_model()

st.set_page_config(page_title='AI CHATBOT', page_icon='🤖')

st.title("🤖 AI ROBO SPEAKER")
def speak(speak_text):
    try:
        engine = pyttsx3.init(driverName='sapi5')
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.say(speak_text)
        engine.runAndWait()
        engine.stop()
        
    except Exception as e :
        st.error(f"Error :  {e}")
    
    

if 'messages' not in st.session_state:
    st.session_state.messages=[
        SystemMessage(content = "you are an educated human.")
    ]

for message in st.session_state.messages[1:]:
    role = "user" if isinstance(message , HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)
        
     
#chat input 
if prompt := st.chat_input("ask anything"):
    
    with st.chat_message('user'):
        st.markdown(prompt)

    #appending the user input 
    st.session_state.messages.append(HumanMessage(content = prompt))
    
    with st.chat_message("assistant"):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)
            speak(response.content) 
    
    st.session_state.messages.append(AIMessage(content = response.content))


#sidebar 

with st.sidebar:
    if st.button("🗑️Clear chat hsitory"):
        st.session_state.messages=[
        SystemMessage(content = "you are an educated human.")]
        st.rerun()
    
    st.markdown('---')
    
