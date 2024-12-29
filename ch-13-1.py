import numpy as np
from skimage import io
# 建立一個 512x512 的黑色影像
image = np.zeros((512, 512, 3), dtype=np.uint8)
image[:, :, 0] = 255
# 在影像上繪製矩形
image[100:300 , 100:200] = [0,255,0]
# 在影像上繪製矩形
image[200:300 , 300:400] = [0,0,0]
# 在影像上繪製矩形
image[300:400 , 200:400] = [255,255,0]
# 顯示影像
io.imshow(image)
io.show()
