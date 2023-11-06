import cv2
import numpy as np

# 讀取圖片
img = cv2.imread('./photo/IMG_3782.jpg')

# 轉換成灰度圖
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 進行邊緣檢測
edges = cv2.Canny(gray, 100, 200)

# 進行輪廓增強
kernel = np.ones((3, 3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# 將輪廓區域填充
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 0), 2)

# 顯示處理後的圖像
cv2.imshow('Cartoonized Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
