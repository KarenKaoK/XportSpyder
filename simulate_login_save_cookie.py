import time
import pyautogui
import pyperclip
import webbrowser
import json
import browser_cookie3

# 讀取帳號密碼
with open("credentials.json", "r", encoding="utf-8") as f:
    creds = json.load(f)

USERNAME = creds["username"]
PASSWORD = creds["password"]

# Step 1: 開啟登入網頁
url = "https://xs.teamxports.com/xs03.aspx?module=login_page&files=login&PT=1"
webbrowser.open(url)
print("🌐 開啟登入頁...")
time.sleep(10)  # 等 Cloudflare 自動驗證與網頁載入

# Step 2: 點擊 SweetAlert2 的 OK 按鈕
pyautogui.click(x=1119, y=251)  # ❗請依你的畫面調整座標
print("✅ 點擊 SweetAlert2 OK1")
time.sleep(1)

# Step 2: 點擊 SweetAlert2 的 OK 按鈕
pyautogui.click(x=965, y=710)  # ❗請依你的畫面調整座標
print("✅ 點擊 SweetAlert2 OK2")
time.sleep(1)

# Step 3: 輸入帳號
pyautogui.click(x=1013, y=336)  # ❗帳號欄位位置
pyperclip.copy(USERNAME)
pyautogui.hotkey("command", "v")  # Mac 使用 command，Windows 改 ctrl
time.sleep(0.5)

# Step 4: 輸入密碼
pyautogui.press("tab")
pyperclip.copy(PASSWORD)
pyautogui.hotkey("command", "v")
time.sleep(0.5)

# Step 2: 點擊 SweetAlert2 的 OK 按鈕
pyautogui.click(x=949, y=482)  # ❗請依你的畫面調整座標
print("✅ 點擊 SweetAlert2 OK2")
time.sleep(1)
print("🚀 已完成登入流程")

import browser_cookie3
import json

# 擷取來自 Chrome 瀏覽器、指定網站的 cookie
cj = browser_cookie3.chrome(domain_name='teamxports.com')

# 轉為 dict 形式方便儲存
cookie_dict = {cookie.name: cookie.value for cookie in cj}

# 儲存到 json 檔案
with open("cookies_teamxports.json", "w", encoding="utf-8") as f:
    json.dump(cookie_dict, f, indent=2, ensure_ascii=False)

print("🍪 Cookie 已儲存為 cookies_teamxports.json")

