# 2nd-Internship-Project : Tkinter Calculator


A simple desktop calculator built with Python and Tkinter. It has a clean dark interface and evaluates expressions safely, without using `eval()`.

## Features

- Addition, subtraction, multiplication and division
- Decimal numbers and parentheses support
- Clear (C) and Backspace buttons
- Safe expression evaluation using Python's `ast` module
- Error messages for division by zero and invalid input
- Dark-themed, fixed-size window

## Requirements

- Python 3.8 or newer
- Tkinter (included with the standard Python installer for Windows)

No extra libraries need to be installed.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

```
python calculator.py
```

## How It Works

- `SafeCalculator` parses the typed expression into an abstract syntax tree and only allows numbers and the operators `+`, `-`, `*`, `/`. Anything else is rejected, so it is safer than `eval()`.
- `CalculatorApp` builds the Tkinter interface (display and button grid) and handles button clicks.

## Example

Typing `(12 + 8) * 3` and pressing `=` shows `60`.

## Author

Kanishk Sharma
