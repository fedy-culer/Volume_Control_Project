import cv2
import mediapipe as mp
import time
cTime =0
pTime=0

class handDetector():
    def __init__(self,mode=False,maxHands=2,model_complexity=1,detectionCon =0.5 , trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.model_complexity = model_complexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,
               self.model_complexity,self.detectionCon,self.trackCon)
        self.mpDraw= mp.solutions.drawing_utils


    def findHands(self,img,draw =True):

        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks :
            for handlmks in self.results.multi_hand_landmarks:
                 if draw :
                    self.mpDraw.draw_landmarks(img,handlmks,self.mpHands.HAND_CONNECTIONS)

        return img
    def findPositions(self,img,handNo=0,draw=True):

       lmkList = []
       if self.results.multi_hand_landmarks:
           myhand=self.results.multi_hand_landmarks[handNo]

           for index, landmark in enumerate(myhand.landmark):
             height, width, channel = img.shape
             posX, posY = int(landmark.x * width), int(landmark.y * height)
             #print(id, posX, posY)
             lmkList.append([index, posX, posY])
             if draw:
                 cv2.circle(img, (posX, posY), 15, (0, 255, 255), cv2.FILLED)

       return lmkList

def main() :

    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector=handDetector()


    while True:
        success, img = cap.read()
        img=detector.findHands(img)
        lmkList=detector.findPositions(img)
        if len(lmkList) !=0 :
            print(lmkList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        text = "fps : " + str(int(fps))
        cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.imshow("img", img)
        cv2.waitKey(1)


if __name__ == "__main__" :
    main()
