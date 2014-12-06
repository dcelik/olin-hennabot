import cv2
import numpy as np
import thresholding as th
import drawer as dw
import arduinocomms_start as ars
coords = [];
th.makeThresholdingWindow()
coords = dw.makeDrawingWindow()
print 'Coords:'
print coords
ars.startComms(coords)