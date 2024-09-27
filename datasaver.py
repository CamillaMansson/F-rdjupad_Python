import logging
import sqlite3

class DataSaver:
    """Saves data in to a SQLite database"""
    
    def __init__(self, db_path=r"C:\Users\camil\Desktop\Fördjupad_Pythonprogrammering\movie_mania\movie_mania.db"):
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)
        
    def save_data(self, data):
        self.logger.info(f"Saved {len(data)} movies to the database.")  
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create the movies table if it doesn't already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                title TEXT PRIMARY KEY,  
                release_date TEXT,
                rating REAL,
                overview TEXT,
                genres TEXT
            )
        ''')

        # Iterate over each movie in the provided data list
        for movie in data:
            # Create a list of genres for the movie, replacing None values with an empty string
            genres = [genre if genre is not None else '' for genre in movie['genres']] 
            # Insert or update the movie record in the database with its details
            cursor.execute('''
                INSERT OR REPLACE INTO movies (title, release_date, rating, overview, genres)
                VALUES (?, ?, ?, ?, ?)
            ''', (movie["title"], movie["release_date"], movie["rating"], movie["overview"], ', '.join(genres))) # Join the genres into a single string, separated by commas

        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()
        self.logger.info("The movie data is saved")
     