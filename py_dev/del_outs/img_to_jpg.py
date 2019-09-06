import os
import sys

dir = sys.argv[1]

for file in os.listdir(dir):
    if file.endswith(".jpg"):
        pass
    else:
        os.remove(os.getcwd() + "/" + dir +"/"+ file)
        print (file+ " removed")


