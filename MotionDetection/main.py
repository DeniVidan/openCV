import cv2
import numpy as np

static_back = None

cap = cv2.VideoCapture('http://192.168.1.7:8080/video')
cap.set(10, 200)
while(cap.isOpened()):
    ret, img = cap.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if static_back is None:
        static_back = grey
        continue
    diff_frame = cv2.absdiff(static_back, grey)

    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cnts,_ = cv2.findContours(thresh_frame.copy(),
                              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        motion = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        #green rect around moving obj
        t = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(t, "Motion detect", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)
        crop = img[y:y+h, x:x+w]
        cv2.imwrite("output/object_" + str("aaa") + ".png", crop)
    cv2.imshow("Contour", img)

    k = cv2.waitKey(10)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
