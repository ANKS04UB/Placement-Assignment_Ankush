#!/usr/bin/env python
# coding: utf-8

# In[13]:


from collections import Counter

def is_valid_string(string):
    # Count the frequency of each character
    char_counts = Counter(string)

    # Count the frequency of frequencies
    freq_counts = Counter(char_counts.values())

    # If there is only one frequency, it is a valid string
    if len(freq_counts) == 1:
        return "YES"

    # If there are more than two frequencies, it is not a valid string
    if len(freq_counts) > 2:
        return "NO"

    # If there are exactly two frequencies
    freq_list = list(freq_counts.items())

    # If one frequency occurs only once, check if removing one character with that frequency makes it valid
    if freq_list[0][1] == 1:
        if freq_list[0][0] == 1:
            return "YES"
        elif freq_list[0][0] - 1 == freq_list[1][0]:
            return "YES"

    # If one frequency occurs only once, check if removing one character with that frequency makes it valid
    if freq_list[1][1] == 1:
        if freq_list[1][0] == 1:
            return "YES"
        elif freq_list[1][0] - 1 == freq_list[0][0]:
            return "YES"

    # If none of the conditions above are satisfied, it is not a valid string
    return "NO"

input_string = input("Enter a string: ")
result = is_valid_string(input_string)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:




