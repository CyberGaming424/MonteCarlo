import keyboard as kb
import time
import random as rand

kb.wait('shift')

running = True
startTime = time.time()

while running:
    if kb.is_pressed('q'):
        running = False
    kb.write('!pray')
    kb.press_and_release('enter')
    kb.write('!dep all')
    kb.press_and_release('enter')
    kb.press_and_release('enter')
    time.sleep(rand.randrange(20, 24))
