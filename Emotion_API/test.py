
# coding: utf-8

# In[1]:

import requests


url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '3c8a635a9b754dc2a5a48976222e25fd',
}

params = {}

if __name__ == '__main__':

    r = requests.post(url ,headers = headers,params = params,data = open("fukada_test.jpg",'rb'))

    print(r.text)


# In[4]:

import requests
import json

url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
image_url = "http://img.horipro.co.jp/wp-content/uploads/sites/17/2014/09/4efa1206c3ddde742caafee8af2a531e.jpg"
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '3c8a635a9b754dc2a5a48976222e25fd',
}

params = {}

payload = {
    "url": image_url,
}

if __name__ == '__main__':

    r = requests.post(url ,headers = headers,params = params,data = json.dumps(payload))

    print(r.text)


# In[ ]:



