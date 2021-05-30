import os.path as osp
import os
import sys
import numpy as np

data_type = sys.argv[1]
folder_no = sys.argv[2]
path = '~/fair-tracker/data/MTA/mta_data/images/' + data_type + '/cam_' + folder_no + '/gt'
filename = path + '/coords_fib_cam_' + folder_no + '.txt'

tid_curr = 0
tid_last = -1
gt = np.loadtxt(filename, dtype=np.float64, delimiter=',')
label_fpath = path + '/gt.txt'
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