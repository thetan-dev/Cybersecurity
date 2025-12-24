# Simple Keyboard Logger (Educational)

This project is a minimal **keyboard logger** built in Python using the `keyboard` library. It listens for global key presses on your system and records them in a text file called `logs.txt` in the current directory.[web:156][web:162]

> ⚠️ **Important:** This project is for **educational use only**. Running a keylogger on systems without explicit permission can be illegal and unethical.[web:166]

---

## Features

- Captures all key presses at the OS level using the `keyboard` module.[web:156][web:168]  
- Converts special keys (such as space, enter, shift) into a human‑readable format before logging.[web:152]  
- Appends keystrokes continuously to `logs.txt` until the program is stopped.

---

## How It Works (Conceptual)

- A writer function appends text to `logs.txt` in *append* mode so existing logs are preserved.  
- A filter function:
  - Converts the `"space"` key into an actual space character.
  - Wraps multi‑character key names (like `enter`, `shift`, `ctrl`) in square brackets to distinguish them.
  - Leaves single‑character keys (letters, digits, symbols) as they are.  
- A logger callback receives key events, passes the key name through the filter, and forwards the result to the writer.  
- The script registers this callback with `keyboard.on_press(...)` and then blocks on `keyboard.wait()` so it runs until interrupted.[web:152][web:159]

---

## Requirements and Setup

- **Python** 3.x installed on your system.  
- **Dependencies:** the `keyboard` package from PyPI.

Install the required package:

pip install keyboard

text

Note: On some systems, capturing global keystrokes requires administrator or root privileges.[web:156][web:162]

---

## Running the Logger

1. Place the Python script file in a directory of your choice.  
2. Open a terminal or command prompt in that directory.  
3. Run the script with Python (for example, `python keylogger.py`).  
4. While the script is running, anything you type anywhere (terminal, browser, editor, etc.) is recorded into `logs.txt`.  
5. Press **Ctrl + C** in the terminal to stop the program gracefully.[web:158][web:161]

---

## Log Format

- Normal characters (letters, numbers, symbols) appear as themselves.  
- Spaces are logged as actual spaces.  
- Special keys (e.g., Enter, Shift, Ctrl, Backspace) appear wrapped in square brackets, for example: `[enter]`, `[shift]`, `[ctrl]`.  
- The log is a continuous stream of these tokens, making it easier to replay or analyze what was typed.[web:152]

---

## Ethical and Legal Disclaimer

This project demonstrates how low‑level keyboard event capture works in Python and should only be used:

- On machines you own or control.  
- With full, explicit consent from any other users of the device.  
- In compliance with local laws, institutional policies, and ethical guidelines.[web:166]

Using keyloggers for credential theft, spying, or unauthorized monitoring is strictly prohibited and may be punishable under cybercrime laws.