import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pyttsx3


load_dotenv(dotenv_path=r"api.env")  #add your own file path 

# loading model
llm = ChatGroq(groq_api_key=os.getenv("groq_api_key"),
               model_name="llama-3.1-8b-instant")

prompt = PromptTemplate.from_template(
    "Answer the given question:{input} politely and short.")

output = StrOutputParser()

# creating chain
chain = prompt | llm | output


def speech(response):
    "function to handle speech"
    try:
        engine = pyttsx3.init(driverName='sapi5')
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.say(response)
        engine.runAndWait()
        engine.stop()
        
    except Exception as e :
        print(f"speech error : {e}")


while True:

    text = input("Ask anything:")
    response = chain.invoke({"input": text})
    print(response)
    speech(response)

    if text.lower() == 'bye':
        break

