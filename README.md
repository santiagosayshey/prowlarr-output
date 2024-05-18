# Prowlarr Search Script

This Python script allows you to search Prowlarr for specific queries using its API. Raw results are saved to the `*_raw.json` file, and titles are saved to the `*.txt` file.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/prowlarr-search-script.git
   cd prowlarr-search-script
   ```

2. Install the required libraries:

   ```sh
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the root directory of the project and add your Prowlarr API key:

   ```env
   PROWLARR_API_KEY=your_prowlarr_api_key
   ```

## Usage

1. Run the script:

   ```sh
   python out.py
   ```

2. When prompted, enter your search query (e.g., `av1`).

3. The script will generate two files:
   - `<query>_raw.json`: The raw JSON response from the Prowlarr API.
   - `<query>.txt`: A text file containing only the titles from the search results.

## Example

```sh
python out.py
Enter the search query: av1
```

This will create `av1_raw.json` and `av1.txt` in the current directory.

## Notes

- Make sure your Prowlarr instance is running and accessible at `http://localhost:9696`.
- Ensure your `.env` file contains the correct API key.

## License

This project is licensed under the MIT License.
