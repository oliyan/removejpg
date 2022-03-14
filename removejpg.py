# Remove JPG is a handy little python script used to remove the unwanted JPGs from the camera media.

import os

allraw = ('.NEF', '.CR2', '.CR3', '.ARW')
thispath = input("Enter the location you want to clean: ")

n = 0
# for every file in this directory
for thisfile in os.listdir(thispath):

    # if the file name ends with a JPG
    if ((os.path.splitext(thisfile))[1]).lower() == ".jpg":

        # check whether any raw file is present too
        for thisraw in allraw:
            if os.path.exists(((os.path.splitext(thisfile))[0])+thisraw):
            
                # if yes, then remove the jpg file
                os.remove(thisfile) 
