import os
import logging

def save_temperature_data_to_csv(ire_temp_data):
    """
    Saves the temperature change and standard deviation DataFrames to CSV files in a 'data' directory.

    Parameters:
    - ire_temp_data (dict): A dictionary containing DataFrames for different temperature change
                            and standard deviation categories.

    Returns:
    - None
    """
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

    filenames = {
        'ire_temp_change_annual': 'temp_change_annual.csv',
        'ire_temp_change_seasonal': 'temp_change_seasonal.csv',
        'ire_temp_change_met': 'temp_change_met.csv',
        'ire_std_dev_annual': 'std_dev_annual.csv',
        'ire_std_dev_seasonal': 'std_dev_seasonal.csv',
        'ire_std_dev_met': 'std_dev_met.csv'
    }

    try:
        for key, filename in filenames.items():
            if key in ire_temp_data:
                ire_temp_data[key].to_csv(os.path.join(directory, filename), index=False)
                logging.info(f"Saved {filename} successfully.")
            else:
                logging.warning(f"{key} not found in the provided data.")
        print("Saved All Files")
    except Exception as e:
        logging.error(f"An error occurred while saving files: {e}")

# Ensure logging is configured to show messages
logging.basicConfig(level=logging.INFO)



def save_crop_data_to_csv(ire_crop_data):
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

    filenames = {
        'ire_crop_prod': 'ire_crop_prod.csv',
        'ire_crop_yield_per_hec': 'ire_crop_yield_per_hec.csv'
    }

    try:
        for key, filename in filenames.items():
            if key in ire_crop_data:
                ire_crop_data[key].to_csv(os.path.join(directory, filename), index=False)
                logging.info(f"Saved {filename} successfully.")
            else:
                logging.warning(f"{key} not found in the provided data.")
        print("Saved All Files")
    except Exception as e:
        logging.error(f"An error occurred while saving files: {e}")