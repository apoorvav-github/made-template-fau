import requests
import zipfile
import io
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_temperature_data(temperature_change_url, csv_filename):
    """
    Downloads a ZIP file from the given URL, extracts the specified CSV file,
    and returns it as a Pandas DataFrame.

    Parameters:
    - temperature_change_url (str): The URL of the ZIP file to download.
    - csv_filename (str): The name of the CSV file to extract from the ZIP file.

    Returns:
    - DataFrame: Pandas DataFrame containing the data from the CSV file.
    - None: If the CSV file is not found or if there is an error.
    """
    try:
        response = requests.get(temperature_change_url)
        response.raise_for_status() 
        logger.info("Downloaded the ZIP file successfully.")
        
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            file_names = zip_file.namelist()
            if csv_filename in file_names:
                with zip_file.open(csv_filename) as f:
                    try:
                        df = pd.read_csv(f, encoding='latin-1')
                    except UnicodeDecodeError:
                        df = pd.read_csv(f, encoding='ISO-8859-1')
                    logger.info("CSV file loaded into DataFrame successfully.")
                    return df
            else:
                logger.error(f"{csv_filename} is not present in the ZIP file.")
                return None
    except requests.RequestException as e:
        logger.error(f"Failed to download the ZIP file: {e}")
        return None
    except zipfile.BadZipFile as e:
        logger.error(f"Failed to read the ZIP file: {e}")
        return None
    except pd.errors.EmptyDataError as e:
        logger.error(f"No data in the CSV file: {e}")
        return None


def get_crop_yield_data(crop_yield_url):
    """
    Downloads and returns the crop yield data from the given URL.

    Parameters:
    - crop_yield_url (str): The URL of the crop yield data CSV file.

    Returns:
    - DataFrame: Pandas DataFrame containing the crop yield data.
    - None: If the data could not be retrieved.
    """
    try:
        response = requests.get(crop_yield_url)
        response.raise_for_status() 
        crop_yield_df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
        logging.info("Crop yield data downloaded and loaded into DataFrame successfully.")
        return crop_yield_df
    except requests.RequestException as e:
        logging.error(f"Failed to download crop yield data: {e}")
        return None
    except pd.errors.EmptyDataError as e:
        logging.error(f"No data in the crop yield CSV file: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred while processing crop yield data: {e}")
        return None