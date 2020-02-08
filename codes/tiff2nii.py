
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 15:11:29 2019

@author: Meran

"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


tiff to nii format 

Run : python tiff2nii.py
Output: it saves in the same folder and labels with nii formate 

"""


import numpy as np
import nibabel as nib
import os
import cv2
import glob


# Image path

path_in = r'./../650IM_512x512_CUBIC_tiff'
path_out = r'./../650IM_512x512_CUBIC_nii_v1'



# function to covert jpg to nii format
def save_as_nii(y, savename):
    y_nii = nib.Nifti1Image(y.astype(np.uint8), np.eye(4))
    nib.save(y_nii, savename + '.nii')



# load images
data_path = os.path.join(path_in,'*.tif')
files = glob.glob(data_path)
data = []
count=1




# Rotation 
rotate = cv2.ROTATE_90_CLOCKWISE
#rotate = cv2.ROTATE_90_COUNTERCLOCKWISE
#rotate = cv2.ROTATE_180


for f1 in files:

    img = cv2.imread(f1)
    
    #img = cv2.rotate(img, rotate)
    
    filename='./%s'%f1
    lab=filename[32:-4]
    label= os.path.join(path_out,lab)
  
    save_as_nii(img, label)
    

    # data.append(img)
    count=count+1
    print('{} image converted to nii format '.format(f1))
    print('Finished')
