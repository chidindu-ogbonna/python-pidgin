# Product Requirement Document (PRD)

## Project: Python Pidgin (v1.0.0)

**Author:** Language Creator & AI Collaborator
**Status:** Draft
**Target Architecture:** Python 3.x Superset Transpiler

## 1. Executive Summary & Core Intent

**Python Pidgin** is an open-source, culturally expressive programming language built as a strict superset of Python. It replaces traditional Python keywords with intuitive, natural Nigerian Pidgin vocabulary (yarn, na, check) while maintaining 100% compatibility with the underlying Python runtime environment.
By prioritizing Python’s native indentation, code styling, and comment structures, Python Pidgin avoids the overhead of foreign syntactic structures (like curly braces), ensuring that learning and writing Python Pidgin feels completely seamless to anyone familiar with Python ecosystems.

## 2. Product Objectives & User Persona

* **Accessibility & Inclusion:** To lower the barrier of entry for local developers by providing a syntax rooted in their everyday cultural vocabulary.
* **Zero-Overhead Integration:** To allow Python Pidgin to run on any machine containing a standard Python interpreter without requiring native binary compilers.
* **User Persona:** Nigerian developers, CS students, or hobbyists looking for an expressive, engaging, and culturally resonant dialect to write scripts, teach programming concepts, or build projects.

## 3. Functional Requirements & Syntax Mapping

Python Pidgin must preserve all native Python behaviors, types, and logic structures. It simply layers an emotional, idiomatic syntax map on top.

### 3.1 Syntax Dictionary (MVP Core)

| Python Pidgin Keyword | Python Equivalent | Purpose / Behavior |
|---|---|---|
| # ... | # ... | Retains native Python comment style. |
| na | *(Omitted)* | Optional declarative indicator for readability (na salary = 50000). |
| check | if | Opens a conditional branch evaluating a Boolean expression. |
| unless | elif | Secondary conditional logic branch. |
| otherwise | else | Fallback execution branch. |
| small pass | < | Less-than comparison operator. |
| big pass | > | Greater-than comparison operator. |
| yarn | print | Native standard output function. |
| gist | def | Function/Method definition keyword. |
| give_am | return | Statement to pass data out of a function block. |
| as_far_say | while | Indefinite execution loop. |
| per_person | for | Definite iteration loop. |
| inside | in | Membership checking operator / structural loop iterator. |
| real_talk | True | Boolean True. |
| lie | False | Boolean False. |

## 4. Technical Architecture & Constraints

```
[ Python Pidgin Source File (.pg) ]
            │
            ▼
┌───────────────────────────┐
│     Python Pidgin Transpiler      │
│  (Token-Level Engine)     │
└───────────┬───────────────┘
            │
            ▼
[ Valid Python Code (.py) ]
            │
            ▼
┌───────────────────────────┐
│ Standard CPython Runtime  │
└───────────────────────────┘

```

### 4.1 Token-Based Transformation Engine

* The transpiler **must not** rely on simple string.replace() functions.
* It must leverage Python’s native tokenize compiler library to split the text down into programmatic elements.
* **Constraint:** Keywords must only be transformed if their token type is identified as NAME. Text appearing within string literals (e.g., yarn("This expression uses na and check safely")) or within comments must remain completely unaltered.

### 4.2 Interoperability

* Python Pidgin files must use the extension .pg.
* Standard Python code written inside a .pg file must execute correctly, ensuring full backward/superset compatibility.

## 5. User Workflow & CLI Requirements

The developer experience interacts primarily via a Command Line Interface (CLI) application wrapper named python-pidgin.py.

### 5.1 CLI Executable Command

The user runs a script by feeding it directly to the Python Pidgin interpreter:

```bash
python python-pidgin.py my_script.pg

```

### 5.2 Target Syntax Experience

An ideal Python Pidgin program must structuralize identically to this footprint:

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

## 6. Future Scope & Enhancements (v2.0+)

* **Package Management (abeg syntax):** Introducing a robust wrapper around pip to allow dependency inclusions via custom syntax (abeg request from internet).
* **Custom Exception Pipeline:** Remapping Python’s tracking outputs (try / except) into native idioms (sub / if_yawa_dey) for localized error tracking and debugging stack traces.
