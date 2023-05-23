#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import Counter

def find_highest_frequency_word_length(string):
    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Find the highest frequency
    max_frequency = max(word_counts.values())

    # Find the length of the word with the highest frequency
    highest_frequency_word_length = len(max(word_counts, key=len))

    return highest_frequency_word_length

# Example usage
input_string = input("Enter a sentence: ")
result = find_highest_frequency_word_length(input_string)
print("Length of the highest-frequency word:", result)


# In[ ]:




