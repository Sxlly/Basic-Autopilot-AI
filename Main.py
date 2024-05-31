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

cv2.imshow("Basic AutoPilot AI", bnwImage)
cv2.waitKey()

