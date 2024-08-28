import pyautogui
import keyboard

f = open('codes.txt', 'r')
arrOfCodes = f.read().split('\n')

for codes in arrOfCodes:
    while True:
        if keyboard.is_pressed('page up'):
            pyautogui.typewrite(codes + '\n')
            break