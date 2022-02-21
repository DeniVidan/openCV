import cv2

#print("Before URL")
cap = cv2.VideoCapture('http://192.168.1.7:8080/video')


#print("After URL")

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    resize = cv2.resize(frame, (1280, 720))
    #print('About to show frame of Video.')
    cv2.imshow("Capturing", resize)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
