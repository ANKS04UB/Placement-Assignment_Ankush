#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
import json
from bs4 import BeautifulSoup

def download_and_extract_data(api_url):
    # Download the data from the API
    response = requests.get(api_url)
    data = response.json()

    # Extract the required attributes
    show_id = data['id']
    show_url = data['url']
    show_name = data['name']

    episodes = data['_embedded']['episodes']
    extracted_data = []

    for episode in episodes:
        episode_id = episode['id']
        episode_season = episode['season']
        episode_number = episode['number']
        episode_type = episode['type']
        episode_airdate = episode['airdate']
        episode_airtime = episode['airtime']
        episode_runtime = episode['runtime']
        episode_rating = episode['rating']['average']
        episode_summary = BeautifulSoup(episode['summary'], 'html.parser').get_text()
        episode_image_medium = episode['image']['medium']
        episode_image_original = episode['image']['original']

        extracted_data.append({
            'id': episode_id,
            'url': show_url,
            'name': show_name,
            'season': episode_season,
            'number': episode_number,
            'type': episode_type,
            'airdate': episode_airdate,
            'airtime': episode_airtime,
            'runtime': episode_runtime,
            'average rating': episode_rating,
            'summary': episode_summary,
            'medium image link': episode_image_medium,
            'original image link': episode_image_original
        })

    return extracted_data

# API URL
api_url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Call the function to download and extract the data
data = download_and_extract_data(api_url)

# Print the extracted data
for episode in data:
    print("Episode ID:", episode['id'])
    print("URL:", episode['url'])
    print("Name:", episode['name'])
    print("Season:", episode['season'])
    print("Number:", episode['number'])
    print("Type:", episode['type'])
    print("Airdate:", episode['airdate'])
    print("Airtime:", episode['airtime'])
    print("Runtime:", episode['runtime'])
    print("Average Rating:", episode['average rating'])
    print("Summary:", episode['summary'])
    print("Medium Image Link:", episode['medium image link'])
    print("Original Image Link:", episode['original image link'])
    print("----------------------------------------")


# In[ ]:





# In[ ]:





# In[ ]:




