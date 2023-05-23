#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import pandas as pd

def download_and_convert_to_csv(url, output_file):
    # Download the JSON data
    response = requests.get(url)
    data = response.json()

    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

    print("Data downloaded and saved as", output_file)

# URL of the JSON data
url = "https://data.nasa.gov/resource/y77d-th95.json"

# Output file name
output_file = "nasa_data.csv"

# Call the function to download and convert the data
download_and_convert_to_csv(url, output_file)


# In[ ]:





# In[ ]:





# In[ ]:




