
import cv2
import os


# input image extension
extensions= ["PNG","TIF","JPG"]


# outout image extension 
ext="jpg"

# add output imagse size to label
si= "_512x512."

# Dimension 
height= 512
width= 512



# available  interpolation 

#   INTER_NEAREST - a nearest-neighbor interpolation

#   INTER_LINEAR - a bilinear interpolation (used by default)

#   INTER_AREA - resampling using pixel area relation. 
#   It may be a preferred method for image decimation,
#   as it gives moire’-free results. But when the image is zoomed,
#   it is similar to the INTER_NEAREST method.
  
#   INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood

#   INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood


#setup interpolation
resize_method = cv2.INTER_NEAREST


DIR = os.path.dirname(os.path.realpath(__file__))


# path for input image
#path_in= os.path.abspath(path + "/../100IM_max3Cells_60x60_jpg/.")

path_in = DIR + '/../100IM_max3Cells_60x60_jpg/'


#path_in = DIR + '/../'


#path for output images
#path_out= os.path.abspath(path+ "/../100IM_max3Cells_512x512_tiff_LANCZOS4/.")

#path_out = DIR + '/../100IM_max3Cells_512x512_tiff_NEAREST/'


path_out = DIR + '/../100IM_max3Cells_512x512_jpg/'


count=1
if __name__ == "__main__":

    for f in os.listdir(path_in):
        if os.path.isfile(os.path.join(path_in ,f)):
            
            f_text, f_ext= os.path.splitext(f)
            
            f_ext= f_ext[1:].upper()
            
            if f_ext in extensions:
                #print (f)
                
                image = cv2.imread(os.path.join(path_in ,f))
                image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
                
                dim=(width,height)
                img = cv2.resize(image, dim, interpolation= resize_method)
            
                # remove some chracters from label
                label=f[:35]
                #label=f
                
                # new label
                im_label= (label+si+ext)
                cv2.imwrite(os.path.join(path_out,im_label), img)
                
                print('')
                print('Image :' , count )
                print('Old Image Size:',image.shape)
                print ('Old Label:',f)
                print('New Image Size:',img.shape)
                print('New Label:',im_label)
                
                count =count +1