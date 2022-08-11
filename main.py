from mmdet.datasets import build_dataset
from mmdet.models import build_detector
from mmdet.apis import train_detector
from mmdet.apis import set_random_seed
import mmcv
import os.path as osp


config = 'configs/mask_rcnn/mask_rcnn_dit_icdar2019.py'
# Set the device to be used for evaluation
device='cuda:0'
# Load the config
config = mmcv.Config.fromfile(config)
# Set pretrained to be None since we do not need pretrained model here
config.model.pretrained = None
config.device='cuda'
# Set up working dir to save files and logs.
config.work_dir = './exps'
# Set seed thus the results are more reproducible
config.seed = 0
set_random_seed(0, deterministic=False)
config.gpu_ids = range(1)

# Build dataset
datasets = [build_dataset(config.data.train)]
# Build the detector
model = build_detector( config.model, train_cfg=config.get('train_cfg'), test_cfg=config.get('test_cfg'))

# Add an attribute for visualization convenience
model.CLASSES = ('table',)
#print(model.CLASSES)

# Create work_dir
mmcv.mkdir_or_exist(osp.abspath(config.work_dir))
train_detector(model, datasets, config, distributed=False, validate=True)