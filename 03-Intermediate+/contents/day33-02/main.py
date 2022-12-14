# Imports

import requests

# Execution

parameters = {
    'lat': 51.507351,
    'lng': -0.127758
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
print(data)
