try:
    from tkinter import *
except:
    from Tkinter import *

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

        bf = ButtonFrame(bottom_frame, {'one': lambda: print('one clicked'), 'two': lambda: print('two clicked')})
        bf.grid(row=0, column=0)

        b2 = Button(left_frame, text='show others', command=lambda: bf.grid())
        b2.grid(row=0, column=0)

        b2 = Button(left_frame, text='hide others', command=lambda: bf.hide('one'))
        b2.grid(row=1, column=0)


class LoginFrame(Toplevel):
    def __init__(self, master, sign_in_callback, create_account_callback):
        Toplevel.__init__(self, master)
        self.grid()

        l = Label(self, text='Please enter your username.')
        l.grid(row=0, column=0)

        username_entry = Entry(self, show='')
        username_entry.grid(row=1, column=0)
        username_entry.focus()

        b1 = Button(self, text='Log in', command=lambda: sign_in_callback(self, username_entry.get()))
        b1.grid(row=2, column=0)

        b2 = Button(self, text='Create account under username', command=lambda: create_account_callback(self, username_entry.get()))
        b2.grid(row=3, column=0)


class ItemFrame(Frame):
    def __init__(self, master, button_text, label_text, callback):
        Frame.__init__(self, master)
        self.grid()

        self.button_string_var = StringVar()

        self.button = Button(self, textvariable=self.button_string_var, command=callback, width=30)
        self.button.grid(row=0, column=0) # , sticky=W)

        self.label_string_var = StringVar()

        self.label = Label(self, textvariable=self.label_string_var)
        self.label.grid(row=0, column=1) # , sticky=E, columnspan=1)

        self.update(button_text, label_text)


    def update(self, button_text, label_text):
        self.button_string_var.set(button_text)
        self.label_string_var.set(label_text)


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

