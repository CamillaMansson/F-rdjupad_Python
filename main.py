import logging
import os
from dotenv import load_dotenv
from api import API
from datacleaner import DataCleaner
from datasaver import DataSaver

load_dotenv()

logging.basicConfig(
    filename=r"C:\Users\camil\Desktop\Fördjupad_Pythonprogrammering\movie_mania\pipeline.log",
    format="[%(asctime)s][%(name)s] %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S", 
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Instantiate the classes for API, DataCleaner and DataSaver
api = API()
dc = DataCleaner()
ds = DataSaver()
logger.info("Starting data pipeline...")

data = api.fetch_data(pages=10)
if data:
    logger.info(f"Sample movie data: {data[0]}")  # Log an example movie.
    cleaned_data = dc.clean_data(data)
    ds.save_data(cleaned_data)
    logger.info("Data pipeline completed successfully.")
else:
    logger.warning("No data fetched, pipeline will not proceed.")
    