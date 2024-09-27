import logging
from genre_manager import GenreManager 

class DataCleaner:
    """Processes and cleans the data fetched from the TMDB API"""
    
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.genre_manager = GenreManager()
        
    def clean_data(self, data):
        self.logger.info("Processing the data...")
        cleaned_data = [] # Initialize an empty list to hold cleaned movie data
        
        # Check if there is data to process
        if data:
            for movie in data:
                # Create a dictionary with selected fields for each movie
                cleaned_movie = {
                    "title": movie.get("title", "Unknown Title"),
                    "release_date": movie.get("release_date", "Unknown Release Date"),
                    "rating": round(float(movie.get("vote_average", 0)), 1) if isinstance(movie.get("vote_average"), (int, float)) else 'N/A',
                    "overview": movie.get("overview", "No Overview Available"),
                    "genres": [self.genre_manager.get_genre_name(genre_id) for genre_id in movie.get("genre_ids", [])]

                }
                cleaned_data.append(cleaned_movie)
            self.logger.info(f"{len(cleaned_data)} movies have been cleaned.")
            return cleaned_data 
        self.logger.warning("No data to process.")
        return []