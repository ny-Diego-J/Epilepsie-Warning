import time
import keyboard
import mouse
import pyautogui

keyboard.press_and_release("win")
time.sleep(0.1)
keyboard.write("paint")
time.sleep(0.1)
keyboard.press_and_release("enter")
time.sleep(1)
keyboard.press_and_release("ctrl+e")
time.sleep(0.5)
keyboard.write("800")
time.sleep(0.1)
keyboard.press_and_release("tab")
time.sleep(0.1)
keyboard.write("800")
time.sleep(0.1)
keyboard.press_and_release("enter")
r,g,b = 1,1,1
mouse_x = 779
mouse_y = 85
while r != 237 or g != 28 or b != 36:
    mouse.move(mouse_x , mouse_y,  absolute=True, duration=0.2)
    mouse_x = mouse_x + 25
    r,g,b = pyautogui.pixel(mouse_x, mouse_y)
    print(r,g,b)
mouse.click()
time.sleep(0.5)
mouse.move(400, 400, absolute=True, duration=0.2)

