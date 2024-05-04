import cv2
import math
from random import *


#*** import demo car image file to test detection
initImg = "demoCarImg.jpg"
#*** import pretrained xml to train processor how to detect cars accuratley {machine learning}
pretrainedCars = "carsDataset.xml"
#*** import pretrained xml to train processor how to detect cars accuratley {machine learning}
pretrainedPedestrains = "haarcascadePedestrianDataSet.xml"