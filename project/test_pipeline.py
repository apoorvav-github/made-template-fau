import os
import pytest
import sys


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from extract import get_temperature_data, get_crop_yield_data  
from transform import process_temp_data, process_crop_data

data_dir = 'data'
temp_files = [
    'temp_change_annual.csv',
    'temp_change_seasonal.csv',
    'temp_change_met.csv',
    'std_dev_annual.csv',
    'std_dev_seasonal.csv',
    'std_dev_met.csv'
]
crop_files = [
    'ire_crop_prod.csv',
    'ire_crop_yield_per_hec.csv'
]


@pytest.fixture(scope='module')
def temp_data():
    df = get_temperature_data(temperature_change_url, csv_filename)
    assert df is not None
    assert not df.empty
    return df

@pytest.fixture(scope='module')
def crop_data():
    df = get_crop_yield_data(crop_yield_url)
    assert df is not None
    assert not df.empty
    return df


# URLs for the actual data
temperature_change_url = 'https://bulks-faostat.fao.org/production/Environment_Temperature_change_E_Europe.zip'
csv_filename = 'Environment_Temperature_change_E_Europe_NOFLAG.csv'
crop_yield_url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/AQA04/CSV/1.0/en'

def test_get_temperature_data_success():
    df = get_temperature_data(temperature_change_url, csv_filename)
    assert df is not None
    assert not df.empty

def test_get_crop_yield_data_success():
    df = get_crop_yield_data(crop_yield_url)
    assert df is not None
    assert not df.empty
        
        
def test_process_temp_data(temp_data):
    result = process_temp_data(temp_data)
    
    # Check if result is not None
    assert result is not None
    
    # Check for the keys in the result dictionary
    expected_keys = [
        'ire_temp_change_annual', 'ire_temp_change_seasonal', 'ire_temp_change_met',
        'ire_std_dev_annual', 'ire_std_dev_seasonal', 'ire_std_dev_met'
    ]
    for key in expected_keys:
        assert key in result

    # Check the structure of one of the DataFrames
    df = result['ire_temp_change_annual']
    assert 'Y2021' in df.columns
    assert 'Y2022' in df.columns

def test_process_crop_data(crop_data):
    result = process_crop_data(crop_data)
    
    # Check if result is not None
    assert result is not None
    
    # Check for the keys in the result dictionary
    expected_keys = ['ire_crop_prod', 'ire_crop_yield_per_hec']
    for key in expected_keys:
        assert key in result

    # Check the structure of one of the DataFrames
    df = result['ire_crop_prod']
    assert 'VALUE' in df.columns
    assert 'Statistic Label' in df.columns


def test_temperature_data_files():
    for filename in temp_files:
        filepath = os.path.join(data_dir, filename)
        assert os.path.exists(filepath), f"{filepath} does not exist."

def test_crop_data_files():
    for filename in crop_files:
        filepath = os.path.join(data_dir, filename)
        assert os.path.exists(filepath), f"{filepath} does not exist."