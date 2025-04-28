import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Taschenrechner_tk")
root.geometry("500x500")
root.minsize(width=900, height=900)

fontgeneral=font.Font(size=60,family="Arial")

eingabe= tk.Entry(root,font=fontgeneral,borderwidth=60, background="black", foreground="grey")
eingabe.grid(row=0,column=0,columnspan=4,sticky="nswe")

def addChar(char):
   eingabe.insert(tk.END,char)


def clear_entry():
   eingabe.delete(0,tk.END)


def show_result():
   try:
       result = eval(eingabe.get())
       eingabe.delete(0,tk.END)
       eingabe.insert(0,str(result))

   except:
      eingabe.delete(0, tk.END)
      eingabe.insert(0, "ERROR!!!!")


button1 = tk.Button(root,text="1",font=fontgeneral, command=lambda: addChar('1'),background="black",foreground="brown", borderwidth=10)
button2 = tk.Button(root,text="2",font=fontgeneral, command=lambda: addChar('2'),background="black",foreground="brown", borderwidth=10)
button3 = tk.Button(root,text="3",font=fontgeneral, command=lambda: addChar('3'),background="black",foreground="brown", borderwidth=10)
button4 = tk.Button(root,text="4",font=fontgeneral, command=lambda: addChar('4'),background="black",foreground="brown", borderwidth=10)
button5 = tk.Button(root,text="5",font=fontgeneral, command=lambda: addChar('5'),background="black",foreground="brown", borderwidth=10)
button6 = tk.Button(root,text="6",font=fontgeneral, command=lambda: addChar('6'),background="black",foreground="brown", borderwidth=10)
button7 = tk.Button(root,text="7",font=fontgeneral, command=lambda: addChar('7'),background="black",foreground="brown", borderwidth=10)
button8 = tk.Button(root,text="8",font=fontgeneral, command=lambda: addChar('8'),background="black",foreground="brown", borderwidth=10)
button9 = tk.Button(root,text="9",font=fontgeneral, command=lambda: addChar('9'),background="black",foreground="brown", borderwidth=10)
button0 = tk.Button(root,text="0",font=fontgeneral, command=lambda: addChar('0'),background="black",foreground="brown", borderwidth=10)

button_plus = tk.Button(root,text="+",font=fontgeneral, command=lambda: addChar('+'), background="black", foreground="brown", borderwidth=10)
button_minus = tk.Button(root,text="-",font=fontgeneral, command=lambda: addChar('-'), background="black", foreground="brown", borderwidth=10)
button_mul = tk.Button(root,text="*",font=fontgeneral, command=lambda: addChar('*'),background="black", foreground="brown", borderwidth=10)
button_div = tk.Button(root,text="/",font=fontgeneral, command=lambda: addChar('/'), background="black", foreground="brown", borderwidth=10)

button_clear= tk.Button(root,text="Clear",font=fontgeneral, command=clear_entry, background="black", foreground="brown", borderwidth=10)
button_result=tk.Button(root,text="=",font=fontgeneral,command=show_result, background="black", foreground="brown", borderwidth=10)

button7.grid(row=1,column=0,sticky="nswe")
button8.grid(row=1,column=1,sticky="nswe")
button9.grid(row=1,column=2,sticky="nswe")
button_clear.grid(row=1,column=3,sticky="nswe", )

button4.grid(row=2,column=0,sticky="nswe")
button5.grid(row=2,column=1,sticky="nswe")
button6.grid(row=2,column=2,sticky="nswe")
button_minus.grid(row=2,column=3,sticky="nswe")

button1.grid(row=3,column=0,sticky="nswe")
button2.grid(row=3,column=1,sticky="nswe")
button3.grid(row=3,column=2,sticky="nswe")
button_plus.grid(row=3,column=3,sticky="nswe")

button_mul.grid(row=4,column=0,sticky="nswe")
button0.grid(row=4,column=1,sticky="nswe")
button_div.grid(row=4,column=2,sticky="nswe")
button_result.grid(row=4,column=3,sticky="nswe")

for column in range(4):
   root.columnconfigure(column,weight=1)
for row in range(5):
   root.rowconfigure(row,weight=1)



root.mainloop()
