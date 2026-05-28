# Pidgin Programming Language

**The Pidgin Programming Language** is a culturally expressive, strict superset of Python that brings the vibrant vocabulary of Nigerian Pidgin to modern software development. It empowers developers to write powerful, 100% Python-compatible code using intuitive, natural expressions (like `yarn`, `na`, `check`), bridging the gap between culture and technology so you can code exactly the way you speak.

By prioritizing Python’s native indentation, code styling, and comment structures, Python Pidgin avoids the overhead of foreign syntactic structures, ensuring that learning and writing Python Pidgin feels completely seamless to anyone familiar with Python ecosystems.

## Installation

### Prerequisites

Since the Pidgin Programming Language is built as a strict superset of Python, you must have Python installed on your system first.

- You can download and install Python from the official website: [python.org/downloads](https://www.python.org/downloads/)
- Alternatively, install it via your system's package manager (e.g., `brew install python` on macOS or `sudo apt install python3` on Ubuntu).

Verify your installation by running `python --version` or `python3 --version` in your terminal.

### Install from PyPI

Once Python is installed, you can easily install the language directly from PyPI:

```bash
pip install python-pidgin
```

### Install from Source

If you want to run from the source directory, you can install it locally using pip:

```bash
pip install -e .
```

This will make the `python-pidgin` command globally available on your machine.

## Usage

Once installed, you can run any Python Pidgin (`.pg`) script by simply passing it to the `python-pidgin` CLI:

```bash
python-pidgin my_script.pg
```

## Syntax Dictionary

Python Pidgin preserves all native Python behaviors. Here are the core keyword mappings:

| Python Pidgin Keyword | Python Equivalent | Purpose / Behavior |
|---|---|---|
| `na` | *(Omitted)* | Optional declarative indicator for readability (e.g. `na x = 5`). |
| `check` | `if` | Opens a conditional branch evaluating a Boolean expression. |
| `unless` | `elif` | Secondary conditional logic branch. |
| `otherwise` | `else` | Fallback execution branch. |
| `small pass` | `<` | Less-than comparison operator. |
| `big pass` | `>` | Greater-than comparison operator. |
| `yarn` | `print` | Native standard output function. |
| `gist` | `def` | Function/Method definition keyword. |
| `give_am` | `return` | Statement to pass data out of a function block. |
| `as_far_say` | `while` | Indefinite execution loop. |
| `per_person` | `for` | Definite iteration loop. |
| `inside` | `in` | Membership checking operator / structural loop iterator. |
| `real_talk` | `True` | Boolean True. |
| `lie` | `False` | Boolean False. |
| `try_am` | `try` | Opens a try block for exception handling. |
| `e_cast` | `except` | Catches exceptions if the try block fails. |
| `Problem` | `Exception` | Base exception class. |
| `abi` | `or` | Logical OR operator. |
| `bring_come` | `import` | Import module statement. |
| `comot` | `break` | Breaks out of the current loop. |
| `move` | `continue` | Skips to the next iteration of the loop. |
| `nothing` | `None` | Null value. |
| `level` | `class` | Class definition. |

## Example Script

```python
# Setup basic parameters
na monthly_pay = 75000
na minimum_wage = 70000

# Logic validation block
check monthly_pay small pass minimum_wage:
    yarn("God dey, things go better!")
otherwise:
    yarn("Oga, do giveaway!")
```
