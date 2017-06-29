
# coding: utf-8

# In[3]:

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': 'ac434e7218f0481e829dc57046079142',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
})

try:
    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
    #   URL below with "westus".
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{\"url\":\"http://img.horipro.co.jp/wp-content/uploads/sites/17/2014/09/4efa1206c3ddde742caafee8af2a531e.jpg\"}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


# In[2]:

import sys
import requests


url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'c1d3ab4f6c24425fb811813bf24c8a7f',
}
params = {
    'returnFaceId': 'true',  # The default value is true.
    'returnFaceLandmarks': 'false', # The default value is false.
    'returnFaceAttributes': 'age,gender', # age, gender, headPose, smile, facialHair, and glasses.
}
if __name__ == '__main__':

    r = requests.post(url ,headers = headers,params = params,data = open("1643_fukada_kyoko.jpg",'rb'))

    print(r.text)


# In[ ]:



