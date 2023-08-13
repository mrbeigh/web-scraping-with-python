import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.kashmiribeauty.com.bd/shop"

# Set a User-Agent header to mimic a web browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    # Send a request to the website and get the HTML response
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for any HTTP error

    # Create a BeautifulSoup object with the response HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product names within the specified div and extract the text
    product_names = [name.a.text.strip() for name in soup.find_all('h3', {'class': 'name'})]

    # Print the product names
    for name in product_names:
        print(name)

    # Save to CSV
    csv_filename = "data_received_kb.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Product Title'])  # Write the header
        for title in product_names:
            csv_writer.writerow([title])  # Write each product title
    print(f"CSV file '{csv_filename}' created successfully.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
