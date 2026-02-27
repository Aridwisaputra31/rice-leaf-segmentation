import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import os

# ==========================================================
# NOTE:
# Please change the folder paths below according to the
# image storage location on your local computer.
# Example (Windows): D:\YourFolder\Subfolder
# ==========================================================

ddir=os.listdir(r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe')
folderFile=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe'
folsave=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking1'

for i in ddir:
  #print(folmasking)
    if i.endswith('jpg'):
        print(i)
        nfol_hasil=os.path.join(folderFile,i)
        img = cv2.imread(nfol_hasil) #RGB
        scale_percent = 50
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dsize = (width, height)
        img_0=cv2.resize(img, dsize)
        
        img_rgb=cv2.cvtColor(img_0, cv2.COLOR_BGR2RGB)
        img_hsv= cv2.cvtColor(img_0, cv2.COLOR_BGR2HLS)
        
        lower_green=np.array([18,28,43],dtype=np.uint8) 
        upper_green=np.array([79,198,207],dtype=np.uint8) 
        mask=cv2.inRange(img_hsv,lower_green,upper_green)
        
        iterasi=5
        kernel = np.ones((3,3),np.uint8)
        dilated = cv2.dilate(mask,kernel,iterations = iterasi)
        
        kernel1 = np.ones((30,30),np.uint8)
        closing1 = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel1)
        
        iterasi=1
        kernel1 = np.ones((3,3),np.uint8)
        eroded1 = cv2.erode(closing1, kernel1, iterations=iterasi)

        hasil_rgb=cv2.bitwise_and(img_rgb,img_rgb, mask=eroded1)
        
        parts = i.split('_')
        nf_hasil1 = "Hasil1_" + '_'.join(parts[0:])
        nfol_hasil1=os.path.join(folsave,nf_hasil1)
        plt.imsave(nfol_hasil1, hasil_rgb)
