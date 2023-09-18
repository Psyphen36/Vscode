from tkinter import *
import speedtest as speedtest


def check_speed():
    label = Label(root,text='Please wait for a moment...',bg='cyan')
    label.place(x=200,y=250)    
    label.update()
    speed = speedtest.speedtest()
    speed.get_servers()
    down = str(round(speed.download()/(10**6),3))+ 'Mbps'
    up = str(round(speed.upload()/(10**6),3))+ 'Mbps'
    internet_download.config(text=down)
    internet_upload.config(text=up)

    label.config(text='Thanks for waiting. ',font='helvica 10 bold')
    label.update()

if __name__ == '__main__':
    root = Tk()
    root.title('Internet Speed test')
    root.geometry('500x350')

    root.config(bg='cyan')

    lbl_down = Label(root,text='Downloading Speed',font='Helvica 14 bold',bg='cyan')
    lbl_down.place(x=150,y=20)

    internet_download = Label(root,text ='00',font='Helvica 14 bold',bg='White',relief='sunken')
    internet_download.place(x=150,y=50,width=200)

    lbl_up = Label(root,text='Downloading Speed',font='Helvica 14 bold',bg='cyan')
    lbl_up.place(x=150,y=120)

    internet_upload = Label(root,text ='00',font='Helvica 14 bold',bg='White',relief='sunken')
    internet_upload.place(x=150,y=150,width=200)

    button = Button(root,text='Check Speed',command = check_speed)
    button.place(x=200,y=210)
    
    root.mainloop()