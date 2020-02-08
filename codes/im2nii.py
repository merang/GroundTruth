

import numpy as np
import nibabel as nib
import os
import cv2
import glob


# images path
im_jpg = r' Users/user/github/HSYAA_GT/100IM_max3Cells_tiff'

#im_jpg = r'./100IM_max3Cells_tiff'

#im_jpg = r'/Users/user/github/HSYAA/python/convert_im2nii/data_bw'


# function to covert jpg to nii format
def save_as_nii(y, savename):
    y_nii = nib.Nifti1Image(y.astype(np.uint8), np.eye(4))
    nib.save(y_nii, savename + '.nii')



# load images
data_path = os.path.join(im_jpg,'*.tif')
files = glob.glob(data_path)
data = []
count=1


for f1 in files:

    img = cv2.imread(f1)
    filename='./%s'%f1
    save_as_nii(img, filename)

    # data.append(img)
    count=count+1
    print('{} image converted to nii format '.format(f1))
    print('Finished')
