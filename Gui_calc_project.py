from tkinter import*

root=Tk()
root.title('Calculator')

root.geometry('450x510')

def touch(event):
    global entry_value

    text=event.widget.cget('text')

    if text=='=':
        if entry_value.get().isdigit():
            value=int(entry_value.get())
        else:
            try:
                value=eval(Screen.get())
            except Exception as e:
                print(e)
                value='ERROR'
        entry_value.set(value)
        Screen.update()

            
    elif text=='c':
        entry_value.set('')
        Screen.update()

    else:
        entry_value.set(entry_value.get()+text)
        Screen.update()


entry_value=StringVar()
entry_value.set('')

Screen=Entry(root, textvariable=entry_value, font='Lucida 20 bold')
Screen.pack(fill=X,padx=20,pady=20,ipady=5)


f=Frame(root,bg='grey')

b=Button(f,text='c',bg='DarkOrange',activebackground='yellow')
b.pack(side=LEFT,ipadx=45,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='/',bg='grey')
b.pack(side=LEFT,ipadx=45,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='*',bg='grey')
b.pack(side=LEFT,ipadx=45,ipady=25)
b.bind('<Button-1>',touch)
f.pack()


f=Frame(root,bg='grey')
b=Button(f,text='7',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='8',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='9',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)
f.pack()



f=Frame(root,bg='grey')

b=Button(f,text='4',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='5',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='6',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)
f.pack()




f=Frame(root,bg='grey')

b=Button(f,text='1',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='2',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='3',bg='grey')
b.pack(side=LEFT,ipadx=44,ipady=25)
b.bind('<Button-1>',touch)
f.pack()




f=Frame(root,bg='grey')

b=Button(f,text='0',bg='grey')
b.pack(side=LEFT,ipadx=25,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='-',bg='grey')
b.pack(side=LEFT,ipadx=30,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='+',bg='grey')
b.pack(side=LEFT,ipadx=30,ipady=25)
b.bind('<Button-1>',touch)

b=Button(f,text='=',bg='Green',activebackground='LightGreen')
b.pack(side=LEFT,ipadx=26,ipady=25)
b.bind('<Button-1>',touch)
f.pack()
root.mainloop()






























