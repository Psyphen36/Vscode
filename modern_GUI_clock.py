import customtkinter
from time import strftime

root = customtkinter.CTk()
root.geometry('500x300')
root.title('Modern_clock')

def clock_time():
    string = strftime('%H:%M:%S %p')
    clock_lbl.configure(text=string)
    clock_lbl.after(1000, clock_time)

hr_lbl = customtkinter.CTkLabel(root, text='H', font=('ds-digital', 30, 'bold'), text_color='yellow')

min_lbl = customtkinter.CTkLabel(root, text='M', font=('ds-digital', 30, 'bold'), text_color='yellow')
sec_lbl = customtkinter.CTkLabel(root, text='S', font=('ds-digital', 30, 'bold'), text_color='yellow')
am_pm_lbl = customtkinter.CTkLabel(root, text='AM/PM', font=('ds-digital', 20, 'bold'), text_color='yellow')
clock_lbl = customtkinter.CTkLabel(root, font=('ds-digital',35, 'bold'), fg_color='white', text_color='purple')

hr_lbl.place(x=160, y=90)
min_lbl.place(x=220, y=90)
sec_lbl.place(x=285, y=90)
am_pm_lbl.place(x=320, y=94)
clock_lbl.place(x=150, y=120)

clock_time()
root.mainloop()