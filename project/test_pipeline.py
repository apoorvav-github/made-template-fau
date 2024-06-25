import os
import io
import pytest
import sys
import pandas as pd


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from transform import process_temp_data, process_crop_data

@pytest.fixture(scope='module')
def temp_data():
    data = """
    ,Area Code,Area Code (M49),Area,Months Code,Months,Element Code,Element,Unit,Y1961,Y1962,Y1963,Y1964,Y1965,Y1966,Y1967,Y1968,Y1969,Y1970,Y1971,Y1972,Y1973,Y1974,Y1975,Y1976,Y1977,Y1978,Y1979,Y1980,Y1981,Y1982,Y1983,Y1984,Y1985,Y1986,Y1987,Y1988,Y1989,Y1990,Y1991,Y1992,Y1993,Y1994,Y1995,Y1996,Y1997,Y1998,Y1999,Y2000,Y2001,Y2002,Y2003,Y2004,Y2005,Y2006,Y2007,Y2008,Y2009,Y2010,Y2011,Y2012,Y2013,Y2014,Y2015,Y2016,Y2017,Y2018,Y2019,Y2020,Y2021,Y2022,Y2023
0,3,'008,Albania,7001,January,7271,Temperature change,°c,0.186,1.416,-1.782,-2.32,0.63,-1.501,-1.887,-2.29,-0.882,1.785,2.409,1.643,0.225,0.751,-0.64,-0.031,1.228,0.14,-0.537,-1.651,-2.58,0.297,0.571,1.055,-0.974,0.623,-0.21,2.491,-0.747,-1.019,-0.614,-0.148,-0.392,2.013,-0.101,1.107,1.975,1.904,0.997,-2.589,3.002,-0.899,1.928,-0.508,0.328,-1.15,2.669,1.235,1.2,0.993,0.903,-1.068,1.372,3.38,1.105,1.222,-2.671,2.239,-1.02,1.073,1.908,0.561,2.704
1,3,'008,Albania,7001,January,6078,Standard Deviation,°c,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479,1.479
2,3,'008,Albania,7002,February,7271,Temperature change,°c,-0.611,-2.121,-0.618,-0.931,-4.308,2.847,-1.221,1.317,0.441,0.124,-0.451,1.457,-0.081,1.718,-1.516,-0.36,3.208,0.855,1.356,-0.391,-1.196,-1.856,-2.311,-0.327,-3.477,-0.646,0.762,0.143,1.192,2.261,-1.776,-1.14,-2.121,0.361,2.193,-1.04,0.709,2.21,-1.453,-0.15,1.256,3.062,-3.839,0.406,-2.547,-0.485,2.279,0.973,-0.819,0.816,0.555,-2.736,1.172,3.35,0.255,4.456,2.463,0.63,1.381,2.182,2.099,1.417,0.616
    """
    return pd.read_csv(io.StringIO(data))

@pytest.fixture(scope='module')
def crop_data():
    data = """
"STATISTIC","Statistic Label","TLIST(A1)","Year","C02039V02469","Type of Crop","UNIT","VALUE"
"AQA04C2","Crop Yield per Hectare","2023","2023","012","Total oats","Tonnes","7"
"AQA04C2","Crop Yield per Hectare","2023","2023","0121","Winter oats","Tonnes","7.9"
"AQA04C2","Crop Yield per Hectare","2023","2023","0122","Spring oats","Tonnes","6.5"
"AQA04C2","Crop Yield per Hectare","2023","2023","013","Total barley","Tonnes","7"
"AQA04C2","Crop Yield per Hectare","2023","2023","0131","Winter barley","Tonnes","8.7"
"AQA04C2","Crop Yield per Hectare","2023","2023","0132","Spring barley","Tonnes","6.3"
"AQA04C3","Crop Production","2011","2011","0132","Spring barley","000 Tonnes","1085.8"
"AQA04C3","Crop Production","2012","2012","013","Total barley","000 Tonnes","1260.7"
"AQA04C3","Crop Production","2012","2012","02","Beans and peas","000 Tonnes","19.7"
"AQA04C3","Crop Production","2012","2012","03","Oilseed rape","000 Tonnes","58.7"
"AQA04C3","Crop Production","2012","2012","04","Potatoes","000 Tonnes","232"
    """
    return pd.read_csv(io.StringIO(data))

def test_get_temperature_data_success(temp_data):
    df = temp_data
    assert df is not None
    assert not df.empty

def test_get_crop_yield_data_success(crop_data):
    df = crop_data
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
    print(df)

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
    print(df)