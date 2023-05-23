#!/usr/bin/env python
# coding: utf-8

# In[36]:


import re

def count_parts_of_speech(text):
  

  parts_of_speech = {
    "verbs": 0,
    "nouns": 0,
    "pronouns": 0,
    "adjectives": 0
  }

  for word in text.split():
    if re.match(r"^[a-z]+(s|ed|ing)$", word):
      parts_of_speech["verbs"] += 1
    elif re.match(r"^[a-z]+$", word):
      parts_of_speech["nouns"] += 1
    elif re.match(r"^[a-z]+(-'s)$", word):
      parts_of_speech["pronouns"] += 1
    elif re.match(r"^[a-z]+(-e|-y)$", word):
      parts_of_speech["adjectives"] += 1

  return parts_of_speech


if __name__ == "__main__":
  text = "The quick brown fox jumps over the lazy dog."
  parts_of_speech = count_parts_of_speech(text)
  print(parts_of_speech)


# In[37]:


def count_parts_of_speech(text):
  
 parts_of_speech = {
    "verbs": 0,
    "nouns": 0,
    "pronouns": 0,
    "adjectives": 0
  }

  for word in text.split():
    if word.endswith("s") or word.endswith("ed") or word.endswith("ing"):
      parts_of_speech["verbs"] += 1
    elif word.isalpha():
      parts_of_speech["nouns"] += 1
    elif word.endswith("-'s"):
      parts_of_speech["pronouns"] += 1
    elif word.endswith("-e") or word.endswith("-y"):
      parts_of_speech["adjectives"] += 1

  return parts_of_speech


if __name__ == "__main__":
  text = "The quick brown fox jumps over the lazy dog."
  parts_of_speech = count_parts_of_speech(text)
  print(parts_of_speech)


# In[ ]:





# In[ ]:





# In[ ]:




