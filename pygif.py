#python 将png图片生成为gif图片

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
