import os
import cv2
import numpy as np

IMG_SIZE   = 256 # 画像サイズ
BLOCK_SIZE = 64  # 黒ブロックサイズ

img_outdir = './img'
os.makedirs(img_outdir, exist_ok=True)

# 動画用の画像作成
outimg_files = []
img_count = 0
for h in range(0, IMG_SIZE, BLOCK_SIZE):
    for w in range(0, IMG_SIZE, BLOCK_SIZE):
        img_count = img_count + 1
        
        # IMG_SIZE x IMG_SIZEの白塗り画像作成
        img = np.empty((IMG_SIZE, IMG_SIZE))
        img.fill(255)
        
        # 黒ブロックを白塗り画像に書き込み
        img[h:h+BLOCK_SIZE,w:w+BLOCK_SIZE] = np.zeros((BLOCK_SIZE, BLOCK_SIZE))
        
        # 画像出力
        outimg_file = '{}/{:05d}.png'.format(img_outdir, img_count)
        cv2.imwrite(outimg_file, img)
        
        outimg_files.append(outimg_file)
        
# 動画作成
fourcc = cv2.VideoWriter_fourcc('m','p','4', 'v')
video  = cv2.VideoWriter('ImgVideo.mp4', fourcc, 20.0, (IMG_SIZE, IMG_SIZE))

for img_file in outimg_files:
    img = cv2.imread(img_file)
    video.write(img)

video.release()
