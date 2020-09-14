import requests
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
import os


def get_dialing_code(iso):
    for code, isos in COUNTRY_CODE_TO_REGION_CODE.items():
        if iso.upper() in isos:
            return code


def parse_file(filename, api_key, dialing_code, data_dict):
    file = open(filename, 'r')
    for line in file:
        if line.startswith('0'): number = line.strip('0').rstrip('\n')
        else: number = line.rstrip('\n')
        if number:
            carrier_name = api_request(api_key, dialing_code, number)
            data_dict[number] = carrier_name
            print(f'{number} : {carrier_name}')
    file.close()


def api_request(api_key, dialing_code, mobile_number):
    if api_key and dialing_code and mobile_number:
        url = f'https://api.data247.com/v3.0?key={api_key}&api=CI&phone={dialing_code}{mobile_number}'
        response = requests.get(url).json()
        carrier_name = response['response']['results'][0]['carrier_name']
        return carrier_name


def main(iso):
    # Config values
    api_key = os.getenv('API_KEY')
    filename = 'numbers.txt'
    data = {}
    
    dialing_code = get_dialing_code(iso) 
    
    parse_file(filename, api_key, dialing_code, data)
    return data