import logging
import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file so that the API key can be used.
load_dotenv()

class API:
    """Class to fetch data from TMDB API."""
    def __init__(self) -> None:
        self.api_key = os.getenv("TMDB_API_KEY")
        self.base_url = "https://api.themoviedb.org/3"
        self.logger = logging.getLogger(__name__)
        
    def fetch_data(self, pages=1):
        """Fetch popular movies from TMDB API across multiple pages."""
        self.logger.info("Fetching data from TMDB")
        all_movies = []
        
        try:
            for page in range(1, pages + 1):  # Loop through the number of pages
                endpoint = f"{self.base_url}/movie/popular"
                params = {
                    "api_key": self.api_key,
                    "language": "en-US",  
                    "page": page
                }
                response = requests.get(endpoint, params=params)
                response.raise_for_status()
                
                self.logger.info(f"Page {page} fetched successfully.")
                all_movies.extend(response.json()["results"])
                
            return all_movies
        
        except requests.exceptions.HTTPError as http_err:
            self.logger.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            self.logger.error(f"Request error occurred: {req_err}")
        return []