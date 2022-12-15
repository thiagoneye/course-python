# Imports

import requests
from datetime import datetime

# Constants

UFPB_LAT = -7.142147
UFPB_LNG = -34.850973

# Functions

def get_iss_position() -> tuple:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])

    return (latitude, longitude)

def check_distance(point1: tuple, point2: tuple, reference: float) -> bool:
    distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**(1/2)

    return distance <= reference

def check_dawn(parameters: dict) -> bool:
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = data['results']['sunrise']
    sunrise = sunrise.split('T')[1]
    sunrise = int(sunrise.split(':')[0]) + int(sunrise.split(':')[1])/60

    sunset = data['results']['sunset']
    sunset = sunset.split('T')[1]
    sunset = int(sunset.split(':')[0]) + int(sunset.split(':')[1])/60

    time_now = datetime.now().hour + datetime.now().minute/60

    return (time_now > sunset) and (24 - time_now < sunrise)

def send_a_email(connection, address_email: str):
    message = 'Subject:Look Up\n\nThe ISS is above you in the sky.'

    connection.sendmail(
        from_addr=my_email,
        to_addrs=address_email,
        msg=message
    )

# Execution

if __name__ == '__main__':
    my_email = input('Username: ')
    my_password = getpass.getpass()

    parameters = {
        'lat': UFPB_LAT,
        'lng': UFPB_LNG,
        'formatted': 0
    }

    ufpb_position = (UFPB_LAT, UFPB_LNG)
    iss_position = get_iss_position()

    if check_dawn(parameters) and check_distance(ufpb_position, iss_position, 5.0):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        send_a_email(connection, address_email: str, message: str)
