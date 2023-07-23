import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
import openpyxl


def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the relevant information from the website
    products = soup.find_all('div', class_='product')

    # Store the scraped data in a list of dictionaries
    data = []
    for product in products:
        name = product.find('h2').text.strip()
        price = product.find('span', class_='price').text.strip()
        data.append({'Product Name': name, 'Price': price})

    return data


def create_database(data):
    # Create a pandas DataFrame from the scraped data
    df = pd.DataFrame(data)

    # Perform any additional data manipulation or analysis here

    return df


def save_to_excel(df):
    # Open a Tkinter dialog to ask for the save location and filename
    Tk().withdraw()
    filename = asksaveasfilename(defaultextension='.xlsx')

    # Save the DataFrame to an Excel file
    df.to_excel(filename, index=False)
    print('Data saved successfully.')


# Main program
if __name__ == '__main__':
    # URL of the shopping website to scrape
    url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=dc9ca94f-ad84-40e1-b6b7-2758290f59bb'

    # Scrape the website
    scraped_data = scrape_website(url)

    # Create a database from the scraped data
    database = create_database(scraped_data)

    # Save the database to an Excel file
    save_to_excel(database)
