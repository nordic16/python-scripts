#!/usr/bin/python

###############################
# Author: Nørdic
# Version: v1.0.0
# Date: 26/3/2021 (3/26/2021)
# Description: Retrieves info from a certain TV Show, using the free TMDB API.
# Usage: ./s_show search/info [OPTIONS]
# Location: Should be put on /bin
###############################

import json, requests, argparse

BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = '[API_KEY]'

### Handles searching.
def search(query, page):
    json = requests.get(f'{BASE_URL}/search/tv?api_key={API_KEY}&language=en-US&page={page}&query={query}&include_adult=false').json()

    if len(json['results']) == 0:
        print('Found no results!') 
     
    # Prints the names and IDs of all shows retrieved by the API.       
    else: 
        [print(f'{json["results"][i]["name"]} | {json["results"][i]["id"]}') for i in range(0, len(json['results']))] 
        print(f'\nPage {page} of {json["total_pages"]}...')

### Gets info about a tv show with a specific id.
def getInfo(id : int):
    json = requests.get(f'{BASE_URL}/tv/{id}?api_key={API_KEY}&language=en-US').json()
    
    print(f'---Info about {json["name"]}---')
    print(f'Original name: {json["original_name"]}')
    print(f'Type: {json["type"]}')
    
    # Gets all genre names and appends them to a single string, separated by |.
    print(f'Genres: {" | ".join([x.get("name") for x in json["genres"]])}')
    print(f'Number of seasons: {json["number_of_seasons"]}')
    #print(f'Overview: {json["overview"] if json["overview"] else "No overview available"}')
    print(f'Number of episodes: {json["number_of_episodes"] if json["number_of_episodes"] else "No episodes available"}')
    print(f'Status: {json["status"]}')

def main():
    if API_KEY != "[API_KEY]":
        # Parses arguments (obviously)
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest='command')
    
        search_parser = subparsers.add_parser('search', help='Allows you to search for a specific TV Show.')
        id_parser = subparsers.add_parser('info', help='Allows you to retrieve information about a specific TV Show.')

        id_parser.add_argument('-i', '--id', type=int, required=True)

        search_parser.add_argument('-Q', '--query', required=True)
        search_parser.add_argument('-p', '--page', type=int,default=1)
    
        args = parser.parse_args()
    
        if args.command == 'search': 
            # Searches only if args.page < 501 and > 0   
            search(args.query, args.page) if args.page < 501 and args.page > 0 else print('Page must be less or equal to 500, and bigger than 0.') 
 
        #tmdb supports up to 500 pages. 
        elif args.command == 'info': 
            getInfo(args.id) if args.id > 0 else print('ID cannot be equal or less than 0.')
    
    else: print("API key not set!")

                
if __name__ == "__main__":
    main()
