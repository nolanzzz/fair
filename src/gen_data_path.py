import os
import glob
import _init_paths
import sys


def gen_caltech_path(root_path):
    label_path = 'Caltech/data/labels_with_ids'
    real_path = os.path.join(root_path, label_path)
    image_path = real_path.replace('labels_with_ids', 'images')
    images_exist = sorted(glob.glob(image_path + '/*.png'))
    with open('../src/data/caltech.all', 'w') as f:
        labels = sorted(glob.glob(real_path + '/*.txt'))
        for label in labels:
            image = label.replace('labels_with_ids', 'images').replace('.txt', '.png')
            if image in images_exist:
                print(image[22:], file=f)
    f.close()


def gen_data_path(root_path):
    mot_path = 'MOT17/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path)) if s.endswith('SDP')]
    with open('/home/yfzhang/PycharmProjects/fairmot/src/data/mot17.half', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_half):
                image = images[i]
                print(image[22:], file=f)
    f.close()


def gen_data_path_mot17_val(root_path):
    mot_path = 'MOT17/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path)) if s.endswith('SDP')]
    with open('/home/yfzhang/PycharmProjects/fairmot2/src/data/mot17.val', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_half, len_all):
                image = images[i]
                print(image[22:], file=f)
    f.close()


def gen_data_path_mot17_emb(root_path):
    mot_path = 'MOT17/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path)) if s.endswith('SDP')]
    with open('/home/yfzhang/PycharmProjects/fairmot2/src/data/mot17.emb', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_half, len_all, 3):
                image = images[i]
                print(image[22:], file=f)
    f.close()


def gen_data_path_mta_train(root_path, num_steps, expected_frames):
    data_path = 'data/MTA/mta_data/images/train'
    label_path = 'data/MTA/mta_data/labels_with_ids/train'
    real_path = os.path.join(root_path, label_path)
    write_file = os.path.join(root_path, 'src/data/mta.train')
    total_frames = 124230
    period_frames, step_length = data_portion(total_frames, num_steps, expected_frames)
    seq_names = [s for s in sorted(os.listdir(real_path))]
    with open(write_file, 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.txt'))
            len_all = len(images)
            # len_half = int(len_all / 2)
            period_i, curr_step = 0, 0
            for i in range(len_all):
                # pass the last step, return here
                if curr_step == num_steps:
                    break
                # enough frames for current step
                if period_i > period_frames:
                    print("step " + str(curr_step), file=f)
                    curr_step += 1
                    period_i = 0
                    i += step_length
                    print("i " + str(i), file=f)
                    continue
                # not enough frames yet:
                period_i += 1
                image = ((images[i])[:-3] + 'jpg').replace(label_path, data_path)
                print(image[29:], file=f)
    f.close()


def data_portion(total_frames, num_portions, expected_frames):
    period_frames = expected_frames / num_portions
    step_length = total_frames / num_portions
    return period_frames, step_length


if __name__ == '__main__':
    root = '/u40/zhanr110/MTMCT'
    portions = sys.argv[1]
    frames = sys.argv[2]
    gen_data_path_mta_train(root, int(portions), int(frames))
