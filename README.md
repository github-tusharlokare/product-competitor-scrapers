# product-competitor-scrapers
This repository contains two web scrapers designed to extract competitor data from Amazon and Flipkart for various product categories such as Aloe Vera Gel, Body Lotion, Body Wash, Shampoo, Hair Oil, and Baby Wipes. The scraped data will be used to assist with product pricing and positioning during a product launch.

## Steps to Scrape Data from Flipkart
1. Identify the Product Category
Go to Flipkart and navigate to the product category you wish to scrape.
2. Install Web Scraper Extension
Install the https://webscraper.io Chrome extension from the Chrome Web Store.
3. Access Flipkart
Open Flipkart in your browser.
4. Inspect the Element
Right-click on the product listings page and select "Inspect" to open the browser's Developer Tools.
5. Create a New Scraper
Open the Web Scraper extension and create a new "Sitemap".
6. Add Paginated URLs
Add the paginated URLs of the listing pages in the metadata section of the Web Scraper settings. This allows the scraper to navigate through multiple pages.
7. Set Up the Scraper
Create a new Scraper within the Web Scraper extension for the specific product category.
8. Define the CSS Selectors
Add the CSS selectors for the product links (e.g., a[href]) to ensure that all product links are captured.
9. Scrape and Export Data
Run the scraper to collect the data. Export the data to a CSV file using the Web Scraper extension.
10. Utilize the Data
The exported CSV file will contain the product listings which can be used as input for further processing with Selenium HTML downloads.

### Download HTML Pages
11. Download HTML Pages
Use the html_download.py script to download the .html pages of the actual listing pages identified in the previous steps.
12. Wait for the Download to Finish
Ensure that all the .html pages are fully downloaded before proceeding to the next step.
13. Verify Download Completion
Confirm that all required HTML pages have been successfully downloaded.
### Parse HTML Pages
14. Run the Flipkart Parser
Execute the Flipkart parser on the downloaded .html pages to extract and process the required data.

#### >> Follow the same process for Amazon parser on the downloaded HTML pages. <<
