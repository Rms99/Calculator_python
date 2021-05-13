from tkinter import*
import math

root = Tk()
root.title("Calculator (Python)")
root.geometry("416x550+500+40")

calc = Frame(root, bd=20, pady=5, bg='grey', relief=RIDGE)
calc.grid()


class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(selfselfself, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def Clear_all(self):
        self.Clear_Entry()
        self.total = 0

    def deleteBs(self):
        numLen = len(txtDisplay.get())
        txtDisplay.delete(numLen - 1, 'end')
        if numLen == 1:
            txtDisplay.insert(0, "0")

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squareroot(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)


added_value = Calc()

txtDisplay = Entry(calc, font=('arial', 16, 'bold'), bd=20, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "123456789"
i = 0
btn = []

for j in range(3, 6):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = numberpad[i]:added_value.numberEnter(x)
        i += 1

# Row1 --------------------------------------------------------------------------------------------------------
btnDelete = Button(calc, width=6, height=2, text="DEL.", font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.deleteBs).grid(row=1, column=0,  pady=1)
btnClear = Button(calc, width=6, height=2, text="C", font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=added_value.Clear_Entry).grid(row=1, column=1,  pady=1)
btnClearAll = Button(calc, width=6, height=2, text="CE.", font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.Clear_all).grid(row=1, column=2,  pady=1)
btnPM = Button(calc, width=6, height=2, text=chr(177), font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.mathsPM).grid(row=1, column=3,  pady=1)

# Row2 --------------------------------------------------------------------------------------------------------
btnSq = Button(calc, width=6, height=2, text="Sqrt.", font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.squareroot).grid(row=2, column=0,  pady=1)
btnSin = Button(calc, width=6, height=2, text="Sin", font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.sin).grid(row=2, column=1,  pady=1)
btnCos = Button(calc, width=6, height=2, text="Cos.", font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.cos).grid(row=2, column=2,  pady=1)
btnTan = Button(calc, width=6, height=2, text="Tan.", font=('arial', 16, 'bold'), bd=4, bg="white"
                   ,command=added_value.tan).grid(row=2, column=3,  pady=1)

# Column3 --------------------------------------------------------------------------------------------------------
btnAdd = Button(calc, width=6, height=2, text="+", font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=lambda: added_value.operation("add")).grid(row=3, column=3,  pady=1)
btnSub = Button(calc, width=6, height=2, text="-", font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=lambda: added_value.operation("sub")).grid(row=4, column=3,  pady=1)
btnMult = Button(calc, width=6, height=2, text="x", font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=lambda: added_value.operation("multi")).grid(row=5, column=3,  pady=1)
btnDiv = Button(calc, width=6, height=2, text=chr(247), font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=lambda: added_value.operation("divide")).grid(row=6, column=3,  pady=1)

# Row6 --------------------------------------------------------------------------------------------------------
btnZero = Button(calc, width=6, height=2, text="0", font=('arial', 16, 'bold'), bd=4,
                   command=lambda: added_value.numberEnter("0")).grid(row=6, column=1,  pady=1)
btnDot = Button(calc, width=6, height=2, text=".", font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=lambda: added_value.numberEnter(".")).grid(row=6, column=0,  pady=1)
btnEquals = Button(calc, width=6, height=2, text="=", font=('arial', 16, 'bold'), bd=4, bg="white",
                   command=added_value.sum_of_total).grid(row=6, column=2,  pady=1)


root.mainloop()


