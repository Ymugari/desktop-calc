import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("280x420+300+250")
        self.master.minsize(280, 420)
        self.master.maxsize(700, 800)
        self.logo = tk.PhotoImage(file='calc_logo.png')
        self.master.iconphoto(False, self.logo)
        self.master.configure(bg='#000000')
        self.input_field = tk.Entry(self.master, highlightthickness=0, font=('Lucida Sans Unicode', 14, 'bold'),
                                    justify='right', bg='#000000', fg='#FFFFFF')
        self.input_field.grid(row=0, column=0, columnspan=4, stick='wesn')
        self.input_field.insert(0, '0')
        self.button_1 = tk.Button(self.master, text="1", command=lambda: self.add_digit(1),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)

        self.button_2 = tk.Button(self.master, text="2", command=lambda: self.add_digit(2),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_3 = tk.Button(self.master, text="3", command=lambda: self.add_digit(3),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_4 = tk.Button(self.master, text="4", command=lambda: self.add_digit(4),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_5 = tk.Button(self.master, text="5", command=lambda: self.add_digit(5),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_6 = tk.Button(self.master, text="6", command=lambda: self.add_digit(6),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_7 = tk.Button(self.master, text="7", command=lambda: self.add_digit(7),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_8 = tk.Button(self.master, text="8", command=lambda: self.add_digit(8),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_9 = tk.Button(self.master, text="9", command=lambda: self.add_digit(9),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_0 = tk.Button(self.master, text="0", command=lambda: self.add_digit(0),
                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                  background='#696969', foreground='#FFFFFF', width=2, height=1, highlightthickness=0)
        self.button_all_clear = tk.Button(self.master, text="AC", command=self.all_clear,
                                          font=('Lucida Sans Unicode', 12, 'bold'),
                                          background='#808080', foreground='#FFFFFF', highlightthickness=0)
        self.button_clear = tk.Button(self.master, text="<--", command=self.clear,
                                      font=('Lucida Sans Unicode', 12, 'bold'),
                                      background='#808080', foreground='#FFFFFF', highlightthickness=0)
        self.button_negative = tk.Button(self.master, text="+/-", command=self.negative,
                                         font=('Lucida Sans Unicode', 12, 'bold'),
                                         background='#808080', foreground='#FFFFFF', highlightthickness=0)

        self.button_division = tk.Button(self.master, text="÷", command=self.division,
                                         font=('Lucida Sans Unicode', 12, 'bold'),
                                         background='#D2691E', foreground='#FFFFFF', width=2, height=1,
                                         highlightthickness=0)
        self.button_reciprocal_number = tk.Button(self.master, text="1/x", command=self.reciprocal_number,
                                                  font=('Lucida Sans Unicode', 12, 'bold'),
                                                  background='#808080', foreground='#FFFFFF', width=2, height=1,
                                                  highlightthickness=0)
        self.button_pow_2 = tk.Button(self.master, text='x²', command=self.pow_2,
                                      font=('Lucida Sans Unicode', 12, 'bold'),
                                      background='#808080', foreground='#FFFFFF', width=2, height=1,
                                      highlightthickness=0)
        self.button_sqrt = tk.Button(self.master, text='√', command=self.sqrt,
                                     font=('Lucida Sans Unicode', 12, 'bold'),
                                     background='#808080', foreground='#FFFFFF', width=2, height=1,
                                     highlightthickness=0)
        self.button_multiplication = tk.Button(self.master, text='×', command=self.multiplication,
                                               font=('Lucida Sans Unicode', 12, 'bold'),
                                               background='#D2691E', foreground='#FFFFFF', width=2, height=1,
                                               highlightthickness=0)
        self.button_minus = tk.Button(self.master, text='-', command=self.minus,
                                      font=('Lucida Sans Unicode', 12, 'bold'),
                                      background='#D2691E', foreground='#FFFFFF', width=2, height=1,
                                      highlightthickness=0)
        self.button_add = tk.Button(self.master, text='+', command=self.add,
                                    font=('Lucida Sans Unicode', 12, 'bold'),
                                    background='#D2691E', foreground='#FFFFFF', width=2, height=1,
                                    highlightthickness=0)
        self.button_equal = tk.Button(self.master, text='=', command=self.equal,
                                      font=('Lucida Sans Unicode', 12, 'bold'),
                                      background='#D2691E', foreground='#FFFFFF', width=2, height=1,
                                      highlightthickness=0)
        self.button_float = tk.Button(self.master, text='.', command=self.make_float,
                                      font=('Lucida Sans Unicode', 12, 'bold'),
                                      background='#696969', foreground='#FFFFFF', width=2, height=1,
                                      highlightthickness=0)

        self.button_all_clear.grid(row=1, column=0, stick='wesn')
        self.button_clear.grid(row=1, column=1, stick='wesn')
        self.button_negative.grid(row=1, column=2, stick='wesn')
        self.button_division.grid(row=1, column=3, stick='wesn')

        self.button_reciprocal_number.grid(row=2, column=0, stick='wesn')
        self.button_pow_2.grid(row=2, column=1, stick='wesn')
        self.button_sqrt.grid(row=2, column=2, stick='wesn')
        self.button_multiplication.grid(row=2, column=3, stick='wesn')

        self.button_7.grid(row=3, column=0, stick='wesn')
        self.button_8.grid(row=3, column=1, stick='wesn')
        self.button_9.grid(row=3, column=2, stick='wesn')
        self.button_minus.grid(row=3, column=3, stick='wesn')

        self.button_4.grid(row=4, column=0, stick='wesn')
        self.button_5.grid(row=4, column=1, stick='wesn')
        self.button_6.grid(row=4, column=2, stick='wesn')
        self.button_add.grid(row=4, column=3, stick='wesn')

        self.button_1.grid(row=5, column=0, stick='wesn')
        self.button_2.grid(row=5, column=1, stick='wesn')
        self.button_3.grid(row=5, column=2, stick='wesn')
        self.button_equal.grid(row=5, column=3, stick='wesn')

        self.button_0.grid(row=6, column=0, columnspan=2, stick='wesn')
        self.button_float.grid(row=6, column=2, columnspan=2, stick='wesn')

        self.master.rowconfigure(0, minsize=60)
        self.master.rowconfigure(1, minsize=60)
        self.master.rowconfigure(2, minsize=60)
        self.master.rowconfigure(3, minsize=60)
        self.master.rowconfigure(4, minsize=60)
        self.master.rowconfigure(5, minsize=60)
        self.master.rowconfigure(6, minsize=60)

        self.master.columnconfigure(0, minsize=70)
        self.master.columnconfigure(1, minsize=70)
        self.master.columnconfigure(2, minsize=70)
        self.master.columnconfigure(3, minsize=70)

        self.answer = ''
        self.f_num = ''
        self.operation = ''

    def add_digit(self, digit):
        value = self.input_field.get()
        if self.answer == value:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, str(digit))
        elif '0' in value and len(value) == 1:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, str(digit))
        elif value == '':
            self.input_field.insert(0, str(digit))
        else:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, value + str(digit))

    def clear(self):
        if self.answer == self.input_field.get():
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, '0')
        self.input_field.delete(len(self.input_field.get()) - 1, tk.END)
        if not self.input_field.get():
            self.input_field.insert(0, '0')

    def all_clear(self):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, '0')

    def negative(self):
        value = self.input_field.get()
        if value[0] != '-' and value != '0':
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, '-' + value)
        elif value[0] == '0':
            pass
        else:
            self.input_field.delete(0, 1)

    def reciprocal_number(self):
        value = self.input_field.get()
        if value != '0' and value != '':
            self.answer = f'{1 / float(value)}'
            if int(float(self.answer)) / float(self.answer) == 1.0:
                self.answer = int(float(self.answer))
        if value == '0':
            self.answer = 'ERR'
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.answer)

    def pow_2(self):
        value = self.input_field.get()
        if '.' in value:
            self.answer = f'{math.pow(float(value), 2)}'
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.answer)
        else:
            self.answer = f'{int(math.pow(int(value), 2))}'
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.answer)

    def division(self):
        first_number = self.input_field.get()
        self.operation = "division"
        self.f_num = first_number
        self.input_field.delete(0, tk.END)

    def sqrt(self):
        value = self.input_field.get()
        if int(math.sqrt(float(value))) / float(math.sqrt(float(value))) != 1.0:
            self.answer = f'{math.sqrt(float(value))}'
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.answer)
        else:
            self.answer = f'{int(math.sqrt(float(value)))}'
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.answer)

    def multiplication(self):
        first_number = self.input_field.get()
        self.operation = "multiplication"
        self.f_num = first_number
        self.input_field.delete(0, tk.END)

    def minus(self):
        first_number = self.input_field.get()
        self.operation = "minus"
        self.f_num = first_number
        self.input_field.delete(0, tk.END)

    def add(self):
        first_number = self.input_field.get()
        self.operation = "add"
        self.f_num = first_number
        self.input_field.delete(0, tk.END)

    def make_float(self):
        value = self.input_field.get()
        if '.' in value:
            pass
        else:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, value + '.')

    def equal(self):
        second_num = self.input_field.get()
        if self.operation == 'add':
            if int(float(self.f_num)) / float(self.f_num) == 1.0 and int(float(second_num)) / float(second_num) == 1.0:
                self.answer = f'{int(self.f_num) + int(second_num)}'
            else:
                self.answer = f'{float(self.f_num) + float(second_num)}'
        elif self.operation == 'minus':
            if int(float(self.f_num)) / float(self.f_num) == 1.0 and int(float(second_num)) / float(second_num) == 1.0:
                self.answer = f'{int(self.f_num) - int(second_num)}'
            else:
                self.answer = f'{float(self.f_num) - float(second_num)}'
        elif self.operation == 'multiplication':
            if int(float(self.f_num)) / float(self.f_num) == 1.0 and int(float(second_num)) / float(second_num) == 1.0:
                self.answer = f'{int(self.f_num) * int(second_num)}'
            else:
                self.answer = f'{float(self.f_num) * float(second_num)}'
        elif self.operation == 'division':
            if second_num == '0':
                self.answer = 'ERR'
            else:
                self.answer = eval(self.f_num + '/' + second_num)
                if int(float(self.answer)) / float(self.answer) == 1.0:
                    self.answer = f'{str(int(self.answer))}'
                else:
                    self.answer = f'{str(float(self.answer))}'
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.answer)


if __name__ == '__main__':
    window = tk.Tk()
    calc = Calculator(window)
    window.mainloop()