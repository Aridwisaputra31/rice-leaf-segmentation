import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# ==========================================================
# NOTE:
# Please change the folder paths below according to the
# image storage location on your local computer.
# Example (Windows): D:\YourFolder\Subfolder
# ==========================================================

ddir=os.listdir(r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking3')
folderFile=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking3'
folsave=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking4'

for i in ddir:
    if i.endswith('jpg'):
        print(i)
        nfol_hasil=os.path.join(folderFile,i)
        img_0 = cv2.imread(nfol_hasil) #RGB
        img_rgb=cv2.cvtColor(img_0, cv2.COLOR_BGR2RGB)
        img_lab2=cv2.cvtColor(img_0, cv2.COLOR_BGR2HSV) #convert citra ke HSV
        lower_green=np.array([20,0, 0],dtype=np.uint8) #lab
        upper_green=np.array([255,255,255],dtype=np.uint8) #lab

        mask=cv2.inRange(img_lab2,lower_green,upper_green)
        
        kernel1 = np.ones((7,7),np.uint8)
        opening1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)        
        
        iterasi=5
        kernel = np.ones((3,3),np.uint8)
        dilated = cv2.dilate(opening1,kernel,iterations = iterasi)

        hasil_rgb=cv2.bitwise_and(img_rgb,img_rgb, mask=dilated)

        parts = i.split('_')
        nf_hasil1 = "Hasil4_" + '_'.join(parts[1:])
        nfol_hasil1=os.path.join(folsave,nf_hasil1)
        plt.imsave(nfol_hasil1, hasil_rgb)
