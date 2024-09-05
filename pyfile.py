import keyboard

import pyperclip
import time



def load_codes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
        return []



codes = load_codes_from_file('codes.txt')


def type_phrase():
    if codes:
        phrase = codes[0]
        for char in phrase:
            keyboard.write(char)
            time.sleep(0.05)  # Adjust the delay as needed
        codes.remove(phrase)


keyboard.add_hotkey('F12', type_phrase)

print("Press F12 to type a phrase.")
keyboard.wait('esc')
