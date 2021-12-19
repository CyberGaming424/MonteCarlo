from time import sleep
import keyboard as kb
import pyautogui as clicker

kb.wait('shift')

running = True

while running:
    #clicker.click(400,600, 200)
    clicker.click(1208,504, 10)
    sleep(0.5)
    if kb.is_pressed("l"):
        running = False