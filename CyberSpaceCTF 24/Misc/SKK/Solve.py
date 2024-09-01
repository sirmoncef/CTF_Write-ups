import numpy as np
import cv2
import random
from datetime import datetime


enc_shuffle = cv2.imread('enc.png')


size_x, size_y = enc_shuffle.shape[:2]


dec_negpos = np.zeros_like(enc_shuffle)


def undo_shuffling(shuffle_value, pixel):
    if shuffle_value == 1:
        return pixel
    elif shuffle_value == 2:
        return pixel[[0, 2, 1]]
    elif shuffle_value == 3:
        return pixel[[1, 0, 2]]
    elif shuffle_value == 4:
        return pixel[[1, 2, 0]]
    elif shuffle_value == 5:
        return pixel[[2, 0, 1]]
    else:
        return pixel[[2, 1, 0]]


random.seed(datetime.now().timestamp())

# Decode the image
for i in range(size_x):
    for j in range(size_y):
        shuffle = random.randint(1, 6)
        # Undo the shuffling
        dec_negpos[i, j] = undo_shuffling(shuffle, enc_shuffle[i, j])


dec_flag = np.where(dec_negpos < 128, dec_negpos ^ 255, dec_negpos)


cv2.imwrite('restored_flag.png', dec_flag)
