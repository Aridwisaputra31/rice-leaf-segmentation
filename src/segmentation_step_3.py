import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


ddir=os.listdir(r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking2')
folderFile=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking2'
folsave=r'D:\File Photo\Ari\SAMSUNG 1\HST 60\Baris 6 hst 60 ari\Equalisasi\Hasil_Clahe\Masking3'

for i in ddir:
  if i.endswith('jpg'):
        print(i)
        nfol_hasil=os.path.join(folderFile,i)
        img_0 = cv2.imread(nfol_hasil)
        img_rgb=cv2.cvtColor(img_0, cv2.COLOR_BGR2RGB)

        img_lab1=cv2.cvtColor(img_0, cv2.COLOR_BGR2LAB) 
        lower_green=np.array([3,0,2],dtype=np.uint8) 
        upper_green=np.array([255,115,255],dtype=np.uint8) 

        mask1=cv2.inRange(img_lab1,lower_green,upper_green)
        img_lab2=cv2.cvtColor(img_0, cv2.COLOR_BGR2LAB) #convert citra ke HSV
        lower_green=np.array([3,105,160],dtype=np.uint8) #lab
        upper_green=np.array([255,135,255],dtype=np.uint8) #lab
        
        mask2=cv2.inRange(img_lab2,lower_green,upper_green)
        mask3=cv2.bitwise_or(mask1,mask2)

        img_yuv=cv2.cvtColor(img_0, cv2.COLOR_BGR2YUV) #convert citra ke HSV
        lower_green=np.array([0,50,150],dtype=np.uint8) #lab
        upper_green=np.array([255,255,255],dtype=np.uint8) #lab
        mask4=cv2.inRange(img_yuv,lower_green,upper_green)
        mask5=cv2.bitwise_or(mask3,mask4)
        
        iterasi=3
        kernel = np.ones((3,3),np.uint8)
        dilated = cv2.dilate(mask5,kernel,iterations = iterasi)
        
        iterasi=2
        kernel1 = np.ones((3,3),np.uint8)
        eroded1 = cv2.erode(dilated, kernel1, iterations=iterasi)
        hasil_rgb=cv2.bitwise_and(img_rgb,img_rgb, mask=eroded1)

        parts = i.split('_')
        nf_hasil1 = "Hasil3_" + '_'.join(parts[1:])
        nfol_hasil1=os.path.join(folsave,nf_hasil1)
        plt.imsave(nfol_hasil1, hasil_rgb)
