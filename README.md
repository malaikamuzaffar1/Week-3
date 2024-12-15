# Week-3
Description
The code demonstrates three different web scraping approaches using BeautifulSoup, Scrapy, and Selenium to extract data from web pages. Each method targets specific scraping needs, ranging from simple static HTML pages to complex dynamic content. Below is an explanation of each section:

1. Requests with BeautifulSoup
Purpose: Extract data from static HTML web pages.
Libraries Used: requests, BeautifulSoup, and csv.
Functionality:
Sends an HTTP GET request to the specified URL using requests.
Parses the HTML response with BeautifulSoup.
Locates and extracts all <h2> tags' text (or any desired tag).
Saves the extracted data to a CSV file named data_bs4.csv.
Steps:
requests.get(url): Fetches the web page content.
soup.find_all('h2'): Finds all <h2> elements in the HTML.
csv.writer: Writes the data into a CSV file.
Example Use Case: Scraping quotes or headings from a static site like http://quotes.toscrape.com.
2. Scrapy Framework
Purpose: Crawl and scrape websites systematically, especially useful for large-scale or multi-page scraping.
Libraries Used: scrapy.
Functionality:
Defines a Scrapy spider (ExampleSpider) with a start URL.
Extracts all <h2> tags' text using response.css('h2::text').
Yields the extracted data as a dictionary, which Scrapy automatically stores.
The scraped data can be exported to formats like JSON or CSV using Scrapy commands.
Execution:
Save the spider code in a Python file (e.g., example_spider.py).
Run the spider using the command:
Copy code
scrapy crawl example -o data_scrapy.json
Example Use Case: Scraping structured data from a large site with multiple pages.
3. Selenium for Dynamic Content
Purpose: Scrape data from websites that load content dynamically using JavaScript.
Libraries Used: selenium, json, and time.
Functionality:
Initializes a headless Chrome WebDriver to interact with the webpage.
Waits for the content to load dynamically (using time.sleep()).
Extracts specific data like the main heading (<h1>) and all paragraphs (<p>).
Saves the extracted data to a JSON file (data_selenium.json).
Prints the data for verification, including the first five paragraphs.
Steps:
webdriver.Chrome(options=chrome_options): Sets up a headless Chrome browser.
driver.find_element(By.TAG_NAME, "h1"): Extracts the first <h1> element's text.
driver.find_elements(By.TAG_NAME, "p"): Extracts all <p> elements' text.
Data is saved in JSON format for better readability.
Example Use Case: Scraping dynamic content, e.g., news articles or product pages loaded via JavaScript.
4. Main Execution
The script is set up to run the BeautifulSoup and Selenium scraping functions directly from the main block.
Scrapy requires running a separate command from the terminal.
Additional Notes
Library Installations:
Use !pip install selenium and !pip install scrapy to install the required libraries.
Chromedriver Setup (Selenium):
Ensure that ChromeDriver is installed and accessible from your PATH or explicitly specify its location.
The code uses headless mode (chrome_options.add_argument("--headless")) for faster execution without a GUI.
Error Handling:
The Selenium scraper includes basic error handling to ensure the program doesn’t crash during extraction.
Key Takeaways
BeautifulSoup is simple and effective for static pages.
Scrapy is powerful for large-scale and structured scraping.
Selenium is indispensable for websites with dynamic content.
