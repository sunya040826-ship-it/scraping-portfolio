from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime

def scrape_with_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://news.yahoo.co.jp/")
        page.wait_for_load_state("networkidle")

        # リンクを取得
        links = page.query_selector_all("a")

        news_list = []
        for link in links:
            title = link.inner_text().strip()
            href = link.get_attribute("href") or ""
            if title and "news.yahoo.co.jp/articles" in href:
                news_list.append({"タイトル": title, "URL": href})

        df = pd.DataFrame(news_list).drop_duplicates()

        filename = f"playwright_news_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"✅ {len(df)}件取得 → {filename} に保存しました")

        browser.close()

if __name__ == "__main__":
    scrape_with_playwright()