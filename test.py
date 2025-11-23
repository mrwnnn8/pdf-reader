import pyttsx3
from pypdf import PdfReader

reader = PdfReader("Chapter 2 Numerical Sequences v2.pdf")
num = len(reader.pages)
engine = pyttsx3.init()

for i in range(num):
    page= reader.pages[i]
    text = page.extract_text()

    print(f"==================page{i+1}==================")
    print(text)  

    engine.say(text)
    
engine.runAndWait()


