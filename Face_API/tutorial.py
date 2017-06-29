
# coding: utf-8

# In[1]:

import cognitive_face as CF


# In[22]:

KEY = 'c1d3ab4f6c24425fb811813bf24c8a7f'
CF.Key.set(KEY)


# In[23]:

img_url = "https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg"
result = CF.face.detect(img_url)
print(result)


# In[ ]:



