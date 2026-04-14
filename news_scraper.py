import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_yahoo_news():
    url = "https://news.yahoo.co.jp/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    
    # ニュースタイトルを取得
    articles = soup.select("a")
    
    news_list = []
    for a in articles:
        title = a.get_text(strip=True)
        link = a.get("href", "")
        if title and "news.yahoo.co.jp/articles" in link:
            news_list.append({"タイトル": title, "URL": link})
    
    # 重複削除
    df = pd.DataFrame(news_list).drop_duplicates()
    
    # CSV保存
    filename = f"yahoo_news_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"✅ {len(df)}件取得 → {filename} に保存しました")

if __name__ == "__main__":
    scrape_yahoo_news()