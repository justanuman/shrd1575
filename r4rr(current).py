import cognitive_face as CF
import requests
import cv2
import os , os.path
id1= ["vadim","serega"]
massid = ["96f33a53-6e6e-4b39-8527-9134200fd35c","c418e10d-fe22-4481-8ed0-dc6383d7c553"]

SUBSCRIPTION_KEY = '601843bed46445f6a879303f84e39e73'   
CF.Key.set(SUBSCRIPTION_KEY)
BASE_URL = 'https://northeurope.api.cognitive.microsoft.com/face/v1.0'  
CF.BaseUrl.set(BASE_URL)
PERSON_GROUP_ID = 'persons'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
vidcap = cv2.VideoCapture("serega.mp4")
print (vidcap.read())
success,image = vidcap.read()
coun = 0
success = True
while success:
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("frame%d.png" % coun, image)     
    coun += 1
st="C:\\Users\\user\\Desktop\\uu\\frame"
en=".png"
count = 0
mid= str(count)
print(st+mid+en)
fect = 0 
fe = 0
while coun!=count :
    fect += 1
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
                fe +=1
                idf= str(identified_faces[i])
                idf= idf.split()
                idfi = idf[4]
                idfix = idfi[1:37]
                for m in range(2):
                    if idfix == massid[m]:
                        idfix= id1[m]
                file = open("id"+str(fect)+str(fe)+'.txt',"w")
                file.write(idfix)
                print(idfix)
                file.close()
