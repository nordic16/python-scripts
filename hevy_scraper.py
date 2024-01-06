"""
This script scrapes all exercises from https://hevy.com
"""
BASE_URL = 'https://hevy.com/'

OFFSET = "0"
LIMIT = "200" # retrieve n workouts

import requests
from secret import HEVY_API_KEY, AUTH_TOKEN
import json

def main():
    HEADERS = {'x-api-key' : HEVY_API_KEY,  'auth-token' : AUTH_TOKEN, 
               'Content-Type' : 'application/json'}   

    rep = json.loads(requests.get(f'https://api.hevyapp.com/user_workouts_paged?username=xkyfal&offset={OFFSET}&limit={LIMIT}', headers=HEADERS).text)

    with open('workouts.txt', 'w') as f:
        f.writelines([f'{d["name"]} | {d["created_at"]}\n' for d in rep['workouts']])

    with open('exercises.txt', 'w+') as f:
        f.writelines([f'{ex["title"]}\n' for x in rep['workouts'] for ex in x['exercises'] if ex['title'] not in f.read()]) 



if __name__ == '__main__':
    main()
