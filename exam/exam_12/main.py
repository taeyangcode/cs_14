import tkinter as tk


class Calculator:
    def __init__(self):
        # operation step (False => 1, True => 2)
        self.step = False

        # first operation
        self.operation_1 = ""
        # second operation
        self.operation_2 = ""
        # operation
        self.operation = ""

        # window
        self.window = tk.Tk()
        self.window.title("TI-0")

        # frames
        self.output_f = tk.Frame(self.window)
        self.row_1_f = tk.Frame(self.window)
        self.row_2_f = tk.Frame(self.window)
        self.row_3_f = tk.Frame(self.window)
        self.row_4_f = tk.Frame(self.window)
        self.row_5_f = tk.Frame(self.window)

        # row 1 output variable and label
        self.output_v = tk.StringVar()
        self.output_l = tk.Label(self.output_f, textvariable=self.output_v)
        self.output_l.pack(side="top")

        # row 2 buttons
        self.b_1 = tk.Button(self.row_1_f, text="1", command=self._b_1)
        self.b_1.pack(side="left")
        self.b_2 = tk.Button(self.row_1_f, text="2", command=self._b_2)
        self.b_2.pack(side="left")
        self.b_3 = tk.Button(self.row_1_f, text="3", command=self._b_3)
        self.b_3.pack(side="left")

        # row 3 buttons
        self.b_4 = tk.Button(self.row_2_f, text="4", command=self._b_4)
        self.b_4.pack(side="left")
        self.b_5 = tk.Button(self.row_2_f, text="5", command=self._b_5)
        self.b_5.pack(side="left")
        self.b_6 = tk.Button(self.row_2_f, text="6", command=self._b_6)
        self.b_6.pack(side="left")

        # row 4 buttons
        self.b_7 = tk.Button(self.row_3_f, text="7", command=self._b_7)
        self.b_7.pack(side="left")
        self.b_8 = tk.Button(self.row_3_f, text="8", command=self._b_8)
        self.b_8.pack(side="left")
        self.b_9 = tk.Button(self.row_3_f, text="9", command=self._b_9)
        self.b_9.pack(side="left")
        self.b_0 = tk.Button(self.row_3_f, text="0", command=self._b_0)
        self.b_0.pack(side="left")

        # row 4 buttons

        # plus
        self.b_p = tk.Button(self.row_4_f, text="+", command=self._b_p)
        self.b_p.pack(side="left")
        # minus
        self.b_m = tk.Button(self.row_4_f, text="-", command=self._b_m)
        self.b_m.pack(side="left")
        # times
        self.b_t = tk.Button(self.row_4_f, text="*", command=self._b_t)
        self.b_t.pack(side="left")
        # divide
        self.b_d = tk.Button(self.row_4_f, text="/", command=self._b_d)
        self.b_d.pack(side="left")

        # row 5 buttons

        # decimal
        self.b_dot = tk.Button(self.row_5_f, text=".", command=self._b_dot)
        self.b_dot.pack(side="left")
        # neg
        self.b_n = tk.Button(self.row_5_f, text="Neg", command=self._b_n)
        self.b_n.pack(side="left")
        # enter/equals
        self.b_e = tk.Button(self.row_5_f, text="=", command=self._b_e)
        self.b_e.pack(side="left")
        # reset
        self.b_r = tk.Button(self.row_5_f, text="Reset", command=self._b_r)
        self.b_r.pack(side="left")

        # pack frames
        self.output_f.pack()
        self.row_1_f.pack()
        self.row_2_f.pack()
        self.row_3_f.pack()
        self.row_4_f.pack()
        self.row_5_f.pack()

    def _b_1(self):
        self.step_helper("1")

    def _b_2(self):
        self.step_helper("2")

    def _b_3(self):
        self.step_helper("3")

    def _b_4(self):
        self.step_helper("4")

    def _b_5(self):
        self.step_helper("5")

    def _b_6(self):
        self.step_helper("6")

    def _b_7(self):
        self.step_helper("7")

    def _b_8(self):
        self.step_helper("8")

    def _b_9(self):
        self.step_helper("9")

    def _b_0(self):
        self.step_helper("0")

    def _b_p(self):
        self.step_helper("+")

    def _b_m(self):
        self.step_helper("-")

    def _b_t(self):
        self.step_helper("*")

    def _b_d(self):
        self.step_helper("/")

    def _b_dot(self):
        self.step_helper(".")

    def _b_n(self):
        self.step_helper("n")

    def _b_e(self):
        self.step_helper("=")

    def _b_r(self):
        self.step_helper("r")

    def step_helper(self, input):
        # handle reset
        if input == "r":
            self.operation_1 = ""
            self.operation_2 = ""
            self.operation = ""
            self.step = False
            self.output_v.set("")
            return

        # handle step 1
        if self.step == False:
            self.handle_step_1(input)
            return

        # handle step 2
        if self.step == True:
            self.handle_step_2(input)
            return

    def handle_step_1(self, input):
        number_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
        operator_input = ["+", "-", "*", "/"]

        # handle input is number
        if input in number_input:
            self.operation_1 += input
            self.output_v.set(self.operation_1)
            return

        # handle Neg
        if input == "n":
            self.operation_1 = "-" + self.operation_1
            self.output_v.set(self.operation_1)
            return

        # handle operation 1
        if input in operator_input:
            self.operation = input
            self.step = True
            self.output_v.set(self.operation)
            return

    def handle_step_2(self, input):
        number_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

        # handle input is number
        if input in number_input:
            self.operation_2 += input
            self.output_v.set(self.operation_2)
            return

        # handle Neg
        if input == "n":
            self.operation_2 = "-" + self.operation_2
            self.output_v.set(self.operation_2)
            return

        # handle equals
        if input == "=":
            if self.operation == "+":
                self.output_v.set(
                    str(float(self.operation_1) + float(self.operation_2))
                )
            elif self.operation == "-":
                self.output_v.set(
                    str(float(self.operation_1) - float(self.operation_2))
                )
            elif self.operation == "*":
                self.output_v.set(
                    str(float(self.operation_1) * float(self.operation_2))
                )
            elif self.operation == "/":
                self.output_v.set(
                    str(float(self.operation_1) / float(self.operation_2))
                )
            return

    def run(self):
        tk.mainloop()


def main():
    calculator = Calculator()
    calculator.run()


main()
