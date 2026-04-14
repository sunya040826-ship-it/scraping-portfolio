# スクレイピングポートフォリオ

PythonによるWebスクレイピングのサンプル集です。

## スキル
- requests + BeautifulSoup（静的サイト）
- Playwright（JavaScript対応サイト）
- pandas（データ整形・CSV出力）

## サンプル一覧

### 1. news_scraper.py
- Yahoo!ニュースのタイトルとURLを収集
- requests + BeautifulSoup4を使用
- CSV形式で出力

### 2. playwright_scraper.py
- JavaScript対応サイトのスクレイピング
- Playwrightを使用
- CSV形式で出力

## 使い方

```bash
# ライブラリインストール
pip install -r requirements.txt

# 静的サイト版
python news_scraper.py

# JavaScript対応版
python playwright_scraper.py
```

## 対応可能な案件
- ECサイトの価格・在庫収集
- 求人・不動産情報の収集
- 競合他社サイトの定期監視
- データの自動収集・CSV/Excel出力