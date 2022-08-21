import json
import shapely.geometry
DATA = {}
with open("data/GO-IIIT-5K/train.json") as json_file:
    GO_IIIT_5K_test= json.load(json_file)
    data = {
        "categories": GO_IIIT_5K_test["categories"],
        "images": GO_IIIT_5K_test["images"] ,
        "annotations": GO_IIIT_5K_test["annotations"] ,
    }
    '''for info in data["annotations"]:
        data['adc'] = "ghj"
        #print(info["segmentation"])
    annotations = []
    for info in data["annotations"]:
        info["id"] =  count
        annotations.append(info)
        count +=1
    data["annotations"] = annotations
    for i in data["annotations"]:
        print(i['abc'])'''
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
with open("train.json", 'w') as test: 
    json.dump(data, test, indent = 4, sort_keys=True)