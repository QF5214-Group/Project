import requests
import pandas as pd

def non_farmer_function(date=None, api_key='7de51df1d77defbeae082211557f4d6a'):
    if date is None:
        date = pd.Timestamp.today().strftime('%Y-%m-%d')

    population_series_id = 'POPTHM'  # Total Population
    payems_series_id = 'PAYEMS'  # Nonfarm Payroll Employment

    # Fetch population data
    population_api_url = f'https://api.stlouisfed.org/fred/series/observations?series_id={population_series_id}&api_key={api_key}&file_type=json&observation_start={date}&observation_end={date}'
    population_response = requests.get(population_api_url)
    population_data = population_response.json()

    # Check if observations are available
    if 'observations' not in population_data or not population_data['observations']:
        return None  # No data available for the specified date

    total_population = float(population_data['observations'][0]['value'])

    # Fetch nonfarm employment data
    payems_api_url = f'https://api.stlouisfed.org/fred/series/observations?series_id={payems_series_id}&api_key={api_key}&file_type=json&observation_start={date}&observation_end={date}'
    payems_response = requests.get(payems_api_url)
    payems_data = payems_response.json()

    # Check if observations are available
    if 'observations' not in payems_data or not payems_data['observations']:
        return None  # No data available for the specified date

    nonfarm_employment = float(payems_data['observations'][0]['value'])

    # Calculate nonfarm population ratio
    nonfarm_population_ratio = nonfarm_employment / total_population

    return nonfarm_population_ratio

#example
#non_farmer_function()
#non_farmer_function('2022-10-09')
