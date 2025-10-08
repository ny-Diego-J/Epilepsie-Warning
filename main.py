import time
import keyboard
import mouse
import pyautogui

keyboard.press_and_release("win")
time.sleep(0.5)
keyboard.write("chrome",0.01)
time.sleep(2)
keyboard.press_and_release("right")
time.sleep(0.5)
keyboard.press_and_release("down")
time.sleep(0.5)
keyboard.press_and_release("down")
time.sleep(1)
keyboard.press_and_release("enter")
time.sleep(3)

keyboard.write("https://youtube.com/watch?v=dQw4w9WgXcQ",0.01)
keyboard.press_and_release("enter")
time.sleep(5)
mouse.move(918, 964)
mouse.click("left")

time.sleep(3)
keyboard.press_and_release("f")

var = 0
let = 1
tmp = 0
while True:
    mouse.move(1100, 1200)
    r,g,b = pyautogui.pixel(27, 1148)
    if r == 255 and g == 0 and b == 51:
        var = 1
        print("red")
    if var == 1:
        mouse.press("left")
    let += 1
    print(let)
    if let == 10000:
        break
    
mouse.release("left")