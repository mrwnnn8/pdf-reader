import pyttsx3
from pypdf import PdfReader
import tkinter as tk
from tkinter import messagebox

reader = PdfReader("Chapter 2 Numerical Sequences v2.pdf") #just a pdf from uni for trying
num = len(reader.pages)
engine = pyttsx3.init()

root = tk.Tk()
root.title ("pdf reader")
root.geometry = ("400x200")

Label = tk.Label(root, text = "to read either all the pages or a chosen one enter 'all' or a page number")
p= input('enter the number of the page u wanna be read (if u want all just type "all")').strip().lower() 
Label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)
if p == "all":
        for i in range(num):
            page= reader.pages[i]
            text = page.extract_text()

            print(f"==================page{i+1}==================")
            print(text)  

            engine.say(text)
    
else: 
    try:
        p = int(p) - 1
        
        if p<0 or p >= num :
            print("page isn't in the range")
        else: 
            page= reader.pages[p]
            text = page.extract_text()
            
            print(f"==================page{p+1}==================")
            print(text)
            engine.say(text)
    
    except ValueError :
        print('pls enter a number or "all" ')
    
engine.runAndWait()




