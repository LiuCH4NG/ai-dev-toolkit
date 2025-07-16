import requests

def fetch_data():
    """Fetches sample data from a public API."""
    try:
        response = requests.get("https://api.publicapis.org/entries")
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        print(f"Successfully fetched {data['count']} entries.")
        # Print the first 5 entries for brevity
        for i, entry in enumerate(data['entries'][:5]):
            print(f"{i+1}. {entry['API']}: {entry['Description']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data()
