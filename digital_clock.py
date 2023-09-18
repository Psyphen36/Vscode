from tkinter import*
import datetime

def Dt():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')


    lbl_hr.config(text=hr)
    lbl_min.config(text=min)
    lbl_sec.config(text=sec)
    lbl_am.config(text=am)

    dd_lbl.config(text=date)
    mm_lbl.config(text=month)
    yy_lbl.config(text=year)
    day_lbl.config(text=day)

    lbl_hr.after(200,Dt)

root = Tk()
root.title(f'*****Digital Clock*****')
root.geometry('900x500')
root.config(bg='black')

#! Time
lbl_time = Label(root,text='Time',font='Helvica 30 bold italic',bg='black',fg='yellow')
lbl_time.place(x=340,y=10,height=50,width=200)

lbl_hr = Label(root,text='00',font=('Time New Roman', 40, 'bold'),bg='black',fg='red')
lbl_hr.place(x=100,y=80,height=50,width=100)

lbl_min = Label(root,text='00',font=('Time New Roman', 40, 'bold'),bg='black',fg='red')
lbl_min.place(x=300,y=80,height=50,width=100)

lbl_sec = Label(root,text='00',font=('Time New Roman', 40, 'bold'),bg='black',fg='red')
lbl_sec.place(x=500,y=80,height=50,width=100)

lbl_am = Label(root,text='00',font=('Time New Roman', 30, 'bold'),bg='black',fg='red')
lbl_am.place(x=700,y=80,height=50,width=100)



hr_txt = Label(root,text='Hour',bg='black',fg='red',font='Helvica 20 bold')
hr_txt.place(x=100,y=150,height=30,width=100)

min_txt = Label(root,text='Min',bg='black',fg='red',font='Helvica 20 bold')
min_txt.place(x=300,y=150,height=30,width=100)

sec_txt = Label(root,text='sec',bg='black',fg='red',font='Helvica 20 bold')
sec_txt.place(x=500,y=150,height=30,width=100)

am_txt = Label(root,text='Am/Pm',bg='black',fg='red',font='Helvica 18 bold')
am_txt.place(x=700,y=150,height=30,width=100)


#! Date

lbl_date = Label(root,text='Date',bg='black',fg='cyan',font='Helvica 30 bold')
lbl_date.place(x=10,y=250,height=50,width=880)


dd_lbl = Label(root,text='00',bg='black',fg='red',font='Helvica 40 bold')
dd_lbl.place(x=100,y=340,height=50,width=100)

mm_lbl = Label(root,text='00',bg='black',fg='red',font='Helvica 40 bold')
mm_lbl.place(x=300,y=340,height=50,width=100)

yy_lbl = Label(root,text='00',bg='black',fg='red',font='Helvica 40 bold')
yy_lbl.place(x=500,y=340,height=50,width=100)

day_lbl = Label(root,text='00',bg='black',fg='red',font='Helvica 25  bold')
day_lbl.place(x=700,y=340,height=50,width=100)

dd_txt = Label(root,text='day',bg='black',fg='red',font='Helvica 20 bold')
dd_txt.place(x=100,y=400,height=30,width=100)

mm_txt = Label(root,text='month',bg='black',fg='red',font='Helvica 20 bold')
mm_txt.place(x=300,y=400,height=30,width=100)

yy_txt = Label(root,text='year',bg='black',fg='red',font='Helvica 20 bold')
yy_txt.place(x=500,y=400,height=30,width=100)

day_txt = Label(root,text='weekday',bg='black',fg='red',font='Helvica 20 bold')
day_txt.place(x=680,y=400,height=30,width=150)

Dt()
root.mainloop()