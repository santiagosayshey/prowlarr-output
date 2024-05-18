import requests
import urllib.parse
import json
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the Prowlarr API key from the environment variable
api_key = os.getenv('PROWLARR_API_KEY')
base_url = 'http://localhost:9696/api/v1/search'

# Check if the API key is loaded correctly
if not api_key:
    raise ValueError("API key not found. Please ensure the .env file contains the PROWLARR_API_KEY.")

# Prompt user for search query
query = input('Enter the search query: ').strip()
if not query:
    raise ValueError("Search query cannot be empty.")

# URL encode the query
encoded_query = urllib.parse.quote(query)

# Define search parameters
indexer_ids = '-1'  # Assuming -1 denotes all indexers (based on provided information)
categories = ''  # Leave empty for all categories
search_type = 'search'  # Replace with appropriate search type if needed (e.g., 'tvsearch', 'moviesearch', etc.)

# Construct the URL
url = f'{base_url}?query={encoded_query}&type={search_type}'

# Add indexerIds only if it's not empty
if indexer_ids:
    url += f'&indexerIds={indexer_ids}'

# Add categories only if it's not empty
if categories:
    url += f'&categories={categories}'

# Headers
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

# Send GET request
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    try:
        json_response = response.json()

        # Sanitize the query to create valid filenames
        sanitized_query = re.sub(r'[\\/*?:"<>|]', '_', query)

        # Save the raw JSON response to a file
        raw_filename = f'{sanitized_query}_raw.json'
        with open(raw_filename, 'w') as file:
            json.dump(json_response, file, indent=4)

        # Extract titles and save to a text file
        titles = [item['title'] for item in json_response if 'title' in item]
        titles_filename = f'{sanitized_query}.txt'
        with open(titles_filename, 'w') as file:
            for title in titles:
                file.write(title + '\n')

    except requests.exceptions.JSONDecodeError:
        with open(f'{sanitized_query}_error.txt', 'w') as file:
            file.write('Received non-JSON response\n')
            file.write(response.text)
else:
    with open(f'{sanitized_query}_error.txt', 'w') as file:
        file.write(f'Search failed\nStatus Code: {response.status_code}\n')
        file.write(response.text)
