import cv2

cam = cv2.VideoCapture(0)
ret, prevFrame = cam.read()

def getNextFrame(vidObj):
    """Takes in the VideoCapture object and reads the next frame, returning one that is half the size
    (Comment out that line if you want fullsize)."""
    ret, frame = vidObj.read()
    # frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    return frame

while True:
    currFrame = getNextFrame(cam)
    imgray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contrs, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(currFrame, contrs, -1, (0, 255, 0), 3)

    diff = cv2.absdiff(prevFrame, currFrame)
    cv2.imshow("Motion", diff)

    x = cv2.waitKey(20)
    c = chr(x & 0xFF)
    if c == "q":
        break
    prevFrame = currFrame

cam.release()
cv2.destroyAllWindows()