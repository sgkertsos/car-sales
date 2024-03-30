import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[data['saledate'] != '16500']
    data = data[data['saledate'] != '10500']
    data = data[data['saledate'] != '12700']
    data = data[data['saledate'] != '8250']
    data = data[data['saledate'] != '14300']
    data = data[data['saledate'] != '14500']
    data = data[data['saledate'] != '13500']
    data = data[data['saledate'] != '10700']
    data = data[data['saledate'] != '13600']
    data = data[data['saledate'] != '13000']
    data = data[data['saledate'] != '14000']
    data = data[data['saledate'] != '9800']
    data = data[data['saledate'] != '12900']
    data = data[data['saledate'] != '13500']
    data = data[data['saledate'] != '9900']
    data = data[data['saledate'] != '12900']
    data = data[data['saledate'] != '13500']
    data = data[data['saledate'] != '13500']
    data = data[data['saledate'] != '8500']
    data = data[data['saledate'] != '13400']
    data = data[data['saledate'] != '12200']
    data = data[data['saledate'] != '15250']
    data = data[data['saledate'] != '13100']
    data = data[data['saledate'] != '7500']
    data = data[data['saledate'] != '12100']
    data = data[data['saledate'] != '13600']

    data['saledate']=pd.to_datetime(data['saledate'],utc=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
