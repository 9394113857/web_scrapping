# 1. Import the necessary libraries:
import re
import requests
from bs4 import BeautifulSoup
import csv

# 2.Load the links from the CSV file:
links = []
with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        links.append(row[0])

# 3. Define a function to scrape the remaining content of each link:
def scrape_date(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_str = soup.find('span', {'class': 'B_NuCI'}).text
    title = re.sub(r'\W+', ' ', title_str)  # remove all non-alphanumeric characters
    price_str = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text
    price = re.sub(r'[^\d\.]+', '', price_str)  # extract numeric portion of price string
    rating_str = soup.find('div', {'class': '_3LWZlK'}).text
    rating = re.sub(r'\W+', ' ', rating_str)  # remove all non-alphanumeric characters
    reviews_str = soup.find('span', {'class': '_2_R_DZ'}).text
    reviews = re.sub(r'\W+', ' ', reviews_str)  # remove all non-alphanumeric characters
    # description = soup.find('div', {'class': '_1y9a40'}).text
    return title, price, rating, reviews  # description

# 4. Call the scrape_data() function for each link and write the data to a CSV file:
with open('data.csv', 'w', newline='', encoding='utf-8') as file: # add encoding parameter
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Rating', 'Reviews']) # Description
    for link in links:
        data = scrape_date(link)
        print(data)
        writer.writerow(data)

