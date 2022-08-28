#!/usr/bin/python

# pip install lxml

# reference: https://github.com/yukkyo/voc2coco

import os
import json
import xml.etree.ElementTree as ET
import glob
from PIL import Image


START_BOUNDING_BOX_ID = 0

PRE_DEFINE_CATEGORIES = {"table": 0 }

# Assign images id according to their filenames
def get_id_as_int(filename):
    try:
        idx = filename.strip('.jpg').split("_")[-1]
        '''filename = filename.replace("\\", "/")
        filename = os.path.splitext(os.path.basename(filename))[0]
        idx = filename[7:12]'''
        return int(idx)
    except:
        raise ValueError("Filename %s is supposed to be an integer." % (idx))


def convert(xml_files, json_file, data_path, data_path_img):
   
    json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    for xml_file in xml_files:
        # Read the structure of XML files
        xml_file_path = data_path+"/"+xml_file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        filename = xml_file.strip('xml')+'jpg'
    
        # The image id must be a number
        image_id = get_id_as_int(filename)
       
        # Get the width and height of images
        im = Image.open(data_path_img+"/"+filename)
        width, height = im.size
        image = {
            "file_name": filename,
            "height": height,
            "width": width,
            "id": image_id,
        }
        print(image)
        json_dict["images"].append(image)
        for object in root.iter('object'):
            category = str(object.find('name').text)
            if category == 'table':
                width = 0
                height = 0
                for bbox in object.iter('bndbox'):
                    xmin = int(bbox.find('xmin').text)
                    xmax = int(bbox.find('xmax').text)
                    ymin = int(bbox.find('ymin').text)
                    ymax = int(bbox.find('ymax').text)
                    bbox = [xmin, ymin, xmax, ymax]
                    ann = {
                        "area": xmax * ymax,
                        "iscrowd": 0,
                        "image_id": image_id,
                        "bbox": bbox,
                        "category_id": 0,
                        "id": bnd_id,
                        "segmentation": [],
                    }
                    json_dict["annotations"].append(ann)
                    bnd_id = bnd_id + 1
                    print(bbox)
                print()
    for cate, cid in categories.items():
        cat = {"supercategory": "none", "id": cid, "name": cate}
        json_dict["categories"].append(cat)
    # Save Coco format annotations in a json file
    with open(json_file, 'w') as f:
        json_str = json.dumps(json_dict)
        f.write(json_str)
        f.close()
        
    '''

    # Save Coco format annotations in a json file
    os.makedirs(os.path.dirname("annotations/"+json_file), exist_ok=True)
    json_fp = open("annotations/"+json_file, "w")
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()
    '''

if __name__ == "__main__":

    # Dataset path for test
    data_path = "data/IIIT-AR-13K/test_xml"
    data_path_img = "data/IIIT-AR-13K/test_images"
    xml_files = os.listdir(data_path)
    print("Number of xml files (test): {}".format(len(xml_files)))
    image_files = os.listdir(data_path_img)
    print("Number of jpg files (test): {}".format(len(image_files)))
    convert(xml_files, "./test.json", data_path, data_path_img)
    
    # Dataset path for train
    data_path = "data/IIIT-AR-13K/training_xml"
    data_path_img = "data/IIIT-AR-13K/training_images"
    xml_files = os.listdir(data_path)
    print("Number of xml files (train): {}".format(len(xml_files)))
    image_files = os.listdir(data_path_img)
    print("Number of jpg files (train): {}".format(len(image_files)))
    convert(xml_files, "./train.json", data_path, data_path_img)
    '''
    for i in range(0, 420):
        xml_files = xml_files + glob.glob(os.path.join(data_path, "AR_"+str(1000+i)+".xml"))

    print("Number of xml files (train): {}".format(len(xml_files)))
    # Generate Coco format annotations
    convert(xml_files, "./train.json", data_path)

    xml_files = []
    for i in range(420, 540):
        xml_files = xml_files + glob.glob(os.path.join(data_path, "cTDaR_t"+str(10000+i)+".xml"))

    print("Number of xml files (val): {}".format(len(xml_files)))
    # Generate Coco format annotations
    convert(xml_files, "./val.json", data_path)

    xml_files = []
    for i in range(540, 600):
        xml_files = xml_files + glob.glob(os.path.join(data_path, "cTDaR_t"+str(10000+i)+".xml"))

    print("Number of xml files (test): {}".format(len(xml_files)))
    # Generate Coco format annotations
    convert(xml_files, "./test.json", data_path)'''