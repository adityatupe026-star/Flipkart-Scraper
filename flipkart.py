from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import random
import os


# 🔹 Force a desktop UA
def flipkart(query, max_pages=1, max_retries=3):
    retries = 1
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    print("🕶 Using User-Agent:", user_agent)

    while retries <= max_retries:
        # Chrome setup
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument(f"user-agent={user_agent}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--window-position=-10000,0")

        driver = webdriver.Chrome(options=options)

        products_data = []
        url = f"https://www.flipkart.com/search?q={query}"
        driver.get(url)

        # Close popup if visible
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='✕']"))
            ).click()
            print("✅ Closed login popup")
        except:
            print("ℹ️ No login popup detected")

        for page in range(max_pages):
            # Scroll to load more results
            for _ in range(3):
                driver.execute_script("window.scrollBy(0, 2000)")
                time.sleep(random.uniform(1, 2))

            # Wait for product blocks to appear
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-id]"))
                )
            except:
                print("⚠️ Could not find product containers. Dumping HTML for debug:")
                with open("debug_flipkart.html", "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
                break

            products = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")
            print(f"🧾 Page {page+1}: Found {len(products)} product cards")

            for div in products:
                try:
                    title = div.find_element(By.CSS_SELECTOR, "div.KzDlHZ").text
                    price = div.find_element(By.CSS_SELECTOR, "div.Nx9bqj").text
                    rating = div.find_element(By.CSS_SELECTOR, "div.XQDdHH").text
                    link = div.find_element(By.CSS_SELECTOR, "a.CGtC98").get_attribute("href")

                    products_data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Link": link
                    })
                    time.sleep(random.uniform(0.5, 1.5))

                except:
                    print("⚠️ Error extracting data for a product. Skipping.")
                    continue

            # Move to next page
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                )
                next_button.click()
                print(f"➡️ Moving to page {page + 2}")
                time.sleep(3)
            except:
                print("🚫 No more pages to navigate.")
                break

        # Save data
        output_folder = "data"
        os.makedirs(output_folder, exist_ok=True)

        output_filename = f"{query}_flipkart.csv"
        csv_path = os.path.join(output_folder, output_filename)

        df = pd.DataFrame(products_data)
        df.to_csv(csv_path, index=False, encoding="utf-8")

        print(f"\n📊 Successfully saved {len(products_data)} products to {output_filename}")
        driver.quit()

        if products_data:
            break
        else:
            print(f"🔄 Retry {retries}/{max_retries}...\n")
            time.sleep(2)
            retries += 1

if __name__== "__main__":
    query = input("Enter the product you want to search: ")
    flipkart(query, max_pages=2)

# flipkart("laptop", max_pages=2)
