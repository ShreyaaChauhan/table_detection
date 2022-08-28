import json
import shapely.geometry
DATA = {}
with open("data/IIIT-AR-13K/test.json") as json_file:
    GO_IIIT_5K_test= json.load(json_file)
    data = {
        "categories": GO_IIIT_5K_test["categories"],
        "images": GO_IIIT_5K_test["images"] ,
        "annotations": GO_IIIT_5K_test["annotations"] ,
    }
    annotations = []
    #convert bounding boxes to polygons
    for i in data["annotations"]:
        #Only the segmentations that are bounding boxes
        bbox=tuple(i["bbox"])
        #Retrieve polygon from bbox through shapely.geometry.box, format was 
        polygon=shapely.geometry.box(*(bbox[0],bbox[1],bbox[0]+bbox[2], bbox[1]+bbox[3]), ccw=True)
        K=str(polygon.wkt).split("POLYGON ((")[-1].split("))")[0].split(',')
        polygon=[]
        for m in K:
            for p in m.split(" "):
                if p:
                    polygon.append(int(p))
        polygon=[polygon]
        i['segmentation'] = polygon
        annotations.append(i)
        #data['segmentation'] = polygon
        #print(data["segmentation"])
    #print(data["annotations"])'''
    data["annotations"] = annotations
    DATA = data
with open("test.json", 'w') as test: 
    json.dump(data, test, indent = 4, sort_keys=True)