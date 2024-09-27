class GenreManager:
    """Handles genre mapping for movies"""
    def __init__(self):
        # Create a dictionary for genre ID 
        self.genre_mapping = {
            28: "Action",
            12: "Adventure",
            16: "Animation",
            35: "Comedy",
            80: "Crime",
            99: "Documentary",
            18: "Drama",
            10751: "Family",
            14: "Fantasy",
            36: "History",
            27: "Horror",
            10402: "Music",
            9648: "Mystery",
            10749: "Romance",
            878: "Science Fiction",
            10770: "TV Movie",
            53: "Thriller",
            10752: "War",
            37: "Western",
        }

    def get_genre_name(self, genre_id):
        """Returns the genre name for a given genre ID."""
        return self.genre_mapping.get(genre_id)