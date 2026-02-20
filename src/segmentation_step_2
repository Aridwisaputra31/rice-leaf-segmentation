import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

ddir=os.listdir(r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking1')
#print(ddir)
folderFile=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking1'
folsave=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking2'

for i in ddir:
    if i.endswith('jpg'):
        print(i)
        nfol_hasil=os.path.join(folderFile,i)
        #baca citra dengan format RGB agar tampilan cocok dengan matplotlib
        img_0 = cv2.imread(nfol_hasil) #RGB
        img_rgb=cv2.cvtColor(img_0, cv2.COLOR_BGR2RGB)
        img_hsv=cv2.cvtColor(img_0, cv2.COLOR_BGR2HSV)
        
        #tentukan range nilai piksel untuk mask
        lower_green=np.array([21,30,48],dtype=np.uint8) #lab
        upper_green=np.array([73,238,236],dtype=np.uint8) #S 238 jgn di ubah
        mask=cv2.inRange(img_hsv,lower_green,upper_green)
        
        iterasi=6
        kernel = np.ones((6,6),np.uint8)
        dilated = cv2.dilate(mask,kernel,iterations = iterasi)
        
        kernel1 = np.ones((10,10),np.uint8)
        closing1 = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel1)
        
        iterasi=3
        kernel1 = np.ones((3,3),np.uint8)
        eroded1 = cv2.erode(closing1, kernel1, iterations=iterasi)
        
        hasil_rgb=cv2.bitwise_and(img_rgb,img_rgb, mask=eroded1)

        
        parts = i.split('_')
        nf_hasil1 = "Hasil2_" + '_'.join(parts[1:])
        nfol_hasil1=os.path.join(folsave,nf_hasil1)
        plt.imsave(nfol_hasil1, hasil_rgb)
