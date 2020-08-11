import cv2 as c

vid = c.VideoCapture(0)

while True:
    ret,frame = vid.read()
    c.imshow('Webcam',frame)
    if c.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
c.destroyAllWindows()
