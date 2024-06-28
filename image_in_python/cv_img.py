import cv2
import numpy as np


def paste_image(back_img, front_img, x_offset, y_offset):
    y1, y2 = y_offset, y_offset + front_img.shape[0]
    x1, x2 = x_offset, x_offset + front_img.shape[1]

    alpha_s = front_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        back_img[y1:y2, x1:x2, c] = (alpha_s * front_img[:, :, c] +
                                alpha_l * back_img[y1:y2, x1:x2, c])


    return back_img

back_img = cv2.imread("back.png", -1)
front_img = cv2.imread("front.png", -1)

x_offset, y_offset = 0, 0
image = paste_image(back_img, front_img, x_offset, y_offset)

# font = cv2.FONT_HERSHEY_SIMPLEX 
# fontScale = 1.5
# color = (255, 255, 255) 
# thickness = 4
# image = cv2.putText(l_img, 'Заголовок', (50, 50) , font, 
#                 fontScale, color, thickness, cv2.LINE_AA) 

# Displaying the image 
cv2.imshow('result', image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
