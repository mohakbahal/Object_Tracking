import cv2
import numpy as np

def main():

    cap=cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret=False

    while ret:
        ret,frame=cap.read()

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        #Blue_Color_Tracking
        #low=np.array([100,50,50])
        #high=np.array([140,255,255])

        #Red_Color_Tracking
        low=np.array([0,100,100])
        high=np.array([10,255,255])

        image_mask = cv2.inRange(hsv,low,high)
        output = cv2.bitwise_and(frame,frame,mask=image_mask)

        cv2.imshow("Blue Object Tracker",output)
        cv2.imshow("Live Cam",frame)
        if cv2.waitKey(1)==27:
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    main()


