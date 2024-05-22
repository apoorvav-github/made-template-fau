import os
import logging
import pandas as pd
from extract import get_temperature_data, get_crop_yield_data
from transform import process_temp_data, process_crop_data
from save import save_temperature_data_to_csv, save_crop_data_to_csv



def main():
    """
    Main function to download, process, and save temperature and crop yield data.
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    try:
        # Temperature data processing
        temperature_change_url = 'https://bulks-faostat.fao.org/production/Environment_Temperature_change_E_Europe.zip'
        csv_filename = 'Environment_Temperature_change_E_Europe_NOFLAG.csv'
        temp_df = get_temperature_data(temperature_change_url, csv_filename)
        if temp_df is not None:
            ire_temp_data = process_temp_data(temp_df)
            save_temperature_data_to_csv(ire_temp_data)
        else:
            logging.error("Temperature data could not be retrieved.")

        # Crop yield data processing
        crop_yield_url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/AQA04/CSV/1.0/en'
        crop_yield_df = get_crop_yield_data(crop_yield_url)        
        if crop_yield_df is not None:
            ire_crop_data = process_crop_data(crop_yield_df)
            save_crop_data_to_csv(ire_crop_data)
        else:
            logging.error("Crop yield data could not be retrieved.")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
