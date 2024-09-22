import numpy as np
import cv2
from skimage import exposure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = cv2.imread("C:/Users/Devin Chau/Desktop/sjsumaptemporary.png")

#creating the grid overlay
#this will just be temporary but this should give us an idea on what to do 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

dx = 100  
dy = 100  
grid_color = [0, 0, 0]  
highlight_color = [1, 0, 0] 

image[:, ::dy, :] = grid_color
image[::dx, :, :] = grid_color

highlight_cell_row = 2  
highlight_cell_col = 3 

start_row = highlight_cell_row * dx
end_row = (highlight_cell_row + 1) * dx
start_col = highlight_cell_col * dy
end_col = (highlight_cell_col + 1) * dy

image[start_row:end_row, start_col:end_col, :] = highlight_color

#this creates the heatmap 
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

a_component = lab[:, :, 1]

_, th = cv2.threshold(a_component, 140, 255, cv2.THRESH_BINARY)

blur = cv2.GaussianBlur(th, (13, 13), 11)

heatmap_img = cv2.applyColorMap(blur, cv2.COLORMAP_JET)

super_imposed_img = cv2.addWeighted(heatmap_img, 0.5, image, 0.5, 0)

super_imposed_img_rgb = cv2.cvtColor(super_imposed_img, cv2.COLOR_BGR2RGB)

plt.imshow(super_imposed_img_rgb)
plt.show()