import requests
import pdfkit
import os

def save_website_as_pdf(url, filename='website_content.pdf', folder='Data'):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Path to wkhtmltopdf executable (replace with your own path)
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    # Full path to save the PDF file
    filepath = os.path.join(folder, filename)

    # Convert website to PDF and save to the specified folder
    pdfkit.from_url(url, filepath, configuration=config)

    print("PDF created successfully.")

# Provide the URL of the website
url = "https://blog.google/products/pixel/pixel-feature-drop-march-2024/#pixel-phone"

# Save the website content as PDF
save_website_as_pdf(url)
