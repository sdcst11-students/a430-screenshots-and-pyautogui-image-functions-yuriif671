import pyautogui as py

py.alert("Click 'Cookie' to activate CoockieClickerAuto", "CookieClickerAuto", "Cookie")

n = 0
y = 850
while n < 9:
    py.moveTo(1250, y, 2)
    y -= 70
    n += 1