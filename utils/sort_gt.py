import sys

# train or test
data_type = sys.argv[1]
# cam_#
cam = sys.argv[2]
directory = '../data/MTA/mta_data/images/' + data_type + '/' + cam + '/gt'
print(directory + '/gt.txt')
print(directory + '/sorted.txt')
# lines = open(directory + '/gt.txt', 'r').readlines()
# output = open(directory + '/sorted.txt', 'w')
# for line in sorted(lines, key=lambda l: int(l.split(',')[1]), reverse=False):
#     output.write(line)
# output.close()