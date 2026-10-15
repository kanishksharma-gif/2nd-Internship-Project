import ast
import operator
import tkinter as tk
from tkinter import messagebox


class SafeCalculator:
    """Evaluate basic arithmetic expressions safely."""

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression, mode="eval")
        return cls._evaluate_node(tree.body)

    @classmethod
    def _evaluate_node(cls, node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in cls.OPERATORS:
            left = cls._evaluate_node(node.left)
            right = cls._evaluate_node(node.right)
            return cls.OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in cls.OPERATORS:
            value = cls._evaluate_node(node.operand)
            return cls.OPERATORS[type(node.op)](value)

        raise ValueError("Invalid expression")


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Tkinter Calculator")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#202124")

        self.expression = tk.StringVar()
        self._build_ui()

    def _build_ui(self):
        display = tk.Entry(
            self.root,
            textvariable=self.expression,
            font=("Arial", 24),
            bg="#2b2c30",
            fg="white",
            bd=0,
            justify="right",
            insertbackground="white",
        )
        display.pack(fill="both", padx=15, pady=(20, 15), ipady=18)

        button_frame = tk.Frame(self.root, bg="#202124")
        button_frame.pack(expand=True, fill="both", padx=15, pady=10)

        buttons = [
            ["C", "Back", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "(", ")"],
        ]

        for row_index, row_values in enumerate(buttons):
            button_frame.rowconfigure(row_index, weight=1)
            for column_index, value in enumerate(row_values):
                button_frame.columnconfigure(column_index, weight=1)
                button = tk.Button(
                    button_frame,
                    text=value,
                    font=("Arial", 16, "bold"),
                    bg=self._button_color(value),
                    fg="white",
                    activebackground="#5f6368",
                    activeforeground="white",
                    bd=0,
                    command=lambda text=value: self._on_button_click(text),
                )
                button.grid(
                    row=row_index,
                    column=column_index,
                    sticky="nsew",
                    padx=5,
                    pady=5,
                )

    def _button_color(self, text):
        if text == "C":
            return "#d93025"
        if text == "=":
            return "#188038"
        if text in {"+", "-", "*", "/", "Back"}:
            return "#3c4043"
        return "#303134"

    def _on_button_click(self, text):
        current = self.expression.get()

        if text == "C":
            self.expression.set("")
            return

        if text == "Back":
            self.expression.set(current[:-1])
            return

        if text == "=":
            self._calculate_result()
            return

        self.expression.set(current + text)

    def _calculate_result(self):
        expression = self.expression.get().strip()

        if not expression:
            return

        try:
            result = SafeCalculator.evaluate(expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            self.expression.set("")
        except Exception:
            messagebox.showerror("Input Error", "Please enter a valid expression.")
            self.expression.set("")


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
