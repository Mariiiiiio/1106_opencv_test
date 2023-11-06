from rembg import remove
from PIL import Image

input_path = "dog.png"
out_path = "dogremove.png"
input = Image.open(input_path)
out = remove(input)
output.save(out_path)