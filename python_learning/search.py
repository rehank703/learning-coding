import pyautogui
import pyperclip
import time
import webbrowser


search = input("what do you want search:")
webbrowser.open("https://chatgpt.com/")
time.sleep(5)



def search_ing ( search):
    pyperclip.copy(search)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.leftClick(882, 482)
    time.sleep(0.4)
    pyautogui.leftClick(882, 482)
    time.sleep(7)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(2)
    
    pyautogui.hotkey("ctrl", "c")
    answer = pyperclip.paste()
    print(answer)

search_ing ( search)
