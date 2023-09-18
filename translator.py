from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES,Translator

def change(text='type',src='English',dest='Hindi'):
    text1 = text
    src1 = src 
    dest1 = dest
    translate = Translator()
    trans1 = translate.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    text_get = change(text= msg,src=s,dest=d) 
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,text_get)




root=Tk()
root.title('translator')
root.geometry('500x700')
root.config(bg='cyan')

lbl_txt = Label(root,text='Translator',font='Helvica 40 bold',bg='cyan')
lbl_txt.place(x=100,y=40,height=50,width=310)

frame = Frame(root).pack(side=BOTTOM)

lbl_txt= Label(root,text='Source Text',font='Helvica 20 bold',fg='red',bg='cyan')
lbl_txt.place(x=100,y=100,height=30,width=310)

sor_txt = Text(frame,font='Helvica 20 bold',wrap=WORD,relief=SUNKEN)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=12,y=300,height=40,width=150)
comb_sor.set('english')

button_change = Button(frame,text='Translate',relief=RAISED,command=data)
button_change.place(x=175,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=340,y=300,height=40,width=150)
comb_dest.set('english')

lbl_txt= Label(root,text='Destination Text',font='Helvica 20 bold',fg='red',bg='cyan')
lbl_txt.place(x=100,y=360,height=30,width=310)

dest_txt = Text(frame,font='Helvica 20 bold',wrap=WORD,relief=SUNKEN)
dest_txt.place(x=10,y=390,height=150,width=480)


root.mainloop()
