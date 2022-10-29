import cognitive_face as CF
import requests
import cv2
import os , os.path

#KEY = 'this key is even more invalid'   
SUBSCRIPTION_KEY = 'this key is invalid'   
CF.Key.set(SUBSCRIPTION_KEY)
BASE_URL = 'https://northeurope.api.cognitive.microsoft.com/face/v1.0'  
CF.BaseUrl.set(BASE_URL)
PERSON_GROUP_ID = 'persons'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
#CF.person_group.create(PERSON_GROUP_ID, 'Known Persons')

#CF.person_group.create(PERSON_GROUP_ID, 'persons')
name = "vadim"
user_data = '10 v klass'
response = CF.person.create(PERSON_GROUP_ID, name, user_data)

# Get person_id from response
person_id = response['personId']
CF.person.add_face('frame8.png', PERSON_GROUP_ID, person_id)

CF.person_group.train(PERSON_GROUP_ID)
response = CF.person_group.get_status(PERSON_GROUP_ID)
status = response['status']

response = CF.face.detect('frame9.png')
face_ids = [d['faceId'] for d in response]

identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
print (identified_faces)
#if str(identified_faces).count("confidence")!=0:
#    print((str(identified_faces).split())[10])
#    perc= (str(identified_faces).split())[10]
#    print(perc[0:len(perc)-4])
#    per =perc[0:len(perc)-4]
#    if float(per) >0.7: print("yes")
#    else:print("no")
#else:print("net")
