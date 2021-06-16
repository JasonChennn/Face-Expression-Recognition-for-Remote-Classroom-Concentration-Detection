# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 20:17:14 2021

@author: I5-10400
"""

import os
import cv2
import imutils
import dlib
import numpy as np
from imutils.face_utils import FaceAligner
from imutils import face_utils

predictor_path = "shape_predictor_5_face_landmarks.dat"

dirInputPath = "input"
dirOutputPath = "output"
files = os.listdir(dirInputPath)
for f in files:
  # 產生檔案的絕對路徑
  fullpath = os.path.join(dirInputPath, f)
  outpath = os.path.join(dirOutputPath, f)
  # 判斷 fullpath 是檔案還是目錄
  try:
      if os.path.isfile(fullpath):
        print("檔案：", fullpath)
        if fullpath == "input\painful_00000.jpg": 
            continue
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path)
        fa = FaceAligner(predictor, desiredFaceWidth=256)
        image = cv2.imread(fullpath)
        image = imutils.resize(image, width=800)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 2)
        for rect in rects:
                (x, y, w, h) = face_utils.rect_to_bb(rect)
                faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
                #faceAligned = fa.align(image, gray, rect)
                resize = cv2.resize(faceOrig, (48, 48), interpolation=cv2.INTER_AREA)
                cv2.imwrite(outpath, resize)
  except:
      continue

cv2.waitKey(0)