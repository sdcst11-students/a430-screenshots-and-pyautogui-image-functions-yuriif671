import pyautogui as py
import keyboard

def main():
    py.alert("Click 'Cookie' to activate CoockieClickerAuto", "CookieClickerAuto", "Cookie")
    keyboard.press_and_release('Alt + Tab')

    while True:
        try:
            py.moveTo('assets/bigcookie.png')
            for i in range(150):
                py.click()
            py.moveTo('assets/cursor.png')
            py.click()
            print("clicked the cursor")
        except Exception as e:
            print("error")

if __name__ == "__main__":
    main()