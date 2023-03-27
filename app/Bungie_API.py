import os

import requests

OAUTH_URL = 'https://www.bungie.net/en/OAuth/Authorize'
OAUTH_CLIENT_ID = 43559
BUNGIE_API_KEY = "348fb15fd82d4bce8e6ab71bd6858a83"


def get_destiny2_character_data(membership_type: int, character_id: str) -> dict:
    '''
      Get Destiny 2 character data from Bungie API
      :param membership_type: 3 for PC, 1 for Xbox, 2 for PlayStation
      :param character_id: Destiny 2 character ID
      :return: Destiny 2 character data
    '''
    api_key = os.environ.get('BUNGIE_API_KEY', BUNGIE_API_KEY)
    if not api_key:
        raise ValueError('BUNGIE_API_KEY environment variable is not set')

    url = f'https://www.bungie.net/Platform/Destiny2/{membership_type}/Profile/{character_id}/?components=200'

    headers = {
        'X-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        character_data = response.json()['Response']['characters']['data']
        # process the character data from Bungie API for Destiny 2
        return character_data
        
    print(f'Error retrieving character data: {response.status_code}')
    return None

def get_profiles(membership_type: int, membership_id: str) -> dict:
    '''
    Get Destiny 2 profile data from Bungie API
    :param membership_type: 3 for PC, 1 for Xbox, 2 for PlayStation
    :param membership_id: Destiny 2 membership ID
    :return: Destiny 2 profile data
    '''
    api_key = os.environ.get('BUNGIE_API_KEY', BUNGIE_API_KEY)
    if not api_key:
        raise ValueError('BUNGIE_API_KEY environment variable is not set')

    url = f'https://www.bungie.net/Platform/Destiny2/{membership_type}/Profile/{membership_id}/?components=100'

    headers = {
        'X-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        profile_data = response.json()['Response']['profile']['data']
        # process the profile data from Bungie API for Destiny 2
        return profile_data

    print(f'Error retrieving profile data: {response.status_code}')
    return None