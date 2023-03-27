import os

import requests

import logging

import fastapi

from Bungie_API_Models import GetFriendsListResponse
from Bungie_Enums import staticURLs
from Bungie_Item_Models import Friend
from Bungie_API_Models import BungieResponse

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
    :param membership_type: 3 for PC, 1 for Xbox, 2 for PlayStation, 254 for BungieNext
    :param membership_id: Bungie membership ID
    :return: Destiny 2 profile data
    '''
    api_key = os.environ.get('BUNGIE_API_KEY', BUNGIE_API_KEY)
    if not api_key:
        raise ValueError('BUNGIE_API_KEY environment variable is not set')

    headers = {
        'X-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    url = f'{staticURLs.DESTINY2.value}/{membership_type}/Profile/{membership_id}/?components=100'

    try:
        response = requests.get(url, headers=headers).content.decode(encoding='utf8')
        response = BungieResponse.parse_raw(response)


        if response.ErrorCode == 1:
            profileData = response.Response
            return profileData
        
        logging.error(f"Error retrieving profile: {response.json()}")
        raise Exception(f'Error retrieving profiles: {response}')

    except Exception as exception:
        logging.error(f"Error retrieving profile data: {exception}")
        raise Exception(f'Error retrieving profile data: {exception}')




def getFriendsList() -> list[Friend]:
    '''
    Get Destiny 2 friends list from Bungie API
    :return: Destiny 2 friends list
    '''

    api_key = os.environ.get('BUNGIE_API_KEY', BUNGIE_API_KEY)
    if not api_key:
        raise ValueError('BUNGIE_API_KEY environment variable is not set')

    headers = {
        'X-API-Key': api_key,
        'Content-Type': 'application/json'
    }

    try:

        logging.debug('Calling Bungie API to get friends list')
        response = requests.get(staticURLs.GetFriendsList.value, headers=headers).content.decode(encoding='utf8')
        response = GetFriendsListResponse.parse_raw(response)

        if response.ErrorCode == 1:
            friends_list: list[Friend] =  response.Response['friends']
            return friends_list
        
        logging.error(f"Error retrieving friends list: {response.json()}")
        raise Exception(f'Error retrieving friends list: {response}')
        
    except Exception as exception:
        logging.error(f'Error calling Bungie API: {exception}')
        raise Exception(f'Error calling Bungie API: {exception}')
