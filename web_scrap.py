import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


def scrape_wikipedia_tables(url):
    # Fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all tables in the page
    tables = soup.find_all("table", {"class": "wikitable"})

    all_data = []

    for i, table in enumerate(tables):
        # Extract all cells (th and td) from the table
        rows = table.find_all("tr")
        table_data = []

        for row in rows:
            cells = row.find_all(["th", "td"])
            row_data = [cell.text.strip() for cell in cells]
            if row_data:
                table_data.append(row_data)

        # Find the maximum number of columns
        max_cols = max(len(row) for row in table_data)

        # Pad rows with empty strings if necessary
        padded_data = [row + [""] * (max_cols - len(row)) for row in table_data]

        # Create DataFrame
        df = pd.DataFrame(padded_data)

        # If the first row seems to be a header, use it as column names
        if df.iloc[0].notna().all():
            df.columns = df.iloc[0]
            df = df[1:]

        # Reset index
        df = df.reset_index(drop=True)

        # Add to the list of all data
        all_data.append((f"Table_{i+1}", df))

    return all_data


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for table_name, df in data:
            writer.writerow([table_name])
            df.to_csv(file, index=False)
            writer.writerow([])  # Empty row between tables


# Example usage
url = "https://en.m.wikipedia.org/wiki/Politics_of_Bangladesh"
output_file = "wikipedia_tables.csv"

scraped_data = scrape_wikipedia_tables(url)
save_to_csv(scraped_data, output_file)

print(f"Tables have been scraped and saved to {output_file}")
