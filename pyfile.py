import pyautogui
import keyboard
import pyperclip
import time

f = open('codes.txt', 'r')
arrOfCodes = f.read().split('\n')

while True:
    if keyboard.is_pressed("backspace"):
        for codes in arrOfCodes:
            pyperclip.copy(codes)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(8)
            pyautogui.press('z')
            time.sleep(2)
            pyautogui.doubleClick()
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press("backspace")
        break

print('completed.')

