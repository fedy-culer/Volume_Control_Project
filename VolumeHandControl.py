import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast ,POINTER

####################################
wCam , hCam= 700 ,480
####################################
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0
detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange =volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0, None)
vol =0
volBAR=400
volpercent=0
while True:
    success,img=cap.read()
    img=detector.findHands(img)
    listpos=detector.findPositions(img,draw=False)
    if len(listpos) !=0 :
      #  print(listpos[4],listpos[8])

        x1,y1=listpos[4][1],listpos[4][2]
        x2, y2 = listpos[8][1], listpos[8][2]

        cv2.circle(img,(x1,y1),15,(0,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(0,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(100,100,2),3)
        cv2.circle(img,(((x1+x2)//2),((y1+y2)//2)),13,(255,0,0),cv2.FILLED)

        length =math.hypot((x2-x1),(y2-y1))
        print(length)
        vol = np.interp(length,[50,200],[-63,0])
        volBAR = np.interp(length, [50, 200], [400, 150])
        volpercent = np.interp(length, [50, 200], [0, 100])

    #print(vol)
        volume.SetMasterVolumeLevel(vol, None)

        if  length<50:
            cv2.circle(img, (((x1 + x2) // 2), ((y1 + y2) // 2)), 13, (255, 255, 255), cv2.FILLED)
    # hand range      entre 240 et 5
    # volume range (-63.5, 0.0, 0.5)
    cv2.rectangle(img,(50,150),(85,400),(128,128,120),3)
    cv2.rectangle(img,(50,int(volBAR)),(85,400),(0,0,0),cv2.FILLED)
    cv2.putText(img, f'{int(volpercent)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255,255), 3)


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS = {int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)

    cv2.imshow("output",img)
    cv2.waitKey(1)