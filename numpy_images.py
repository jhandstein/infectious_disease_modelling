# https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/
import numpy as np

width = 100
height = 50

array = np.zeros([height, width, 3], dtype=np.uint8)

# fill with orange pixels (RGB values in brackets)
array[:30,:] = [255, 128, 0]
array[30:,:] = [128, 0, 128]

# save image
from PIL import Image

img = Image.fromarray(array)
img.save('testrgb.png')

# editing an actual image
img_file_path = "compartments.png"
comps_img = Image.open(img_file_path, 'r')

# print(comps_img.size)
img_array = np.array(comps_img)

print(img_array[0,0])

# still broken
test_val = 0
for k, v in img_array.iteritems():
    if k == (0, 0, 0, 0) and v == (0, 0, 0, 0):
        test_val += 1
    
print(test_val)
