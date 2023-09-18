from tkinter import*
from PIL import ImageTk,Image

def text_100(text):
    final_text=''
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+='\n'
    return final_text

root=Tk()
root.title('News')

texts=[]
photos=[]
for i in range(0,3):
    with open(f'{i+1}.txt') as f:
        text=f.read()
        texts.append(text_100(text))

    image=Image.open(f'{i+1}.png')

    image=image.resize((165,165),Image.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))
    

f=Frame(root,width=1000,height=70)

Label(f,text='Latest News',font='Lucida 30 bold',bg='silver').pack(fill=X)
Label(f,text='March 07, 2023 ,Tuesday',width=20,height=1,bg='silver',font='Lucida 10 bold').pack(fill=X)

f.pack(fill=X)


f1=Frame(root,width=900,height=700,pady=20,bg='silver')
f2=Frame(root,width=900,height=700,pady=20,bg='silver')
f3=Frame(root,width=900,height=700,pady=20,bg='silver')


c=Canvas(f1,width=1000,height=1,bg='silver')
line=c.create_line(0,1,1000,1)
c.pack()

Label(f1,text=text_100(texts[0]),padx=5,pady=5,bg='silver').pack(side=LEFT)
Label(f2,text=text_100(texts[1]),pady=5,bg='silver').pack(side=RIGHT)
Label(f3,text=text_100(texts[2]),padx=5,pady=5,bg='silver').pack(side=LEFT)

f1.pack(anchor="w",fill=X)
f2.pack(fill=X)
f3.pack(fill=X)


Label(f1,image=photos[0],anchor='e',bg='silver').pack(fill=Y)
Label(f2,image=photos[1],anchor='w',pady=80,bg='silver').pack()
Label(f3,image=photos[2],anchor='e',pady=80,bg='silver').pack()

root.mainloop()
