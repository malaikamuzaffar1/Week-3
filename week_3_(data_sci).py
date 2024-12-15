# -*- coding: utf-8 -*-
"""Week 3 (Data Sci)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u_f84pj3X2ihsLeRD-zFpWnnordIQExQ
"""

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
!pip install selenium
!pip install scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import scrapy
import csv
import json
import time

# --- a. Requests with BeautifulSoup ---
# Function to scrape data using BeautifulSoup
def scrape_with_bs4(url):
    response = requests.get('http://quotes.toscrape.com')
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data (adjust the tag and class based on the site structure)
    data = []
    for item in soup.find_all('h2'):
        data.append(item.text.strip())

    # Save to CSV
    with open("data_bs4.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Heading"])
        for row in data:
            writer.writerow([row])

    print("Data scraped and saved using BeautifulSoup.")

# --- b. Scrapy Framework ---
# Spider class for Scrapy
class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://example.com"]

    def parse(self, response):
        data = response.css('h2::text').getall()
        for heading in data:
            yield {"Heading": heading}

# To run the Scrapy spider, save this code as 'example_spider.py' and execute:
# scrapy crawl example -o data_scrapy.json

# --- c. Selenium for Dynamic Content ---
# Function to scrape data using Selenium
def scrape_with_selenium(url):
  def scrape_with_selenium(url):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set the path to the chromedriver executable
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()  # Ensure the WebDriver is properly installed
    driver.get(url)

    # Wait for content to load
    time.sleep(5)

   # Extract data
    try:
        main_heading = driver.find_element(By.TAG_NAME, "h1").text
        paragraphs = [p.text for p in driver.find_elements(By.TAG_NAME, "p")]

        data = {
            "main_heading": main_heading,
            "paragraphs": paragraphs
        }

    except Exception as e:
        print(f"Error during data extraction: {e}")
        data = {}  # Return empty dictionary if extraction fails

    # Save to JSON
    with open("data_selenium.json", "w") as f:
        json.dump(data, f, indent=4)  # Use indent for better readability

    driver.quit()
    print("Data scraped and saved using Selenium.")

    # Display extracted data
    print("\n--- Extracted Data ---")
    print(json.dumps(data, indent=4))  # Use json.dumps for pretty printing
     # Display first five rows of paragraph data
    print("\n--- First Five Rows of Paragraph Data ---")
    for i, paragraph in enumerate(data.get("paragraphs", [])[:5]):
        print(f"{i + 1}: {paragraph}")

# --- Main Execution ---
if __name__ == "__main__":
    # URL to scrape
    target_url = "https://example.com"

    # Run BeautifulSoup scraper
    scrape_with_bs4(target_url)

    # Note: Scrapy requires a separate command-line execution to run the spider.

    # Run Selenium scraper
    scrape_with_selenium(target_url)