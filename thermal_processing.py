#!/usr/bin/env python

import cv2, math
import numpy as np
from matplotlib import pyplot as plt

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def main():
   video = cv2.VideoCapture("videos/a1.mp4")

   i = 0

   hands = []

   while video.isOpened():
      ret, frame = video.read()

      if not ret:
         break

      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      print('{} {}'.format(i, ret))
      i += 1

      # apply median filter
      med = cv2.medianBlur(gray, 5)

      # apply otsu's
      ret, otsu = cv2.threshold(med, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
         
      # find contours (note: this modifies the image so we create a copy)
      contours,hierarchy = cv2.findContours(otsu.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      
      # find contour with largest area, a.k.a. the hand
      handContour = max(contours, key=lambda c:cv2.contourArea(c))

      # create binary image of the hand
      handBinary = otsu.copy()
      handBinary.fill(0)
      cv2.drawContours(handBinary, [handContour], 0, (255,255,255), -1)
      handBinary = np.array(handBinary == 255, dtype=int)

      hands.append(handBinary)

      if i == 30:

         allHands = np.logical_or.reduce(hands)
         allHands = np.array(allHands, dtype=int)
         searchSpace = np.subtract(handBinary, allHands)
         #searchSpace = np.array(searchSpace == 1, dtype=int) 

         print(allHands[482][65])
         print(handBinary[482][65])
         print(searchSpace[482][65])
         
         plt.subplot(121)
         plt.imshow(allHands, cmap='gray')
         plt.title("Combining previous hands")
         plt.xticks([]), plt.yticks([])

         plt.subplot(122)
         plt.imshow(searchSpace, cmap='gray')
         plt.title("Heat trace search space")
         plt.xticks([]), plt.yticks([])

         plt.show()

         '''
         plt.subplot(121),plt.imshow(med, cmap='gray'),plt.title('Median Filtering')
         plt.xticks([]), plt.yticks([])
         plt.subplot(122),plt.imshow(thr, cmap='gray'),plt.title("Otsu's Thresholding")
         plt.xticks([]), plt.yticks([])
         plt.show()'''


   video.release()

if __name__ == "__main__":
   main()
