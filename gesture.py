import cv2
cap = cv2.VideoCapture(0)

X1 = 160
Y1 = 140
X2 = 400
Y2 = 360

while True:
    _, FrameImage = cap.read()
    FrameImage = cv2.flip(FrameImage, 1)
    cv2.imshow("", FrameImage)
    cv2.rectangle(FrameImage, (X1, Y1), (X2, Y2), (0, 255, 0), 1)
    ROI = FrameImage[Y1:Y2, X1:X2]
    ROI = cv2.resize(ROI, (64, 64))
    ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    _, output = cv2.threshold(ROI, 100, 255, cv2.THRESH_BINARY)  # adjust brightness
    SHOWROI = cv2.resize(ROI, (256, 256))
    _, output2 = cv2.threshold(SHOWROI, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", output2)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('q'):  # esc key
        break

cap.release()
cv2.destroyAllWindows()
