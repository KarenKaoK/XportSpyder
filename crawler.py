import requests
import json
import datetime
from bs4 import BeautifulSoup
import pandas as pd

# 1. 載入 cookie
with open("cookies_teamxports.json", "r", encoding="utf-8") as f:
    cookies = json.load(f)

# 2. 準備儲存所有資料的列表
all_records = []

# 3. 從今天開始的 14 天內，每天處理 3 個分頁 D2=1,2,3
today = datetime.datetime.now()
for day_offset in range(14):
    date = (today + datetime.timedelta(days=day_offset)).strftime("%Y/%m/%d")
    for d2 in [1, 2, 3]:
        url = f"https://xs.teamxports.com/xs03.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D={date}&D2={d2}"
        response = requests.get(url, cookies=cookies)

        if response.status_code != 200:
            print(f"❌ 取得失敗：{url} 狀態碼 {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'border': '1'})
        if not table:
            print(f"⚠️ 日期 {date} 頁面 D2={d2} 找不到場地表格")
            continue

        rows = table.find_all('tr')
        current_time = ""

        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) == 4:
                time_col = cols[0].get_text(strip=True)
                if time_col:
                    current_time = time_col

                court = cols[1].get_text(strip=True)
                price = cols[2].get_text(strip=True)
                status_img = cols[3].find('img')
                status = status_img['title'] if status_img and 'title' in status_img.attrs else '未知'
                
                # 狀態解析
                if status_img:
                    # 有 title 就取 title
                    if 'title' in status_img.attrs:
                        status = status_img['title']
                    else:
                        # 依據圖片來源判斷
                        src = status_img.get('src', '')
                        if "place01" in src:
                            status = "可預約"
                        elif "place02" in src:
                            status = "已被預約"
                        else:
                            status = "未知"
                else:
                    status = "未知"

                all_records.append({
                    "日期": date,
                    "時段": current_time,
                    "場地": court,
                    "價格": price,
                    "狀態": status,
                    "分頁": d2
                })

# 4. 轉換為 DataFrame 並存為 CSV
df = pd.DataFrame(all_records)
df.to_csv("teamxports_booking_14days.csv", index=False)
print("✅ 已成功儲存為 teamxports_booking_14days.csv")
