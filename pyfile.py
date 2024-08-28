import pyautogui
import keyboard

f = open('codes.txt', 'r')
arrOfCodes = f.read().split('\n')

for codes in arrOfCodes:
    while True:
        if keyboard.is_pressed('backspace'):
            pyautogui.typewrite(codes + '\n')
            break

print('completed.')