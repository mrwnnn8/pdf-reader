import pyttsx3
from pypdf import PdfReader
import tkinter as tk
from tkinter import messagebox

reader = PdfReader("Chapter 2 Numerical Sequences v2.pdf") #just a pdf from uni for trying
num = len(reader.pages)
engine = pyttsx3.init()

root = tk.Tk()
root.title ("pdf reader")
root.geometry ("400x200")

label = tk.Label(root, text="To read all pages or a chosen one, enter 'all' or a page number")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

def  readpdf(): 
    p = entry.get().strip().lower()
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


button = tk.Button(root, text="Read PDF", command=readpdf)
button.pack(pady=20)

root.mainloop()


