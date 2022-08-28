
import cv2
path = "data/trackA_modern/train/cTDaR_t10000.jpg"
img=cv2.imread(path,1) #load the image
            
bbox_1 = [
                113,
                94,
                567,
                355
            ]
bbox_2 =   [
                170,
                1235,
                850,
                208
            ]

# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2

[x,y,w,h] = bbox_1
cv2.rectangle(img, (int(x), int(y)), (int(w), int(h)), color, 2)

[x,y,w,h] = bbox_2
#cv2.rectangle(img, (int(x), int(y)), (int(w), int(h)), color, 2)


'''c1, c2 = (int(coor[1]), int(coor[0])), (int(coor[3]), int(coor[2]))
Line 159 -> cv2.rectangle(image, c1, (int(np.float32(c3[0])), int(np.float32(c3[1]))), bbox_color, -1)'''

#cv2.imshow("mycastle", img)
cv2.imwrite("myNewCastle.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()