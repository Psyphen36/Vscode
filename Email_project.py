from tkinter import*
import tkinter.messagebox as msg 
root = Tk()
root.geometry('600x500')
root.title('Email')

def email_Entry():
    email = mail_value.get()
    password = pass_value.get()
    k,j,l = 0,0,0
    if len(email)>= 16:
        if email[0].isalpha():
            if ('@' in email) and email.count('@')==1:
                if (email[-3]=='.') ^ (email[-4]=='.'):
                    for i in email:
                        if i==i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i==i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i=='_' or i=='.' or i=='@':
                            continue
                        else:
                            l=1
                    if k==1 or j==1 or l==1:
                        text = '''You can probably do one or more than one mistake you can just read these steps to fix your email:
1. You can't use space( ) in email.
2. You can't use capital letters in your email.
3. You can only enter ("_", ".", "@") these types of punctuation in your email.'''

                        msg.showinfo(f'{email} is wrong input!!!',text)
                    else:
                        if password=='':
                            text = 'Oh no! you forgot to enter your password'
                            msg.showinfo('Oops!',text)
                        else:
                            text = f'''You entered your email in a right way.
    Your email is: {email}
    Your password is: {password}'''
                            msg.showinfo('Congratulations!',text)
                else:
                    text = 'Please Enter dot (".") in a correct position Or check your character\'s after using "."'
                    msg.showinfo(f'{email} is wrong input!!!',text)
            else:
                text = '1. If you forget to enter "@" in your email please Do that.\t\t2. If not than please enter "@" only one time'
                msg.showinfo(f'{email} is wrong input!!!',text)
        else:
            text = 'Your first character is to be an alphabet'
            msg.showinfo(f'{email} is wrong input!!!',text)
    else:
        text = 'Please enter minimum six character email'
        msg.showinfo(f'{email} is wrong input!!!',text)

if __name__ == '__main__':
    lbl1 = Label(root,text='Email ',anchor=NE,font='Helvica 15 bold' )
    lbl2 = Label(root,text='Password ',anchor=NE,font='Helvica 15 bold' )
    lbl1.grid(column=0,row=0)
    lbl2.grid(column=0,row=1)

    mail_value = StringVar()
    pass_value = StringVar()

    enter1 = Entry(root,width=20,textvariable = mail_value,font='Helvica 15')
    enter2 = Entry(root,width=20,textvariable = pass_value,font='Helvica 15')

    enter1.grid(column=1,row=0,pady=15)
    enter2.grid(column=1,row=1,pady=15)


    Button(root,text='Enter',command=email_Entry).grid(column=1,ipadx=16,ipady=5)

    root.mainloop()


