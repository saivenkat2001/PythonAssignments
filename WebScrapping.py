import tkinter as tk

import requests

from bs4 import BeautifulSoup

import os

def scrape_website():
    website_url = website_entry.get()

    try:

        response = requests.get(website_url)

        response.raise_for_status()  # Checking for a successful response

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting all text from the HTML

        scraped_value = soup.get_text()

        result_label.config(text="Scraped Value (First 500 characters):\n" + scraped_value)

        # Saving the scraped data to a PDF file

        save_to_pdf(website_url, scraped_value)

    except requests.exceptions.RequestException as e:

        result_label.config(text=f"Error: {str(e)}")

    except Exception as e:

        result_label.config(text=f"Scraping error: {str(e)}")


def save_to_pdf(website_url, scraped_value):
    website_name = website_url.split('//')[1].split('/')[0]
    pdf_directory = os.getcwd()
    pdf_filename = f"{pdf_directory}\\{website_name}_home.txt"
    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory)

    with open(pdf_filename, 'w', encoding='utf-8') as file:
        file.write(scraped_value)


app = tk.Tk()

app.title("Web Scraper")

website_label = tk.Label(app, text="Enter Website URL:")

website_label.pack()

website_entry = tk.Entry(app)

website_entry.pack()

scrape_button = tk.Button(app, text="Scrape", command=scrape_website)

scrape_button.pack()

result_label = tk.Label(app, text="")

result_label.pack()

app.mainloop()