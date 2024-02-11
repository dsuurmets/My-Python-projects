#this is for web scraping, get gas prices in LV-EE region

# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Compute the day after tomorrow
today = datetime.now().date()
day_after_tomorrow = today + timedelta(days=2)
date_to = day_after_tomorrow.strftime("%Y-%m-%d")

url = f"https://www.getbaltic.com/en/market-data/trading-data/?date_to={date_to}&period=day&graph=trades&area=23&show=price&display=table"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table element containing the data
    table = soup.find("table")

    # Extract the table headers
    headers = [th.text for th in table.find_all("th")]

    # Extract the table rows
    rows = []
    for tr in table.find_all("tr"):
        row = [td.text.strip() for td in tr.find_all("td")]
        if row:
            rows.append(row)

    # Print the headers and rows
    print(headers)
    for row in rows:
        print(row)
else:
    print("Failed to fetch the URL. Status code:", response.status_code)
# %%
df=pd.DataFrame(rows, columns=['Delivery period', 'Lowest price, EUR/MWh', 'Highest price, EUR/MWh', 'BGSI LV-EE, EUR/MWh', 'BGSI-DA LV-EE, EUR/MWh'])
df.drop(index=df.index[0], axis=0, inplace=True)
df
