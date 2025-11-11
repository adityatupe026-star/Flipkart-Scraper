# Flipkart Product Scraper 🛒

A Python-based web scraper that extracts product details from **Flipkart** using **Selenium**.  
It captures product **titles, prices, ratings, and links** and saves the data into a CSV file.

---

## Author ✍️
- Name: Your Name
- GitHub: [yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## Features ✨
- Supports searching for any product on Flipkart.
- Scrapes multiple pages (configurable).
- Handles login popups automatically.
- Saves scraped data in CSV format.
- Built-in retries for failed scraping attempts.
- Randomized scrolling & delays to mimic human behavior.

---

## Tech Stack 🛠
- Python 3.x  
- Selenium WebDriver  
- Pandas  

---

## Installation ⚡

1. Clone the repository:
```bash
git clone <repo-url>
cd <repo-folder>
```

2. Install required Python packages:
```bash
pip install selenium pandas
```

3. Make sure **Google Chrome** and **ChromeDriver** are installed and in your system PATH.

---

## Usage 🚀

1. Run the script:
```bash
python flipkart_scraper.py
```

2. Enter the product name when prompted:
```
Enter the product you want to search: laptop
```

3. The scraper will navigate Flipkart, extract product data, and save it as a CSV inside the `data/` folder:
```
data/laptop_flipkart.csv
```

---

## Configuration ⚙
- **`max_pages`**: Number of pages to scrape (default: 1)  
- **`max_retries`**: Number of retry attempts if scraping fails (default: 3)  

Example usage inside code:
```python
flipkart("smartphone", max_pages=3, max_retries=2)
```

---

## Notes 📝
- Uses a **desktop user-agent** to avoid mobile layout issues.
- Random delays and scrolling are added to reduce the chance of being blocked.
- Popups are automatically closed if detected.
- If scraping fails, HTML is saved to `debug_flipkart.html` for troubleshooting.

---

## Future Improvements 🚀
- Scrape additional fields like **offers, stock availability**.
- Add **multi-platform support** (Amazon, Flipkart, etc.).
- Output **JSON or Excel** format.
- Add a **Telegram bot** to get results instantly.

---

## License
This project is **open-source**. Feel free to modify and use for personal or learning purposes.

