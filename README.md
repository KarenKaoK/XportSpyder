# XportSpyder

## Overview

XportSpyder is an automation crawler designed to collect badminton court availability data from the TeamXports booking platform.
It simulates human login, retrieves the next 14 days of availability data, and saves the results in a structured CSV file for analysis or alert purposes.

## Features

- 14-Day Availability Scraper
Automatically retrieves booking data for the next 14 days, including morning, afternoon, and evening time slots.
- Login Flow Automation
Simulates human login behavior and handles cookie validation to ensure session availability.
-  Structured Availability Output
Scraped data is cleaned and exported to a structured CSV file, focusing on available and reserved slots across all venues and time periods..

## Usage Steps
🔐 Login Simulation Phase

1. Use `location.py` to record mouse click coordinates (for buttons and input fields on the login page)

2. Input the recorded coordinates into the corresponding positions in `simulate_login_save_cookie.py`

3. Create a `credentials.json` file containing your login username and password

4. Run `simulate_login_save_cookie.py` to simulate login and generate the `cookies_teamxports.json` file

🕸 Data Crawling Phase

5. Run `crawler.py` to automatically fetch badminton court availability for the next 14 days and export it as `teamxports_booking_14days.csv`

## Q&A / Troubleshooting

- `browser_cookie3.BrowserCookieError: Unable to get key for cookie decryption`

    - 摘要說明： 這個錯誤表示 browser_cookie3 無法存取 Chrome 儲存的 cookie 解密金鑰，因此無法擷取 cookie。

    - 常見原因：
        - 系統權限限制
            - 在 macOS 上，Chrome 使用「鑰匙圈 (Keychain)」儲存金鑰，需使用同一個使用者登入並允許權限。
            - 在 Windows 上，Chrome 使用 DPAPI 加密，僅限同一使用者帳戶讀取。
        - 尚未登入或尚未儲存 cookie
            - 如果從未在這台電腦上登入過 TeamXports，或登入後未成功儲存 cookie，browser_cookie3 無法取得任何內容。
        - 瀏覽器版本或使用者環境問題
            - 使用訪客帳戶或瀏覽器更新後的儲存路徑變動，都可能導致擷取失敗。
    - 解決方式：
    
        - 建議方法 1：改用 Selenium 自動登入並擷取 cookie: 模擬登入後使用 driver.get_cookies() 擷取 cookie，穩定性最高
        
        - 建議方法 2：手動從 Chrome DevTools 匯出 cookie:登入後打開開發者工具 → Application → Cookies → 複製資料手動儲存為 JSON
        
