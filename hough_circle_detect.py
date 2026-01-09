#import opencv
import cv2

#load in the picture
original_can = cv2.imread("original_can.png")

#grayscale
grey = cv2.cvtColor(original_can, cv2.COLOR_BGR2GRAY)

#find the circumference+center
processed_can = cv2.HoughCircles(image=grey, method=cv2.HOUGH_GRADIENT, dp=1, minDist=500, param1=50, param2=45, minRadius=1000, maxRadius=1300)

#extract the detected circle data
processed_can = processed_can[0]

#draw the processed circumference + center
for c in processed_can:
    x = int(c[0])
    y = int(c[1])
    r = int(c[2])
    cv2.circle(original_can, (x, y), r, (255, 150, 0), 11) #circumference
    cv2.circle(original_can, (x, y), 18, (0, 0, 255), -1)  #center

#display
cv2.imshow("processed circle", original_can)
cv2.waitKey(0)
cv2.destroyAllWindows()

# pseudocode:
# 1 load the image
# 2 convert the image to grayscale
# 3 use hough circle to detect circular shapes
# 4 extract the circle's data of the center and radius
# 5 draw the circumference and center on the original image
# 6 display the final result
