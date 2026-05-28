# Python Pidgin

Python Pidgin is an open-source, culturally expressive programming language built as a strict superset of Python. It replaces traditional Python keywords with intuitive, natural Nigerian Pidgin vocabulary (`yarn`, `na`, `check`) while maintaining 100% compatibility with the underlying Python runtime environment.

By prioritizing Python’s native indentation, code styling, and comment structures, Python Pidgin avoids the overhead of foreign syntactic structures, ensuring that learning and writing Python Pidgin feels completely seamless to anyone familiar with Python ecosystems.

## Installation

You can install Python Pidgin locally directly from the source directory using pip:

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
