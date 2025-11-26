import pyttsx3
from pypdf import PdfReader
import tkinter as tk
from tkinter import messagebox

reader = PdfReader("Chapter 2 Numerical Sequences v2.pdf") #just a pdf from uni for trying
num = len(reader.pages)
engine = pyttsx3.init()

root = tk.Tk()#creat
root.title ("pdf reader")
root.geometry ("400x200")
root.configure(bg="#f3f3f3")

panel = tk.Frame(root, bg="#ffffff" , bd=1 , relief="solid")
panel.place(relx=0.5, rely=0.5, anchor="center", width=340, height=200)

label = tk.Label(
    panel,
    text="read pdf page",
    bg ="#ffffff",
    fg="#333333",
    font=("segoe UI" , 13, "bold")
)
label.pack(pady=10)

sub = tk.Label(
    panel,
    text = "enter 'all' or a page number",
    bg = "#ffffff",
    fg = "#555555",
    font = ("segoe UI" , 10)
)
sub.pack()

entry = tk.Entry (
    panel,
    width = 22,
    font =("segoe UI" , 11),
    bg = "#f5f5f5",
    fg = "#222222",
    relief= "flat",
    highlightthickness=1,
    highlightcolor = "#a0a0a0",
    highlightbackground="#cccccc",
    insertbackground ="black"
    
)
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
                messagebox.showerror("page isn't in the range" , "error")
                return
            else: 
                page= reader.pages[p]
                text = page.extract_text()
            
            print(f"==================page{p+1}==================")
            print(text)
            engine.say(text)
    
        except ValueError :
             messagebox.showerror('pls enter a number or "all" ' , "error")
             return
    engine.runAndWait()  


button = tk.Button(
    panel, 
    text="Read PDF", 
    command=readpdf,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8" , 
    activeforeground="white" , 
    relief="flat" , 
    font=("segoe UI" , 11 , "bold"),
    padx=10,
    pady=5,
    bd=0
)

button.pack(pady=15)
button.configure(width=15)

root.mainloop()







