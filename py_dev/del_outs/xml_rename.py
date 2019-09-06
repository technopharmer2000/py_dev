import os
import sys
import xml.etree.ElementTree as ET


xml_dir = sys.argv[1]

xml_files = os.listdir(xml_dir)
xml_files.sort()

for file in xml_files:
    if file.endswith(".xml"):
        n=1

        tree = ET.parse(os.getcwd()+"/"+xml_dir+"/"+file)
        root = tree.getroot()

        for filename in root.findall("filename"):
            print (filename.tag, filename.text)

        for path in root.findall("path"):
            print (path.tag, path.text)