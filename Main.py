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

cv2.imshow("Basic AutoPilot AI", openImg)
cv2.waitKey()