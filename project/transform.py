import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_temp_data(temp_df):
    """
    Processes temperature data for Ireland by filtering for annual, seasonal,
    and meteorological data changes and standard deviations.

    Parameters:
    - temp_df (DataFrame): The original temperature DataFrame.

    Returns:
    - dict: A dictionary containing processed DataFrames for different temperature
            change and standard deviation categories.
    """
    try:
        # Filter data for Ireland
        ire_temp_df = temp_df[temp_df['Area'] == 'Ireland']
        
        # Split data for temperature change and standard deviation
        ire_temp_change = ire_temp_df[ire_temp_df['Element Code'] == 7271]
        ire_std_deviation = ire_temp_df[ire_temp_df['Element Code'] == 6078]
        
        # Define the ranges for different categories
        categories = {
            'annual': (7001, 7012),
            'seasonal': (7016, 7019),
            'met': (7020, 7020)
        }
        
        ire_data = {}

        # Process each category for temperature change and standard deviation
        for category, (start, end) in categories.items():
            temp_change_cat = ire_temp_change[ire_temp_change['Months Code'].between(start, end)]
            std_dev_cat = ire_std_deviation[ire_std_deviation['Months Code'].between(start, end)]
            
            # Drop unnecessary columns
            columns_to_drop = ['Area Code', 'Area Code (M49)', 'Area', 'Months Code', 'Element Code', 'Element', 'Unit']
            temp_change_cat = temp_change_cat.drop(columns=columns_to_drop)
            std_dev_cat = std_dev_cat.drop(columns=columns_to_drop)
            
            # Add to the result dictionary
            ire_data[f'ire_temp_change_{category}'] = temp_change_cat
            ire_data[f'ire_std_dev_{category}'] = std_dev_cat
        
        return ire_data
    
    except KeyError as e:
        logging.error(f"Missing expected column: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while processing the data: {e}")
        return None


def process_crop_data(crop_yield_df):
    try:
        # Filter data for Ireland
        ire_crop_prod_df = crop_yield_df[crop_yield_df['Statistic Label'] == 'Crop Production']
        ire_crop_yield_per_hec_df = crop_yield_df[crop_yield_df['Statistic Label'] == 'Crop Yield per Hectare']
        
        ire_crop_data = {}
            
        # Drop unnecessary columns
        columns_to_drop = ['STATISTIC', 'TLIST(A1)', 'C02039V02469', 'UNIT']
        ire_crop_prod_df = ire_crop_prod_df.drop(columns=columns_to_drop)
        ire_crop_yield_per_hec_df = ire_crop_yield_per_hec_df.drop(columns=columns_to_drop)
        
        # Add to the result dictionary
        ire_crop_data['ire_crop_prod'] = ire_crop_prod_df
        ire_crop_data['ire_crop_yield_per_hec'] = ire_crop_yield_per_hec_df
        
        return ire_crop_data
    
    except KeyError as e:
        logging.error(f"Missing expected column: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while processing the data: {e}")
        return None
    