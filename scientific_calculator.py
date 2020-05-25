from tkinter import *
from tkinter.ttk import *
import math
import re

root = Tk()
root.title("Test")
screen = Text(root, state = 'disabled', width = 40, height = 3, background = 'black', foreground = 'yellow')
screen.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

mul = '*'
add = '+'
sub = '-'
div = u'\u00F7'
count= 0

type_ = ''
eq = ''

style = Style()
style.configure('W.TButton', font = ('sans-serif', 11, 'bold'), foreground = 'blue')


b1 = Button(root, text = 1, command = lambda: click(1), width = 7)
b2 = Button(root, text = 2, command = lambda: click(2), width = 7)
b3 = Button(root, text = 3, command = lambda: click(3), width = 7)
b4 = Button(root, text = 4, command = lambda: click(4), width = 7)
b5 = Button(root, text = 5, command = lambda: click(5), width = 7)
b6 = Button(root, text = 6, command = lambda: click(6), width = 7)
b7 = Button(root, text = 7, command = lambda: click(7), width = 7)
b8 = Button(root, text = 8, command = lambda: click(8), width = 7)
b9 = Button(root, text = 9, command = lambda: click(9), width = 7)

buttons= [b1, b2, b3, b4, b5, b6, b7, b8, b9]
for row in range(3, 0, -1):
    for col in range(3):
        buttons[count].grid(row = row, column = col)
        count += 1


b4 = Button(root, text = u'\u232B', style = "W.TButton", command = clear, width = 7)
b4.grid(row = 1, column = 3)
b1 = Button(root, text = div, command = lambda: basic_val(div), width = 7)
b1.grid(row = 2, column = 3)
b3 = Button(root, text = mul, command = lambda: basic_val(mul), width = 7)
b3.grid(row = 3, column = 3)
b5 = Button(root, text = sub, command = lambda: basic_val(sub), width = 7)
b5.grid(row = 4, column = 3)
b6 = Button(root, text = add, command = lambda: basic_val(add), width = 7)
b6.grid(row = 4, column = 2)
b7 = Button(root, text = '.', command = lambda: click('.'), width = 7)
b7.grid(row = 4, column = 0)
b8 = Button(root, text = '0', command = lambda: click(0), width = 7)
b8.grid(row = 4, column = 1)
b9 = Button(root, text = '=', command = equal, width = 30)
b9.grid(row = 5, column = 0, columnspan = 5)

b_sqrt = Button(root, text = u'\u221A', command = sqrt_val, width = 7)
b_sqrt.grid(row = 1, column = 4)
b_log = Button(root, text = 'log2', command = log2_val, width = 7)
b_log.grid(row = 2, column = 4)
b_log10 = Button(root, text = 'log10', command = log10_val, width = 7)
b_log10.grid(row = 3, column = 4)

def click(val):
    screen.configure(state = 'normal')
    screen.insert(END, val)
    screen.configure(state = 'disabled')

def basic_val(val):
    click(val)
    f_num = screen.get('1.0', END)
    f_num = f_num.split('+')
    f_num = f_num[0]
    print("F_num: ", f_num)
    global type_
    type_ = 'basic'
    
def equal():
    if type_ == 'basic':
        print("Inside equal")
        s_num = screen.get('1.0', END)
        s_num = re.sub(u"\u00F7", '/', s_num)
        global eq
        eq = str(s_num)
        print(eq)
        add = str(eval(eq))
        print("Add: ", add)
        screen.configure(state = 'normal')
        screen.delete('1.0', END)
        screen.insert(END, add)
        
    else:
        screen.delete('1.0', END)
        
def clear():
    screen.configure(state = 'normal')
    screen.delete('1.0', END)
    
def sqrt_val():
    #click(u'\u221A')
    global type_
    type_ = "sqrt_"
    f = screen.get('1.0', END)
    f = f.split('\n')
    print("NUm: ", f[0])
    num = int(f[0])
    sqrt = str(math.sqrt(num))
    screen.configure(state = 'normal')
    screen.delete('1.0', END)
    screen.insert(END, sqrt)
    
def log2_val():
    #click(u'\u221A')
    global type_
    type_ = "log_base_2"
    f = screen.get('1.0', END)
    f = f.split('\n')
    print("NUm: ", f[0])
    num = int(f[0])
    log = str(math.log2(num))
    screen.configure(state = 'normal')
    screen.delete('1.0', END)
    screen.insert(END, log)
    
def log10_val():
    #click(u'\u221A')
    global type_
    type_ = "log_base_2"
    f = screen.get('1.0', END)
    f = f.split('\n')
    print("NUm: ", f[0])
    num = int(f[0])
    log = str(math.log10(num))
    screen.configure(state = 'normal')
    screen.delete('1.0', END)
    screen.insert(END, log)

    
root.mainloop()
