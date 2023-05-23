#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import json
import pandas as pd

def download_and_convert_to_excel(url, output_file):
    # Download the JSON data
    response = requests.get(url)
    data = response.json()

    # Convert the data into a DataFrame
    df = pd.json_normalize(data['pokemon'])

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

    print("Data downloaded and saved as", output_file)

# URL of the JSON data
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# Output file name
output_file = "pokedex.xlsx"

# Call the function to download and convert the data
download_and_convert_to_excel(url, output_file)


# In[ ]:





# In[ ]:





# In[ ]:




