import pyautogui
import keyboard
import pyperclip

f = open('codes.txt', 'r')
arrOfCodes = f.read().split('\n')

for codes in arrOfCodes:
    while True:
        if keyboard.is_pressed('backspace'):
            pyperclip.copy(codes)
            pyautogui.hotkey("ctrl", "v")
            break

print('completed.')
