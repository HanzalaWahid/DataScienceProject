# Question 1: Use yfinance to Extract Stock Data
# Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import time
import requests
import json
from selenium import webdriver

# Fetch Tesla stock data
Tesla_stock = yf.Ticker("TSLA")
Tesla_data = Tesla_stock.history(period="max")

# Display information about Tesla data and the first five rows
print(Tesla_data.info())
print(Tesla_data.head())

# Reset the index, save to a JSON file, and display the first five rows again
Tesla_data.reset_index(inplace=True)
Tesla_data.to_json('tesla_stock_data.json', orient='records', lines=True)
print(Tesla_data.head())

# Question 2: Use Webscraping to Extract Tesla Revenue Data
# Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
htmlContent = response.content

# Save the HTML content to a file (optional)
with open("revenue_page.html", "wb") as file:
    file.write(htmlContent)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(htmlContent, "html.parser")

# Extract the title of the HTML page
title = soup.title
print(title)

# Find the table containing revenue data (hypothetical example)
revenue_table = soup.find('table', {'class': 'historical_data_table'})

# Check if the table is found before proceeding
if revenue_table:
    # Initialize lists to store data
    dates = []
    revenues = []

    # Extract data from the table rows
    for row in revenue_table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        date = cols[0].get_text(strip=True)
        revenue = cols[1].get_text(strip=True)

        dates.append(date)
        revenues.append(revenue)

    # Create a DataFrame from the extracted data
    revenue_data = {'Date': dates, 'Revenue': revenues}
    tesla_revenue = pd.DataFrame(revenue_data)

    # Display the last five rows using the tail function
    print(tesla_revenue.tail())
else:
    print("Table not found. Check HTML structure or class names.")

#Question 3: Use yfinance to Extract Stock Data
# Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

# Fetch GameStop stock data
GameStock = yf.Ticker("GME")
GameStock_Data = GameStock.history(period="max")

# Display information about GameStop data, financials, and analyst price target
print(GameStock_Data.info())
print(GameStock_Data.head())


# Reset the index, save to a JSON file, and display the first five rows again
GameStock_Data.reset_index(inplace=True)
GameStock_Data.to_json('Game_stock_data.json', orient='records', lines=True)
print(GameStock_Data.head())

# Question 4: Use Webscraping to Extract GME Revenue Data
# Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Wait for the page to load (you might need to adjust the sleep time)

time.sleep(5)

# Extract HTML content after the page has loaded
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the table containing revenue data
revenue_table = soup.find('table', {'class': 'historical_data_table'})

# Extract data from the table
if revenue_table:
    data = []
    for row in revenue_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        date = cols[0].get_text(strip=True)
        revenue = cols[1].get_text(strip=True)
        data.append([date, revenue])

    # Create a DataFrame
    GameStock_revenue = pd.DataFrame(data, columns=['Date', 'Revenue'])

    # Display the last five rows
    print(GameStock_revenue.tail())
else:
    print("Table not found. Check HTML structure or class names.")


# Question 5: Plot Tesla Stock Graph
# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.
# Upload a screenshot of your results.

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data['Close'], label="Closing price", color="blue")
    plt.title(title)  # Use the provided title parameter
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

make_graph(Tesla_data, "Tesla Stock Price Data")


# Question 6: Plot GameStop Stock Graph
# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.
# Upload a screenshot of your results.

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data['Close'], label="Closing price", color="blue")
    plt.title(title)  # Use the provided title parameter
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

make_graph(GameStock_Data, "Game Stock Price Data")


