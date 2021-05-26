import os.path as osp
import os
import numpy as np

tid_curr = 0
tid_last = -1
gt = np.loadtxt('coords_fib_cam_0.txt', dtype=np.float64, delimiter=',')
label_fpath = 'gt.txt'
for fid, tid, x1, y1, x2, y2 in gt:
    fid = int(fid)
    tid = int(tid)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    width = int(x2 - x1)
    height = int(y2 - y1)
    rest = 1
    label_str = '{:d},{:d},{:d},{:d},{:d},{:d},{:d},{:d},{:d}\n'.format(
        fid, tid, x1, y1, width, height, rest, rest, rest)
    with open(label_fpath, 'a') as f:
        f.write(label_str)