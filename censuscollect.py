import os
import requests

def get_population_data(year):
    url = f'https://api.census.gov/data/{year}/pep/population?'
    params = {
        'get': f'POP_{year},NAME,STATE',
        'for': 'state:*'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Write data to CSV file
        directory = 'population_data'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f'{directory}/population_data_{year}.csv'
        with open(filename, 'w') as f:
            for row in data:
                f.write(','.join(row) + '\n')
        print(f"Population data for {year} saved to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving populations data for {year}:", e)
    
def get_economic_census(): 
    url = 'https://api.census.gov/data/2022/ecnbasic?'
    params = { 
        "get": 'BENEFIT', 
        "for": 'us:*'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        directory = 'economic_census'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f'{directory}/economic_census_2022.csv'
        with open(filename, 'w') as f:
            for row in data:
                f.write(','.join(row) + '\n')
        print(f"Economic census for 2022 saved to {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving populations data for 2022:", e)
        return None


def main():
    # Iterate over years from 2021 to 2010
    get_economic_census() 
    # for year in range(2021, 2009, -1):
    #     get_population_data(year)


    

    

if __name__ == "__main__":
    main()