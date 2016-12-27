#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Graphium
# URL:      http://tehutehu.com
# License:  MIT License
# Created:  2016-12-27
#
import numpy as np
from PIL import Image

import argparse
ps = argparse.ArgumentParser()
ps.add_argument('imglist',type=str)
ps.add_argument('clip_size',type=int)
args = ps.parse_args()
imgs = [Image.open(x.strip()) for x in open(args.imglist).readlines()]

data = np.zeros([len(imgs), 3*args.clip_size*args.clip_size])
for i,img in enumerate(imgs):
    data[i] = np.asarray(img).reshape([3*args.clip_size*args.clip_size])

data = (data-127.5) / 127.5
np.save('Data.npy',data)


