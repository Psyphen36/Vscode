
from tkinter import * 

root = Tk()
root.geometry('1000x700')
root.title('Mad Libs game')

Label(root,text='Mad Libs games \n have fun',font='ariel 20 bold').grid()
Label(root,text='Click Any One:',font='ariel 15 bold').place(x=40,y=80)

def madLib1():
    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madLib2():
    Label(root,text='adjective',font='ariel 15 bold').place(x=40,y=200)
    Label(root,text='color',font='ariel 15 bold').place(x=550,y=200)
    Label(root,text='thing',font='ariel 15 bold').place(x=40,y=250)
    Label(root,text='place',font='ariel 15 bold').place(x=550,y=250)
    Label(root,text='person',font='ariel 15 bold').place(x=40,y=300)
    Label(root,text='adjective1',font='ariel 15 bold').place(x=490,y=300)
    Label(root,text='insect',font='ariel 15 bold').place(x=40,y=350)
    Label(root,text='food',font='ariel 15 bold').place(x=550,y=350)
    Label(root,text='verb',font='ariel 15 bold').place(x=40,y=400)

    adjective = StringVar()
    color = StringVar()
    thing = StringVar()
    place = StringVar()
    person = StringVar()
    adjective1 = StringVar()
    insect = StringVar()
    food = StringVar()
    verb = StringVar()

    result_label = Label(root, font='arial 15 bold')
    result_label.place(x=25, y=480)

    def show_result():
        result = (
        'Last night I dreamed I was a ' + adjective.get() +
        ' butterfly with ' + color.get() +
        ' splotches that \n looked like ' + thing.get() +
        '. I flew to ' + place.get() +
        ' with my best friend \n' + person.get() +
        ' who was a ' + adjective1.get() +
        ' ' + insect.get() +
        '. We ate\n some ' + food.get() +
        ' when we got there and then decided \n to ' + verb.get() +
        ' and the dream ended when I said-- lets ' + verb.get() + '.')
        result_label.config(text=result)

    enter1 = Entry(root, width=20, textvariable=adjective, font='Helvica 15')
    enter2 = Entry(root, width=20, textvariable=color, font='Helvica 15')
    enter3 = Entry(root, width=20, textvariable=thing, font='Helvica 15')
    enter4 = Entry(root, width=20, textvariable=place, font='Helvica 15')
    enter5 = Entry(root, width=20, textvariable=person, font='Helvica 15')
    enter6 = Entry(root, width=20, textvariable=adjective1, font='Helvica 15')
    enter7 = Entry(root, width=20, textvariable=insect, font='Helvica 15')
    enter8 = Entry(root, width=20, textvariable=food, font='Helvica 15')
    enter9 = Entry(root, width=20, textvariable=verb, font='Helvica 15')

    enter1.place(x=160, y=200)
    enter2.place(x=620, y=200)
    enter3.place(x=160, y=250)
    enter4.place(x=620, y=250)
    enter5.place(x=160, y=300)
    enter6.place(x=620, y=300)
    enter7.place(x=160, y=350)
    enter8.place(x=620, y=350)
    enter9.place(x=160, y=400)



    submit_button = Button(root, text='Submit', font='arial 15 bold', command=show_result)
    submit_button.place(x=780, y=450)

Button(root,text='The Photographer',font='ariel 15 bold italic',command=madLib1,bg='ghost white').place(x=40,y=120)
Button(root,text='A Dream',font='ariel 15 bold italic',command=madLib2,bg='ghost white').place(x=300,y=120)

root.mainloop()
