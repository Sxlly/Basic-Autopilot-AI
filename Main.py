import cv2
import math
from random import *


#*** import demo car image file to test detection
initImg = "freewaypeebreak.jpeg"
#*** import pretrained xml to train processor how to detect cars accuratley {machine learning}
pretrainedCars = "carsDataset.xml"
#*** import pretrained xml to train processor how to detect cars accuratley {machine learning}
pretrainedPedestrains = "haarcascadePedestrianDataSet.xml"


#*** create opencv image
openImg = cv2.imread(initImg)

#*** convert image to black and white for reading
bnwImage = cv2.cvtColor(openImg, cv2.COLOR_BGR2GRAY)

#*** train car_tracker variable to indentify a car accuratley through reading pre made xml car dataset
carTracker = cv2.CascadeClassifier(pretrainedCars)

#*** detect cars in bnw image
cars = carTracker.detectMultiScale(bnwImage)

print(cars)

car1 = cars[0]
(x,y,w,h) = car1
cv2.rectangle(openImg, (x,y), (x+w, y+h), (0,255,0), 2)


cv2.imshow("Basic AutoPilot AI", openImg)
cv2.waitKey()


