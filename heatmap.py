import numpy as np
import cv2
from skimage import exposure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = cv2.imread("C:/Users/Devin Chau/Desktop/sjsumaptemporary.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.show()

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

a_component = lab[:, :, 1]

_, th = cv2.threshold(a_component, 140, 255, cv2.THRESH_BINARY)

blur = cv2.GaussianBlur(th, (13, 13), 11)

heatmap_img = cv2.applyColorMap(blur, cv2.COLORMAP_JET)

super_imposed_img = cv2.addWeighted(heatmap_img, 0.5, image, 0.5, 0)

super_imposed_img_rgb = cv2.cvtColor(super_imposed_img, cv2.COLOR_BGR2RGB)

plt.imshow(super_imposed_img_rgb)
plt.show()