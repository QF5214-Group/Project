import requests
import pandas as pd

def cpi_function(date=None, api_key='7de51df1d77defbeae082211557f4d6a'):
    if date is None:
        date = pd.Timestamp.today().strftime('%Y-%m-%d')

    cpi_series_id = 'CPIAUCNS'  # CPI All Urban Consumers
    cpi_api_url = f'https://api.stlouisfed.org/fred/series/observations?series_id={cpi_series_id}&api_key={api_key}&file_type=json&observation_start={date}&observation_end={date}'
    

    cpi_response = requests.get(cpi_api_url)
    cpi_response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    
    cpi_data = cpi_response.json()

    # Check if observations are available
    if 'observations' not in cpi_data or not cpi_data['observations']:
        return None  # No data available for the specified date

    cpi_value = cpi_data['observations'][0]['value']
    return float(cpi_value)

#example
#cpi_function()
#cpi_function('2023-01-01')