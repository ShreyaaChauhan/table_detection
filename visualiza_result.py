from mmdet.apis import init_detector, inference_detector
import mmcv
# Specify the path to model config and checkpoint file
config_file = 'configs/mask_rcnn/mask_rcnn_dit_icdar2019.py'
checkpoint_file = 'exps/latest.pth'
# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')
# test a single image and show the results
img =  "data/GO-IIIT-5K/test/AR_1023.jpg" # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
# visualize the results in a new window
#model.show_result(img, result)
model.show_result(img, result, out_file='result.jpg')