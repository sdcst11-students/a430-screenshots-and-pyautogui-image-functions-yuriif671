import pyautogui as py
import keyboard
import time

def clickCookie():
    py.moveTo('assets/bigcookie.png')
    for i in range(300):
        py.click()

def purchaseBuildings():
    n = 0
    y = 850

    while n < 9:
        py.moveTo(1250, y)
        for i in range(7):
            time.sleep(0.3)
            py.click()

        y -= 70
        n += 1

def main():
    py.alert("Click 'Cookie' to activate CoockieClickerAuto", "CookieClickerAuto", "Cookie")
    
    keyboard.press_and_release('Alt + Tab')

    while True:
        try:
            clickCookie()
            purchaseBuildings()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()