try:
    from Tkinter import *
except:
    from tkinter import *

def f():
    return

class GameFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Test frame")

        top_frame = Frame(master, bg="red", width=200, height=200)
        top_frame.grid(row=0, column=0, columnspan=2, sticky=W+E+N+S) # , padx=10, pady=2)

        left_frame = Frame(master, bg="green", width=200, height=200)
        left_frame.grid(row=1, column=0, sticky=W+E+N+S)

        right_frame = Frame(master, bg="blue", width=200, height=200)
        right_frame.grid(row=1, column=1, sticky=W+E+N+S)

        bottom_frame = Frame(master, bg="red")
        bottom_frame.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S)

        bf = ButtonFrame(bottom_frame, {'one': lambda: eval("print('one clicked')"), 'two': lambda: eval("print('two clicked')")})
        bf.grid(row=0, column=0)

        b2 = Button(left_frame, text='show others', command=lambda: bf.grid())
        b2.grid(row=0, column=0)

        b2 = Button(left_frame, text='hide others', command=lambda: bf.hide('one'))
        b2.grid(row=1, column=0)


class ButtonFrame(Frame):
    def __init__(self, master, name_action_list, callback):
        Frame.__init__(self, master)
        self.grid()

        self.buttons = {}

        row = 0
        for ls in name_action_list:
            name = ls[0]

            def make_callback(s, ls):
                b = Button(self, text=name, command=lambda: callback(self, ls))
                b.grid(row=row, column=0, sticky=W+E+N+S)
                self.buttons[name] = b

            make_callback(self, ls)
            row += 1

    def hide(self, name):
        self.buttons[name].grid_forget()
