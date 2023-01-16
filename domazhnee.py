from tkinter import *

num1 = int(0)

class Tkinter(Tk):

    def __init__(self):
        super().__init__()
        self.b1 = Button(self, text='прибавить', font='Arial 20', padx=30, pady=30, command=self.plus)
        self.b2 = Button(self, text='вычесть', font='Arial 20', padx=90, pady=30, command=self.minus)
        self.b3 = Button(self, text='обнулить', font='Arial 20', padx=600, pady=30, command=self.reset)
        self.b1.grid(row=0, column=1)
        self.b1.grid(row=0, column=2)
        self.b1.grid(row=0, column=3)

        self.value = Label(self, text='0', font='Arial 35')

        self.value.grid(row=0, column=0)

    def plus(self):
        global num1
        num1 += 1


    def minus(self):
        global num1
        num1 -= 1

    def reset(self):
        global num1
        num1 == 0

if __name__ == "__main__":

    t = Tkinter()

    Tkinter.mainloop(self=t)