
import sys
from PIL import Image
import os

image_file_list = os.listdir(sys.argv[1])
image_file_list.sort()
for file in image_file_list:
    #try:
        image = Image.open(file)
        print (file)
        image.save(file, jpg)
            #print(file + " - invalid - " + str(file_type))
            #cv2.imwrite(file, image)
    #except IOError:

       # print ("noload")
    #sys.exit(1)

