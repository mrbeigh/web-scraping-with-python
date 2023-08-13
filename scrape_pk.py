import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.premiumkashmir.com/shop"

# Send a request to the website and get the HTML response
response = requests.get(url)

# Create a BeautifulSoup object with the response HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product titles within the specified div and extract the text
product_titles = [title.text.strip() for title in soup.find_all('div', {'class': 'eael-product-title'})]

# Print the product titles
print(product_titles)

#save to CSV
csv_filename = "data_received_pk.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Title'])  # Write the header
    for title in product_titles:
        csv_writer.writerow([title])  # Write each product title
print(f"CSV file '{csv_filename}' created successfully.")
