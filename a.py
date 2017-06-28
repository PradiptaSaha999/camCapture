import cv2

cap=cv2.VideoCapture(0)

i=0;

while(True):
## Capture frame-by-frame
    ret, frame = cap.read()
##    sidge= cap.get(3)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame


    
    cv2.imshow("frame",gray)
##    print(sidge)
    if cv2.waitKey(1) & 0xFF == ord("s"):
        i=i+1
        cv2.imwrite("SAD.jpg",frame)
    elif cv2.waitKey(1) & 0xFF == ord("q"):
        break
## When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
