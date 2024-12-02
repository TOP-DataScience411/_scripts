from tkinter import Tk, Frame, Label, Entry, Button, StringVar


root = Tk()
root.title('Демонстратор GUI')
root.geometry('400x150+100+100')

mainframe = Frame(root, padx=10, pady=10)
mainframe.grid(row=0, column=0, sticky='nsew')

wdg_lbl = Label(mainframe, text='Введите новый заголовок:')
wdg_lbl.grid(row=0, column=0, sticky='nsew')

text = StringVar()

wdg_ent = Entry(mainframe, textvariable=text)
wdg_ent.grid(row=1, column=0, sticky='nsew', pady=10)

def change_title():
    root.title(text.get())

wdg_btn = Button(
    mainframe, 
    text='Изменить заголовок',
    command=change_title,
)
wdg_btn.grid(row=2, column=0, sticky='ns')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.columnconfigure(0, weight=1)

root.mainloop()

