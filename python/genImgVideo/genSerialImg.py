import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMG_SIZE   = 256 # 画像サイズ
BLOCK_SIZE = 64  # 黒ブロックサイズ

fig, ax = plt.subplots(2, 8, figsize=(16,4), subplot_kw={'xticks': [], 'yticks': []})
fig.subplots_adjust(hspace=0.3, wspace=0.05)

img_count = 0
for h in range(0, IMG_SIZE, BLOCK_SIZE):
    for w in range(0, IMG_SIZE, BLOCK_SIZE):
        img_count = img_count + 1
        
        # IMG_SIZE x IMG_SIZEの白塗り画像作成
        img = np.empty((IMG_SIZE, IMG_SIZE))
        img.fill(255)
        
        # 黒ブロックを白塗り画像に書き込み
        img[h:h+BLOCK_SIZE,w:w+BLOCK_SIZE] = np.zeros((BLOCK_SIZE, BLOCK_SIZE))
        
        ax.flat[img_count-1].imshow(img, 'gray')
        ax.flat[img_count-1].set_title('{:05d}.png'.format(img_count))
        
fig.savefig('serialImgs.png', bbox_inches = 'tight')
