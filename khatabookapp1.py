from tkinter import *
from tkinter.messagebox import showinfo
import datetime

root = Tk()
root.minsize(500, 500)
root.maxsize(600, 500)
root.title("Khata Book App")

__thisMenuBar = Menu(root)
__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
root.config(menu=__thisMenuBar)
expression = ""


def calculator():
    # Python program to  create a simple GUI
    # calculator using Tkinter

    # globally declare the expression variable
    def __quit():
        gui.destroy()

    # Function to update expressiom
    # in the text entry box
    def press(num):
        # point out the global expression variable
        global expression

        # concatenation of string
        expression = expression + str(num)

        # update the expression by using set method
        equation.set(expression)

    # Function to evaluate the final expression
    def equalpress():
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        try:

            global expression

            # eval function evaluate the expression
            # and str function convert the result
            # into string
            total = str(eval(expression))

            equation.set(total)

            # initialze the expression variable
            # by empty string
            expression = ""

        # if error is generate then handle
        # by the except block
        except:

            equation.set(" error ")
            expression = ""

    # Function to clear the contents
    # of text entry box
    def clear():
        global expression
        expression = ""
        equation.set("")

    # Driver code
    # create a GUI window

    gui = Toplevel(root)

    # set the background colour of GUI window
    gui.configure(background="grey")

    # set the title of GUI window
    gui.title("Simple Calculator design by vikash kumar")

    # set the configuration of GUI window
    gui.minsize(400, 460)
    gui.maxsize(400, 460)

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation, font="None 18 bold")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('enter your expression')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='grey',
                     command=lambda: press(1), height=5, width=13)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='grey',
                     command=lambda: press(2), height=5, width=13)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='grey',
                     command=lambda: press(3), height=5, width=13)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='grey',
                     command=lambda: press(4), height=5, width=13)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='grey',
                     command=lambda: press(5), height=5, width=13)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='grey',
                     command=lambda: press(6), height=5, width=13)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='grey',
                     command=lambda: press(7), height=5, width=13)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='grey',
                     command=lambda: press(8), height=5, width=13)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='grey',
                     command=lambda: press(9), height=5, width=13)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='grey',
                     command=lambda: press(0), height=5, width=13)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='grey',
                  command=lambda: press("+"), height=5, width=13)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='grey',
                   command=lambda: press("-"), height=5, width=13)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='grey',
                      command=lambda: press("*"), height=5, width=13)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='grey',
                    command=lambda: press("/"), height=5, width=13)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='grey',
                   command=equalpress, height=5, width=13)
    equal.grid(row=5, column=2)

    buttonmod = Button(gui, text=' % ', fg='black', bg='grey',
                       command=lambda: press('%'), height=5, width=13)
    buttonmod.grid(row=5, column=1)

    Decimal = Button(gui, text='.', fg='black', bg='grey',
                     command=lambda: press('.'), height=5, width=13)
    Decimal.grid(row=6, column=0)
    button00 = Button(gui, text=' 00 ', fg='black', bg='grey',
                      command=lambda: press('00'), height=5, width=13)
    button00.grid(row=6, column=1)
    clear = Button(gui, text='Clear', fg='red', bg='blue',
                   command=clear, height=5, width=13)
    clear.grid(row=6, column='2')
    Button(gui, text='exit', fg='red', bg='blue', command=__quit, height=5, width=13).grid(row=6, column=3)
    # start the GUI
    gui.mainloop()


def add():
    with open('khatabook.txt', 'a') as f:
        f.write(
            f"{customervalue.get()}        {addressvalue.get()}           {amountvalue.get()}        {datetime.datetime.now()}\n")
    showinfo(f"{customervalue.get()} Khata",
             f"Address:\t{addressvalue.get()}\n\nAmount Added in {customervalue.get()} Khata : {amountvalue.get()}")
    customerentry.delete(0, END)
    addressentry.delete(0, END)
    amountentry.delete(0, END)


def __quitApplication():
    root.destroy()
    # exit()


def __showAbout():
    showinfo("Khata Book App", " design by vikash kumar")


def total():
    with open('khatabook.txt', 'r') as f:
        su = 0
        for line in f:
            line = line.rstrip()
            if not line.startswith(f"{customervalue.get()}        {addressvalue.get()}        "): continue
            words = line.split("        ")
            su = su + float(words[2])
        showinfo(f"{customervalue.get()} Khata", f"Address:\t{addressvalue.get()}\n\nTotal amount : {su}")
        customerentry.delete(0, END)
        addressentry.delete(0, END)
        amountentry.delete(0, END)


def __delete():
    with open('khatabook.txt', 'r+') as f:
        f.seek(0)
        f.truncate()


def detail():
    with open('khatabook.txt', 'r') as f:
        su = ""
        for line in f:
            line = line.rstrip()
            if not line.startswith(f"{customervalue.get()}        {addressvalue.get()}        "): continue
            words = line.split("        ")
            su = su.__add__(f"{words[2]}\t{words[3]}\n")
        showinfo(f"{customervalue.get()} Khata", f"Address:\t{addressvalue.get()}\n\nAmount details :\n {su}")
        customerentry.delete(0, END)
        addressentry.delete(0, END)
        amountentry.delete(0, END)


__thisFileMenu.add_command(label="Exit",
                           command=__quitApplication)
__thisMenuBar.add_cascade(label="File",
                          menu=__thisFileMenu)
__thisHelpMenu.add_command(label="About Khata Book App",
                           command=__showAbout)
__thisHelpMenu.add_command(label="Delete All Account",
                           command=__delete)
__thisMenuBar.add_cascade(label="Help",
                          menu=__thisHelpMenu)
f1 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f1.grid(row=1, column=2, pady=10)
Label(f1, text="Welcome To My Khata Book App", font="Helvetica 12 bold", fg="green", borderwidth=8, relief=SUNKEN).grid(
    pady=20)
Label(root, text="Name of Customer", font="Helvetica 12 bold").grid(pady=10, row=4, column=0)
Label(root, text="Address of Customer", font="Helvetica 12 bold").grid(pady=10, row=5, column=0)
Label(root, text="Amount", font="Helvetica 12 bold").grid(pady=10, row=6, column=0)
customervalue = StringVar()
addressvalue = StringVar()
amountvalue = StringVar()
customerentry = Entry(root, textvariable=customervalue, font="Helvetica 12 bold", borderwidth=6, relief=SUNKEN)
addressentry = Entry(root, textvariable=addressvalue, font="Helvetica 12 bold", borderwidth=6, relief=SUNKEN)
amountentry = Entry(root, textvariable=amountvalue, font="Helvetica 12 bold", borderwidth=6, relief=SUNKEN)
customerentry.grid(row=4, column=2, pady=8)
addressentry.grid(row=5, column=2, pady=8)
amountentry.grid(row=6, column=2, pady=8)
Button(root, text="Save", font="Helvetica 16 bold", bg="red", command=add).grid(row=10, column=2, pady=6)
Button(root, text="View Total Amount", font="Helvetica 16 bold", bg="red", command=total).grid(row=12, column=2,
                                                                                               pady=6)
Button(root, text="View Account details", font="Helvetica 16 bold", bg="red", command=detail).grid(row=14, column=2,
                                                                                                   pady=6)
Button(root, text="Calculator", font="Helvetica 16 bold", bg="blue", command=calculator).grid(row=16, column=2, pady=6)
root.mainloop()
