from Tkinter import *
THRESHOLD=0

def show_values():
    print(w1.get(), w2.get())

master = Tk()
w1 = Scale(master, from_=0, to=42)
w1.pack()
w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w2.pack()
Button(master, text='Show', command=show_values).pack()

# Label(master, text=f"{THRESHOLD}")

mainloop()