# 1.Import the necessary libraries:
import requests
from bs4 import BeautifulSoup
import csv

# 2.Define a function to get the links from multiple pages of 'realme phones':
def get_links():
    links = []
    for i in range(1, 2):
        url = f'https://www.flipkart.com/search?q=realme+phones&page={i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', {'class': '_1fQZEK'}):
            links.append('https://www.flipkart.com' + link.get('href'))
        return links

# 3.Call the get_links() function to get the links and write them to a csv file:
links = get_links()

with open('links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for link in links:
        print(link)
        writer.writerow([link])
