import cognitive_face as CF
import requests
import cv2
import os , os.path


SUBSCRIPTION_KEY = '601843bed46445f6a879303f84e39e73'   
CF.Key.set(SUBSCRIPTION_KEY)
BASE_URL = 'https://northeurope.api.cognitive.microsoft.com/face/v1.0/'  
CF.BaseUrl.set(BASE_URL)
PERSON_GROUP_ID = 'persons'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
print(CF.person.lists(PERSON_GROUP_ID))