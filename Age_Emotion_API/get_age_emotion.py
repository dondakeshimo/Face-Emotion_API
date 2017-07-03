
# coding: utf-8

# In[8]:

import os
import sys
import requests
import json


# In[9]:

# set api url and make header
face_url = "https://westus.api.cognitive.microsoft.com/face/v1.0/detect"
emo_url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

face_headers = {
    "content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": "c1d3ab4f6c24425fb811813bf24c8a7f",
}
emo_headers = {
    "content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": "3c8a635a9b754dc2a5a48976222e25fd",
}

face_params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
}
emo_params = {}


# In[11]:

#argv = sys.argv
#if len(argv) == 1:
#    print("Usage: # python {} [filename]".format(argv[0]))
#    quit()
    
#image_url = argv[1]

image_url = "http://img.horipro.co.jp/wp-content/uploads/sites/17/2014/09/4efa1206c3ddde742caafee8af2a531e.jpg"
payload = {
    "url": image_url
}

face = requests.post(face_url, headers=face_headers, params=face_params, data=json.dumps(payload))
emo = requests.post(emo_url, headers=emo_headers, params=emo_params, data=json.dumps(payload))

print(face.text)
print(emo.text)


# In[21]:

face_dict = json.loads(face.text)[0]
emo_dict = json.loads(emo.text)[0]["scores"]

age = face_dict["faceAttributes"]["age"]
temp = max(emo_dict.items(), key=lambda x:x[1])
emotion = [temp[0], int(temp[1] * 100)]

print("I estimate that your age is {}, ".format(age))
print("and your emotion is [{0[0]}] with a {0[1]}% chance".format(emotion))


# In[ ]:



