import os.path as osp
import os
import sys
import numpy as np

path = sys.argv[1]
filename = path + '/' + sys.argv[2]

tid_curr = 0
tid_last = -1
gt = np.loadtxt(filename, dtype=np.float64, delimiter=',')
label_fpath = path + '/gt.txt'
i = 0
for fid, tid, x1, y1, x2, y2 in gt:
    if i == 0:
        i += 1
        continue
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