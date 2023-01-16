#Importing all the modules
from tkinter import *

#Creating a window
window=Tk()
window.geometry("350x500")
window.title("Calculator")
window.configure(bg="#3399ff")
#Changing the default icon of the root window
window.iconbitmap("calculator_icon.ico")

#Initiating the expressions
expression=''
def press(n):
    global expression
    expression+=str(n)
    equation.set(expression)

#Evaluation of expressions ("Exception Handling for if divisor==0")
def equal():
    try:
        global expression
        total=str(eval(expression))         #Python default eval function to evaluate an expression
        equation.set(total)
        expression=''                       #Remove the older entered expression
    except:
        equation.set("Error")               #if dividing by zero
        expression=''

#Clearing the entire expression
def clear():
    global expression
    expression=''
    equation.set('0')

#Clearing the expression specifically
def backspace():
    global expression
    expression=expression.rstrip(expression[-1])
    equation.set(expression)

#Expression frame to see expressions and buttons frame to place buttons
expression_frame=Frame(window,bg="#3399ff")
buttons_frame=Frame(window,bg="#3399ff")
expression_frame.pack()
buttons_frame.pack()

#Setting the font styles and font types
font_entry=("ariel",20,"bold")              #(fonttype,font size,fontstyle)
font_button=("new times roman",12)
equation=StringVar()                        #(User input to the widget)
equation.set('0')                           #(Setting the default value to zero)

#Equation(Entry widget)
equation_field=Entry(expression_frame,textvariable=equation,font=font_entry,justify="right")
equation_field.pack(ipadx=10,ipady=10,pady=20)

#Creating buttons
button1=Button(buttons_frame,text="1",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(1))
button2=Button(buttons_frame,text="2",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(2))
button3=Button(buttons_frame,text="3",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(3))
plus=Button(buttons_frame,text="+",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press("+"))
button4=Button(buttons_frame,text="4",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(4))
button5=Button(buttons_frame,text="5",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(5))
button6=Button(buttons_frame,text="6",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(6))
minus=Button(buttons_frame,text="-",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press("-"))
button7=Button(buttons_frame,text="7",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(7))
button8=Button(buttons_frame,text="8",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(8))
button9=Button(buttons_frame,text="9",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(9))
multiply=Button(buttons_frame,text="*",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press("*"))
button0=Button(buttons_frame,text="0",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press(0))
decimal=Button(buttons_frame,text=".",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press("."))
clear=Button(buttons_frame,text="C",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=clear)
divide=Button(buttons_frame,text="/",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=lambda:press("/"))
equal=Button(buttons_frame,text="=",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=equal)
backspace=Button(buttons_frame,text="<<",font=font_button,relief="ridge",bg="#80bfff",borderwidth=1,width=8,height=3,command=backspace)

#Placing the buttons in the frames
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
plus.grid(row=0,column=3)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
minus.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
multiply.grid(row=2,column=3)

button0.grid(row=3,column=0)
decimal.grid(row=3,column=1)
clear.grid(row=3,column=2)
divide.grid(row=3,column=3)

equal.grid(row=4,column=0,columnspan=3,sticky="nsew")
backspace.grid(row=4,column=3)

#Window mainevent loop
window.mainloop()




















