import sys
import cv2 as cv
import numpy as np

def main(argv):
    
    default_file = 'Bubbles2.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

    # Add grayscale
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray,(9,9),0)
    cv.imshow("Original image", blurred)
    
    #Find circles
    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, dp = 0.9, minDist = 20,
                               param1=50, param2=20,
                               minRadius=2, maxRadius=30)

    bubblesCount = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            #Circle center
            #cv.circle(src, center, 1, (100, 100, 100), 3)
            if center:
                bubblesCount += 1
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 2)
    
    imageTitle = "Detected bubbles: %d" % bubblesCount
    cv.imshow(imageTitle, src)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])