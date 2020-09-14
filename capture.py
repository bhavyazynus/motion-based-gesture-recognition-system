import cv2 as c

vid = c.VideoCapture('http://192.168.1.107:8080/video')

while True:
    ret,frame = vid.read()
    c.imshow('Webcam',frame)
    if c.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
c.destroyAllWindows()
