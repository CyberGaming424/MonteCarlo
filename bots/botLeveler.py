import keyboard as kb
import time
import random as rand
import pyautogui as clicker


kb.wait('shift')

running = True
startTime = time.time()

while running:
    #clicker.click(400,600, 200)
    if kb.is_pressed("enter"):
        clicker.click(400,600, 10)
    elif kb.is_pressed("l"):
        running = False
