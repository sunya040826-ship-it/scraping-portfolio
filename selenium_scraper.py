from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime

def scrape_with_selenium():
    # ChromeDriverを自動インストール・起動
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # ブラウザを表示しない
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Yahoo!ニュースにアクセス
        driver.get("https://news.yahoo.co.jp/")

        # ページが読み込まれるまで待機
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )

        # リンクを取得
        elements = driver.find_elements(By.TAG_NAME, "a")

        news_list = []
        for el in elements:
            title = el.text.strip()
            link = el.get_attribute("href") or ""
            if title and "news.yahoo.co.jp/articles" in link:
                news_list.append({"タイトル": title, "URL": link})

        # 重複削除
        df = pd.DataFrame(news_list).drop_duplicates()

        # CSV保存
        filename = f"selenium_news_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"✅ {len(df)}件取得 → {filename} に保存しました")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_with_selenium()