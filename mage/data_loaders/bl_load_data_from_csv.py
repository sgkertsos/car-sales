import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    url = 'https://github.com/dgkertsos/car-sales/raw/main/data/car-prices.zip'
  
    data_types = {'year': pd.Int64Dtype(),
                    'make': str,
                    'model': str,
                    'trim': str,
                    'body': str,
                    'transmission': str,
                    'vin': str,
                    'state': str,
                    'condition': pd.Int64Dtype(),
                    'odometer': pd.Int64Dtype(),
                    'color': str,
                    'interior': str,
                    'seller': str,
                    'mmr': pd.Int64Dtype(),
                    'sellingprice': pd.Int64Dtype(),
                    'saledate': str }

    parse_dates = ['saledate']

    df = pd.read_csv(url, sep=',', dtype=data_types)

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
