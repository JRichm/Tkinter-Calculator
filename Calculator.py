import tkinter as tk

class Calculator:
    def __init__(self):

        # tkinter window properties
        self.root = tk.Tk()
        self.root.geometry("333x375")
        self.root.title("Calculator")

        # calculator class variables
        self.entry_num = None
        self.memory_num = None
        self.operator = None

        # tkinter elements
        self.num_display = tk.Entry(self.root, font=('Cascadia Code bold', 24), justify='right')
        self.num_display.pack(pady=10, padx=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)
        self.button_frame.columnconfigure(3, weight=1)
        self.button_frame.columnconfigure(4, weight=1)

        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.rowconfigure(1, weight=1)
        self.button_frame.rowconfigure(2, weight=1)
        self.button_frame.rowconfigure(3, weight=1)
        self.button_frame.rowconfigure(4, weight=1)

        # 0-9 buttons
        btn0 = tk.Button(self.button_frame, text='0', font=('Cascadia Code bold', 18), command=lambda : self.type_number(0))
        btn0.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)

        btn1 = tk.Button(self.button_frame, text='1', font=('Cascadia Code bold', 18), command=lambda : self.type_number(1))
        btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

        btn2 = tk.Button(self.button_frame, text='2', font=('Cascadia Code bold', 18), command=lambda : self.type_number(2))
        btn2.grid(row=3, column=1, sticky=tk.W+tk.E)

        btn3 = tk.Button(self.button_frame, text='3', font=('Cascadia Code bold', 18), command=lambda : self.type_number(3))
        btn3.grid(row=3, column=2, sticky=tk.W+tk.E)

        btn4 = tk.Button(self.button_frame, text='4', font=('Cascadia Code bold', 18), command=lambda : self.type_number(4))
        btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

        btn5 = tk.Button(self.button_frame, text='5', font=('Cascadia Code bold', 18), command=lambda : self.type_number(5))
        btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

        btn6 = tk.Button(self.button_frame, text='6', font=('Cascadia Code bold', 18), command=lambda : self.type_number(6))
        btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

        btn7 = tk.Button(self.button_frame, text='7', font=('Cascadia Code bold', 18), command=lambda : self.type_number(7))
        btn7.grid(row=1, column=0, sticky=tk.W+tk.E)

        btn8 = tk.Button(self.button_frame, text='8', font=('Cascadia Code bold', 18), command=lambda : self.type_number(8))
        btn8.grid(row=1, column=1, sticky=tk.W+tk.E)

        btn9 = tk.Button(self.button_frame, text='9', font=('Cascadia Code bold', 18), command=lambda : self.type_number(9))
        btn9.grid(row=1, column=2, sticky=tk.W+tk.E)

        # operator buttons
        add_btn = tk.Button(self.button_frame, text='+', font=('Cascadia Code bold', 18), command=lambda : self.set_operator('add'))
        add_btn.grid(row=4, column=3, sticky=tk.W+tk.E)

        sub_btn = tk.Button(self.button_frame, text='-', font=('Cascadia Code bold', 18), command=lambda : self.set_operator('sub'))
        sub_btn.grid(row=3, column=3, sticky=tk.W+tk.E)

        mul_btn = tk.Button(self.button_frame, text='*', font=('Cascadia Code bold', 18), command=lambda : self.set_operator('mul'))
        mul_btn.grid(row=2, column=3, sticky=tk.W+tk.E)

        div_btn = tk.Button(self.button_frame, text='/', font=('Cascadia Code bold', 18), command=lambda : self.set_operator('div'))
        div_btn.grid(row=1, column=3, sticky=tk.W+tk.E)

        # other buttons
        decimal_btn = tk.Button(self.button_frame, text='.', font=('Cascadia Code bold', 18), command=lambda : self.type_number('.'))
        decimal_btn.grid(row=4, column=2, sticky=tk.W+tk.E)

        backspace_btn = tk.Button(self.button_frame, text='◄', font=('Cascadia Code bold', 18), command=self.drop_last_digit)
        backspace_btn.grid(row=0, column=0, sticky=tk.W+tk.E)

        return_btn = tk.Button(self.button_frame, text='=', font=('Cascadia Code bold', 18), command=self.return_result)
        return_btn.grid(row=3, column=4, rowspan=2, sticky=tk.W+tk.E+tk.S+tk.N)

        clear_mem_btn = tk.Button(self.button_frame, text='C', font=('Cascadia Code bold', 18), command=self.clear_memory)
        clear_mem_btn.grid(row=0, column=2, sticky=tk.W+tk.E)

        clear_entry_btn = tk.Button(self.button_frame, text='CE', font=('Cascadia Code bold', 18), command=self.clear_entry)
        clear_entry_btn.grid(row=0, column=1, sticky=tk.W+tk.E)

        switch_negative_btn = tk.Button(self.button_frame, text='+/-', font=('Cascadia Code bold', 18), command=self.switch_negative)
        switch_negative_btn.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.button_frame.pack(fill='x')
        self.root.mainloop()


    # calculator functions
    def type_number(self, num):

        new_number = float(str(self.num_display.get()) + str(num))
        self.num_display.delete(0, tk.END)

        if new_number.is_integer():
            new_number = int(new_number)

        self.num_display.insert(0, new_number)

        self.entry_num = new_number
        print("\nNew Number\n", "\tentry num: ", self.entry_num, "\n\tmemory num: ", self.memory_num)


    def clear_entry(self):
        self.num_display.delete(0, tk.END)
        print("\nCleared Entry\n", "\tentry num: ", self.entry_num, "\n\tmemory num: ", self.memory_num)


    def clear_memory(self):
        self.clear_entry()
        self.memory_num = None
        print("\nCleared Memory\n", "\tentry num: ", self.entry_num, "\n\tmemory num: ", self.memory_num)


    def set_operator(self, operator):
        self.memory_num = self.entry_num
        self.clear_entry()
        self.entry_num = None
        self.operator = operator
        print(f'\nSet Operator ({operator})\n', "\tentry num: ", self.entry_num, "\n\tmemory num: ", self.memory_num)


    def switch_negative(self):
        self.clear_entry()
        self.entry_num = -float(self.entry_num)
        if self.entry_num is not None:
            if self.entry_num.is_integer():
                self.entry_num = int(self.entry_num)

        self.type_number(self.entry_num)
        print("\nSwitched Sign\n", "\tentry num: ", self.entry_num, "\n\tmemory num: ", self.memory_num)


    def drop_last_digit(self):
        if self.entry_num is not None:
            num_str = str(self.entry_num)
            num_str = num_str[:-1]

            num_float = float(num_str)
            if num_float.is_integer():
                self.clear_entry()
                self.type_number(int(num_float))
            else:
                self.clear_entry()
                self.type_number(num_float)


    def return_result(self):
        if self.memory_num:
            if not self.operator:
                result = self.entry_num
            elif self.operator == 'add':
                if (self.memory_num == 9 and self.entry_num == 10):
                    result = 21
                else:
                    result = self.memory_num + self.entry_num
            elif self.operator == 'sub':
                result = self.memory_num - self.entry_num
            elif self.operator == 'mul':
                result = self.memory_num * self.entry_num
            elif self.operator == 'div':
                if self.entry_num == 0:
                    self.type_number("DIV BY ZERO ERROR")
                else:
                    result = self.memory_num / self.entry_num

            if result is not None:
                if float(result).is_integer():
                    result = int(result)

            self.clear_entry()
            self.type_number(result)
            self.memory_num = None

Calculator()