import tkinter as tk

calculation = ""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def back_space():
        global calculation
        calculation = calculation[:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0,calculation)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x390")
root.configure(bg="light blue")
text_result = tk.Text(root, height=3, width=20, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1= tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 20))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 20))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 20))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 20))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 20))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 20))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 20))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 20))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 20))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 20))
btn_0.grid(row=5, column=2)


btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 20))
btn_dot.grid(row=6, column=1)
btn_dot.configure(bg="light blue")

btn_openBracket = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 20))
btn_openBracket.grid(row=5, column=1)
btn_openBracket.configure(bg="light blue")

btn_closeBracket = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 20))
btn_closeBracket.grid(row=5, column=3)
btn_closeBracket.configure(bg="light blue")

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 20))
btn_plus.grid(row=2, column=4)
btn_plus.configure(bg="light blue")

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 20))
btn_minus.grid(row=3, column=4)
btn_minus.configure(bg="light blue")

btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 20))
btn_mul.grid(row=4, column=4)
btn_mul.configure(bg="light blue")

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 20))
btn_div.grid(row=5, column=4)
btn_div.configure(bg="light blue")

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 20))
btn_equals.grid(row=6, column=4)
btn_equals.configure(bg="silver")

btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 20))
btn_clear.grid(row=6, column=2)
btn_clear.configure(bg="light pink")

btn_backspace = tk.Button(root, text="DEL", command=back_space, width=5, font=("Arial", 20))
btn_backspace.grid(row=6, column=3)
btn_backspace.configure(bg="light pink")

root.mainloop()