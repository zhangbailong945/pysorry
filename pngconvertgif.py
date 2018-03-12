#-*- coding:utf-8 -*-*
'''
#测试功能：多个帧png图片生成gif图片
#需要手动安装的库
(1)、python -m pip install imageio #用于mp4 转png 帧图片
'''
__author__='loach'


import imageio
import os
import os.path
from PIL import Image
gif_name='sorry.gif'
duration=0.2
frames=[]
path='temp/images'
gifPath='temp/gif/'
pngFiles=os.listdir(path)
images_list=[os.path.join(path,f) for f in pngFiles]
for image_name in images_list:
    frames.append(imageio.imread(image_name))

#保存为gif图片
imageio.mimsave(gifPath+gif_name,frames,'GIF',duration=duration)
