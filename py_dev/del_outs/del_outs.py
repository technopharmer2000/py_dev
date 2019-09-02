import os
import sys

args = sys.argv

str_dir = args[1]
con_dir = args[2]

def decon_dir(str_dir,con_dir):
    str_list = []
    for file in os.listdir(str_dir):
        file = file.split('.')[0]
        str_list.append(file)
        #print (str_list)

    for i in os.listdir(con_dir):
        if i.split('.')[0] in str_list:
            pass
        else:
            os.remove(os.getcwd()+"/"+con_dir+i)
            print (i+" removed")


decon_dir(str_dir, con_dir)
