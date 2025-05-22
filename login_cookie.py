import asyncio
import json
from pyppeteer import launch
from pyppeteer_stealth import stealth

LOGIN_URL = "https://xs.teamxports.com/xs03.aspx?module=login_page&files=login&PT=1"
CREDENTIALS_PATH = "credentials.json"
COOKIE_OUTPUT_PATH = "cookies_teamxports.json"

async def main():
    with open(CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        creds = json.load(f)
    username = creds["username"]
    password = creds["password"]

    browser = await launch({
        "headless": False,
        "args": [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-blink-features=AutomationControlled",
        ],
        "defaultViewport": None,
    })

    page = await browser.newPage()
    await stealth(page)

    # 🔔 自動關閉原生 alert
    page.on("dialog", lambda dialog: asyncio.ensure_future(handle_dialog(dialog)))

    print("⚡ 打開登入頁面...")
    await page.goto(LOGIN_URL, {'waitUntil': 'domcontentloaded'})

    # 嘗試關閉 SweetAlert2 彈窗
    try:
        print("🔎 嘗試點擊 SweetAlert2 OK 按鈕...")
        await asyncio.sleep(1.5)
        await page.evaluate("""() => {
            const btn = document.querySelector('.swal2-confirm');
            if (btn) btn.click();
        }""")
    except Exception as e:
        print("⚠️ SweetAlert2 未偵測到：", e)

    # 等待 Turnstile 通過驗證（Cloudflare）
    print("🔐 等待 Turnstile 驗證處理...")
    await asyncio.sleep(8)

    print("📝 填入帳密...")
    await page.type("#ContentPlaceHolder1_loginid", username)
    await page.type("#loginpw", password)

    print("🚀 點擊登入按鈕...")
    await page.click("#login_but")

    await asyncio.sleep(5)

    cookies = await page.cookies()
    cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}
    with open(COOKIE_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(cookie_dict, f, indent=2, ensure_ascii=False)

    print(f"✅ Cookie 已儲存為 {COOKIE_OUTPUT_PATH}")
    await browser.close()

async def handle_dialog(dialog):
    print(f"🛑 原生 alert 偵測到：{dialog.message}")
    await asyncio.sleep(0.5)
    await dialog.accept()
    print("✅ 已自動關閉原生 alert")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
