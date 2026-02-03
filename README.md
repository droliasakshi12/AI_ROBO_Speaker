# 🤖AI ROBO SPEAKER
A **ROBO SPEAKER** created using python programming where anything asked would be answered in speech.
Made the use of **Groq - llama Model** to reply the text inputted.

## 🧠Concept Covered 
- Loading Env file 
- Langchain library 
- llama - Groq Models
- reply the text in speech

<h2>🛒Requirement</h2>
<b>Python version</b>
<br>
-Python(3.11.5)<br>
<br>
---

<b>IDE/Code Editor</b>
<br>
-VS Code
</br>
<br>
<h2>📦Tech Stack</h2>
<b>- PYTHON</b>
<br>

**Run the below code in the terminal:**
- This will install all the required libraries.

``` bash
pip install -r requirements.txt
```
<br>

## 📚 Library Used

``` bash 
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pyttsx3
```

## ✏️About the Project 
- 📙This project includes the use of pyttsx3 library which is used for converting the **Text-To-Speech** .
- 🤖 We have made the use of langchain where **llama model** is integrated to reply the inputted text.
- 🔊The reply is in the format of text also in the format of speech
- 🗣️We can convert the voice from male to female using the below code.

**👩‍💻CODE**
``` bash
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)  #female voice 
engine.setProperty('rate',150)  #speed of the voice
```
<br>

<b><p>⭐ If you found this repository useful, consider giving it a star!</p>
<p>Happy Coding 🐍✨</p></b>

👤 Github  : [@droliasakshi12](https://github.com/droliasakshi12)<br>
📩 Email   : sakshidrolia12@gmail.com <br>
🔗 Linkdin : https://www.linkedin.com/in/sakshi-drolia12 <br>

<b><h5>Author</h5></b>
<b>Sakshi Drolia</b>

