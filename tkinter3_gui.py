from tkinter import *

ws = Tk()
ws.title('Morning Routine')
ws.geometry('400x200')
ws.config(bg='#000000')

name_var = StringVar()
age_var = IntVar()
age_var.set(18)

def callback():
    disp.config(text=f'Your favorite city is {name_var.get().capitalize()}')
    return True

frame = Frame(
	ws,
	padx=10,
	pady=10,
	bg='#F2BD1D'
)
frame.pack(pady=20)

Label(
	frame,
	text='CONFIRM WAKE UP TIME',
	font=('sans-serif', 14),
	bg='#F2BD1D'
).grid(row=0, column=0)

Entry(
	frame, 
	textvariable=name_var, 
	validate='focusout', 
	validatecommand=callback,
	font=('sans-serif', 14)
	).grid(row=0, column=1, padx=10)


# this entry widget is used to change the focus
Entry(
	frame,
	width=2
).grid(row=1, columnspan=2, padx=10)

disp = Label(
	frame,
	text='tap tab',
	font=('sans-serif', 14),
	relief=SOLID,
	padx=10,
	pady=10
)
disp.grid(row=2, columnspan=2, pady=20)

ws.mainloop()