from keras.preprocessing.image import load_img, img_to_array
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
import tensorflow as tf
from keras.applications.vgg19 import preprocess_input
from keras.preprocessing.image import img_to_array, array_to_img
import os

# 載入你的圖片
content_image_path = 'photo/IMG_3782.jpg'

# 載入CycleGAN模型
gan_model = tf.keras.models.load_model('cycle_gan_model_path')

# 處理圖片進行風格轉換
content_image = load_img(content_image_path, target_size=(256, 256))
content_image = img_to_array(content_image)
content_image = np.expand_dims(content_image, axis=0)
content_image = preprocess_input(content_image)

# 進行風格轉換
stylized_image = gan_model.predict(content_image)

# 保存轉換後的圖片
output_path = 'stylized_image.jpg'
array_to_img(stylized_image[0]).save(output_path)
