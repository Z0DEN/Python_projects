import numpy as np
from PIL import Image

square_animation = []
for offset in range(0, 100, 2):
    sdfred = np.zeros((600, 600))
    green = np.zeros((600, 600))
    blue = np.zeros((600, 600))
    red[101 + offset : 301 + offset, 101 + offset : 301 + offset] = 255
    green[200:400, 200:400] = 255
    blue[299 - offset : 499 - offset, 299 - offset : 499 - offset] = 255
    red_img = Image.fromarray(red).convert("L")
    green_img = Image.fromarray(green).convert("L")
    blue_img = Image.fromarray((blue)).convert("L")
    square_animation.append(
        Image.merge(
            "RGB",
            (red_img, green_img, blue_img)
        )
    )
    square_animation[0].save(
    "animation.gif", save_all=True, append_images=square_animation[1:]
)
square_animation[0].save(
    "animation.gif", save_all=True, append_images=square_animation[1:]
)