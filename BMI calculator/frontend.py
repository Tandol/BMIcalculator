from distutils import command
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

GUI = Tk()
GUI.configure(bg = '#ECC8A1')
L1 = Label(GUI, text = "BMI Calculator" , font = ('Times', '35','bold'), fg = '#80945F', bg = '#ECC8A1')
L1.place(x = 10, y = 20)
GUI.title('BMI calculator')
GUI.geometry('900x500')

def wcsv(datalist) :
    with open('BMI.csv', 'a', encoding = 'utf-8', newline = '') as file : #a = append
        fw = csv.writer(file) # fw = file writter
        fw.writerow(datalist) #[]

FB1 = LabelFrame(GUI,text = 'Forms' ,font = ('Times', '30','bold'), fg = '#80945F', bg = '#ECC8A1')
FB1.place(x = 175, y = 100)
L2 = Label(FB1, text = '', font = ('Times', '28','bold'), fg = '#CE8879',bg = '#ECC8A1' )
L2.pack(ipadx = 150,ipady = 50, padx = 130 , pady = 25 )

def Button3() :
    text = 'Deposite'
    messagebox.showwarning(message = 'Are you sure')
    
def bmi() :
    print(h_data.get())
    print(w_data.get())
    inth = float(h_data.get())
    intw = float(w_data.get())
    if(inth > 100) :
        inth = inth/100
    ansbmi = intw / (inth * inth)
    print(ansbmi)
    showbmi(ansbmi,inth,intw)

    
L3 = Label(GUI, text = "Height : " , font = ('Times', '28'), fg = '#80945F',bg = '#ECC8A1')
L3.place(x = 200, y = 150)

L5 = Label(GUI, text = "cm" , font = ('Times', '28'), fg = '#80945F',bg = '#ECC8A1')
L5.place(x = 600, y = 150)

h_data = StringVar()
h_data.get()
E1 = ttk.Entry(textvariable = h_data, font = ('Times', '28'))
E1.place(x = 305, y = 150)

L4 = Label(GUI, text = "Weight : " , font = ('Times', '28'), fg = '#80945F',bg = '#ECC8A1')
L4.place(x = 200, y = 220)

L6 = Label(GUI, text = "Kg" , font = ('Times', '28'), fg = '#80945F',bg = '#ECC8A1')
L6.place(x = 610, y = 230)

w_data = StringVar()
w_data.get()
E2 = ttk.Entry(textvariable = w_data, font = ('Times', '28'))
E2.place(x = 310, y = 227)


B3 = ttk.Button(text = 'Calculate', command = bmi)
B3.pack(ipadx = 20, ipady = 30)
B3.place(x = 600, y = 320)

def     showbmi(ansbmi,inth,intw) :
    shwbmi = str(ansbmi)
    messagebox.askyesno(message = 'Your BMI is ' + shwbmi)
    data = [inth , intw, ansbmi]
    wcsv(data)
    


GUI.mainloop()

