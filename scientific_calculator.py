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
style.configure('W.TButton', font = ('sans-serif', 10,  'bold'), foreground = 'black')


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


b4 = Button(root, text = u'\u232B', command = lambda: clear(), width = 7)
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
b9 = Button(root, text = '=', command = lambda: equal(), width = 30)
b9.grid(row = 6, column = 0, columnspan = 5)

b_sqrt = Button(root, text = u'\u221A', command = lambda: sqrt_val(), width = 7)
b_sqrt.grid(row = 1, column = 4)
b_log = Button(root, text = 'log2', command = lambda: log2_val(), width = 7)
b_log.grid(row = 2, column = 4)
b_log10 = Button(root, text = 'log10', command = lambda: log10_val(), width = 7)
b_log10.grid(row = 3, column = 4)
b_rev = Button(root, text = '1/x', command = lambda: reverse(), width = 7)
b_rev.grid(row = 4, column = 4)

b_sin = Button(root, text = 'sin', command = lambda: sin_val(), width = 7)
b_sin.grid(row = 5, column = 0)
b_cos = Button(root, text = 'cos', command = lambda: cos_val(), width = 7)
b_cos.grid(row = 5, column = 1)
b_tan = Button(root, text = 'tan', command = lambda: tan_val(), width = 7)
b_tan.grid(row = 5, column = 2)
b_exp = Button(root, text = 'exp', command = lambda: exp_val(), width = 7)
b_exp.grid(row = 5, column = 4)

b_power = Button(root, text = '^', command = lambda: power_val(), width = 7)
b_power.grid(row = 5, column = 3)

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
    
    elif type_ == 'power':
        print("Power")
        num = screen.get('1.0', END)
        num = num.split('^')
        f_num = float(num[0])
        s_num = float(num[1])
        power = str(float(math.pow(f_num, s_num)))
        screen.configure(state = 'normal')
        screen.delete('1.0', END)
        screen.insert(END, power)

    elif type_ == 'sine':
        f = screen.get('1.4', END)
        f = f.split('\n')
        print("NUm: ", f[0])
        num = float(f[0])
        ans = str(round(math.sin(num*(math.pi/180)), 2))
        screen.configure(state = 'normal')
        screen.delete('1.0', END)
        screen.insert(END, ans)
        
    elif type_ == "cosine":
        f = screen.get('1.4', END)
        f = f.split('\n')
        print("NUm: ", f[0])
        num = float(f[0])
        ans = str(round(math.cos(num * (math.pi/180)), 2))
        screen.configure(state = 'normal')
        screen.delete('1.0', END)
        screen.insert(END, ans)
        
    elif type_ == "tan_of_x":
        f = screen.get('1.4', END)
        f = f.split('\n')
        print("NUm: ", f[0])
        num = float(f[0])
        ans = str(round(math.tan(num * (math.pi/180)), 2))
        screen.configure(state = 'normal')
        screen.delete('1.0', END)
        screen.insert(END, ans)
        
    elif type_ == 'exponent':
        f = screen.get('1.4', END)
        f = f.split('\n')
        print("NUm: ", f[0])
        num = float(f[0])
        ans = str(math.exp(num))
        screen.configure(state = 'normal')
        screen.delete('1.0', END)
        screen.insert(END, ans)

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
    num = float(f[0])
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
    num = float(f[0])
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
    num = float(f[0])
    log = str(math.log10(num))
    screen.configure(state = 'normal')
    screen.delete('1.0', END)
    screen.insert(END, log)

def reverse():
    global type_
    type_ = "reverse"
    f = screen.get('1.0', END)
    f = f.split('\n')
    print("NUm: ", f[0])
    num = float(f[0])
    rev = str(float(1)/float(num))
    screen.configure(state = 'normal')
    screen.delete('1.0', END)
    screen.insert(END, rev)
    
def sin_val():
    click('sin ')
    global type_
    type_ = "sine"

    
def cos_val():
    click('cos ')
    global type_
    type_ = "cosine"

    
def tan_val():
    click('tan ')
    global type_
    type_ = "tan_of_x"

    
def exp_val():
    click('exp ')
    global type_
    type_ = "exponent"

    
def power_val():
    click("^")
    global type_
    type_ = "power"

    
    
root.mainloop()
