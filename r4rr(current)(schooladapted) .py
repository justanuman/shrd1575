import cognitive_face as CF
import requests
import cv2
import os , os.path
file = open("id"+'.txt',"w")
id1= ["stepab","seregam","vadim","serega"]
massid = ["02e66b12-b760-4320-925e-da78489a38ea","3951687f-9b54-4093-ac1a-4d5ec8f49e70","42b0407a-b27c-480b-b20a-f619888b8594","a0ca509e-a0c3-4334-891f-1566ad7097ba"]
nam = []
SUBSCRIPTION_KEY = 'this key is invalid'   
CF.Key.set(SUBSCRIPTION_KEY)
BASE_URL = 'https://northeurope.api.cognitive.microsoft.com/face/v1.0'  
CF.BaseUrl.set(BASE_URL)
PERSON_GROUP_ID = 'persons'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
vidcap = cv2.VideoCapture("sv.mp4")
print (vidcap.read())
success,image = vidcap.read()
coun = 0
success = True
while success:
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("frame%d.png" % coun, image)     
    coun += 1
st="C:\\Users\\locadmin\\Desktop\\shrd\\frame"
en=".png"
count = 0
mid= str(count)
print(st+mid+en)

while coun!=count :
    mid= str(count)
    print(mid)
    count +=1
    response = CF.face.detect(st+mid+en)
    print(response)
    if os.path.exists(st+mid+en):
        img_url = st+ mid +en
        print(img_url) 
        os.remove(st+mid+en)
        if response != []:
            face_ids = [d['faceId'] for d in response]
            identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
            for i in range(len(identified_faces)):
                idf= str(identified_faces[i])
                idf= idf.split()
                if len(idf)>4:
                    idfi = idf[4]
                    idfix = idfi[1:37]
                    for m in range(len(massid)):
                        if idfix == massid[m]:
                            idfix= id1[m]
                            if nam.count(str(idfix)) <1:
                                nam.append(idfix)
                                file = open("id"+'.txt',"w")
                                file.write(str(nam))
                                file.close()
                else:
                    break

