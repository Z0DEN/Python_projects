from PIL import Image

im = Image.open("/home/blesk/GitHub/Python_projects/cropped_image.jpg")
pixels = im.load() # список с пикселями
x, y = im.size # ширина (x) и высота (y) изображения


for i in range(x):  
    for j in range(y):
        r, g, b = pixels[i, j]
        rgb = f"{r}, {g}, {b}"
        print('#' + ''.join([f"{int(i):02x}" for i in rgb.split(',')]))
        print(r, g, b)