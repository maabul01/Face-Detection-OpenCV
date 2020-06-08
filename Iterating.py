from scipy import ndimage, misc
import numpy as np
import os
import cv2

def main():
    outPath ="C:\\Users\\Maabul Quddus\\Documents\\Co Curricular\\Python Projects\\Spyder\\Out"
    path = "C:\\Users\\Maabul Quddus\\Documents\\Co Curricular\\Python Projects\\Spyder\\DataSets"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_rotate = ndimage.imread(input_path)
        
        
        #whatever functionality you have to give is 
        rotated=cv2.imwrite(image_path,0)
        
        
        
        #save images as rotated
        # create full output path, 'example.jpg' 
        # becomes 'rotate_example.jpg', save the file to disk
        fullpath = os.path.join(outPath, 'rotated_'+image_path)
        misc.imsave(fullpath, rotated)

if __name__ == '__main__':
    main()