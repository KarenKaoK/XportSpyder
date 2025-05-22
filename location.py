import time
import pyautogui

print("請把滑鼠移動到你要記下的位置，3 秒後開始記錄...")

time.sleep(3)

while True:
    x, y = pyautogui.position()
    print(f"目前滑鼠座標：({x}, {y})", end="\r")  # \r 讓輸出一直在同一行
    time.sleep(0.1)
