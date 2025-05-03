import imageio.v3 as iio
from PIL import Image

filenames = ['C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/cat.jpg','C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/cat3.jpg','C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/cat4.jpg','C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/cat5.jpg','C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/cat6.jpg',]
images = [ ]

# 1. Get the size of the largest image
max_width = 0
max_height = 0

for filename in filenames:
    with Image.open(filename) as img:
        max_width = max(max_width, img.width)
        max_height = max(max_height, img.height)

# 2. Resize or pad each image to the same size
for filename in filenames:
    with Image.open(filename) as img:
        # Convert to RGBA for transparency support
        img = img.convert("RGBA")

        # Create a new blank image with max size
        background = Image.new("RGBA", (max_width, max_height), (0, 0, 0, 0))

        # Paste the original image into the center
        x = (max_width - img.width) // 2
        y = (max_height - img.height) // 2
        background.paste(img, (x, y))

        images.append(background)

# 3. Save as GIF
iio.imwrite('C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/hailey.gif', images, duration=700, loop=0)

#for filename in filenames:
#  with Image.open(filename) as img:
 #   max_width = max(max_width, img.width)
  #  max_height = max(max_height, img.height)

#for filename in filenames:
 # images.append(iio.imread(filename))

#iio.imwrite('C:/Users/pmqnebalasca/Desktop/YEAR_2026/python/Gif/hailey.gif', images, duration = 500, loop = 0)
