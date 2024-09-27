from datacleaner import DataCleaner

def test_clean_data_correct_formatting():
    """Test that the clean_data function correctly processes raw movie data"""
    # Create an instance of DataCleaner
    data_cleaner = DataCleaner()

    # Simulated raw data with various scenarios
    raw_movie_data = [
        {
            "title": "Test Movie",
            "release_date": "2024-09-25",
            "vote_average": 8.1,
            "overview": "This is a test movie"
        },
        {
            "title": "Another Test Movie",
            "release_date": "2024-09-26",
            "vote_average": 7.4,
            "overview": "This is another test movie"
        },
        {
            "title": "Movie with Missing Overview",
            "release_date": "2024-09-27",
            "vote_average": 6.5,  
        },
        {
            "title": "Movie with Missing Fields",
            "release_date": "2024-09-28",
        },
        {
            
        }
    ]

    # Process the raw data
    cleaned_movie_data = data_cleaner.clean_data(raw_movie_data)

    # Check that the correct number of movies is in the cleaned data
    assert len(cleaned_movie_data) == 5

    # Check that the first movie has the correct title and rating
    assert cleaned_movie_data[0]["title"] == "Test Movie"
    assert cleaned_movie_data[0]["rating"] == 8.1

    # Check that the second movie has the correct release date
    assert cleaned_movie_data[1]["release_date"] == "2024-09-26"
    
    # Check that movies with missing fields are handled correctly
    assert cleaned_movie_data[2]["overview"] == "No Overview Available"  
    assert cleaned_movie_data[3]["rating"] == 'N/A'  

    # Check that the movie with all fields missing receives default values
    assert cleaned_movie_data[4]["title"] == "Unknown Title"
    assert cleaned_movie_data[4]["release_date"] == "Unknown Release Date"
    assert cleaned_movie_data[4]["rating"] == 'N/A'
    assert cleaned_movie_data[4]["overview"] == "No Overview Available"
