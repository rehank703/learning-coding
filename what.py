# 

import pyautogui
import pyperclip
import time
import webbrowser

# Open WhatsApp Web
webbrowser.open("https://web.whatsapp.com")
time.sleep(15)  # time to scan QR

# Contacts or group names
recipients = [
     "SY AN-A Unofficial"
]

# Message to send
message = ("I am a chatbot made by .\n"
           "Here’s what he wants to say:\n"
           "'Study for '")

def send_message(recipient):
    
    pyautogui.click(200, 200)  
    time.sleep(1)

    
    pyperclip.copy(recipient)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.5)

    
    pyautogui.press("enter")
    time.sleep(2.5)  # wait for chat to open

    
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    
    pyautogui.press("enter")
    print(f" Message sent to: {recipient}")
    time.sleep(2)

# Send to all
for r in recipients:
    send_message(r)
