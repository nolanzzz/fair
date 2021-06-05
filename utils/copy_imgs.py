import shutil
import sys


frames = int(sys.argv[1])
for i in range(6):
    j, period_i, curr_step = 1, 0, 0
    while j <= 127880:
        if curr_step == 5:
            break
        # enough frames for current step
        if period_i > frames:
            curr_step += 1
            period_i = 0
            j = j + 25000
            continue
        # not enough frames yet:
        j += 1
        period_i += 1
        img_title = str(j).zfill(6) + '.jpg'
        shutil.copy2('../data/MTA/mta_data/images/test/cam_' + str(i) + '/img1/' + img_title, '../data/MTA/mta_data/images/test/cam_' + str(i) + '_t')