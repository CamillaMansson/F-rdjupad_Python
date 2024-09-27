from api import API

api = API()

def test_api():
    # Test that fetch_data returns a list
    data = api.fetch_data()
    
    # Check that fetch_data returns a list
    assert isinstance(data, list), "fetch_data should return a list"