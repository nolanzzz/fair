import sys

# train or test
data_type = sys.argv[1]
# cam_#
cam = sys.argv[2]
directory = '../data/MTA/mta_data/images/' + data_type + '/' + cam + '/gt'
lines = open(directory + '/unsorted.txt', 'r').readlines()
output = open(directory + '/gt.txt', 'w')
for line in sorted(lines, key=lambda l: int(l.split(',')[1]), reverse=False):
    output.write(line)
output.close()
