import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pyttsx3

load_dotenv(dotenv_path=r"api.env")

llm = ChatGroq(groq_api_key=os.getenv("groq_api_key"),
               model_name="llama-3.1-8b-instant")

prompt = PromptTemplate.from_template(
    "Answer the given question:{input} polietly and short.")

output = StrOutputParser()
chain = prompt | llm | output


if __name__ == "__main__":
    print("Welcome to ROBO Speaker!!!")
    
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)  #female voice 
    engine.setProperty('rate',150)  #speed of the voice 
     
     

    while True:
        text = input("Enter anything:")
        response = chain.invoke({"input":text})
        
        if text.lower() == "bye" :
            print(response)
            engine.say(response)
            break
        
        engine.say(response)
        print(response)
        engine.runAndWait()
        
        
        
        

        
