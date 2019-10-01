# Getting Individual Channels
from PIL import Image
katy = Image.open("katy_perry.jpg")
print(katy.mode)
r, g, b = katy.split()
r.show()
g.show()
b.show()

# Awesome merge effect
from PIL import Image
katy1 = Image.open("katy_perry.jpg")
anne = Image.open("anne_marie.jpg")
area = (0, 0, 300, 223)
katy = katy1.crop(area)
r1, g1, b1 = katy.split()
r2, g2, b2 = anne.split()
new_katy = Image.merge("RGB", (g1, r1, b1))
new_img = Image.merge("RGB", (r1, g2, b1))
new_img.show()
new_katy.show()

# Basic Transformations
from PIL import Image
katy = Image.open("katy_perry.jpg")
square_katy = katy.resize((900,900))
flip_katy = katy.transpose(Image.FLIP_LEFT_RIGHT)
spin_katy = katy.transpose(Image.ROTATE_90)

square_katy.show()
flip_katy.show()
spin_katy.show()

# Modes and Filters
from PIL import Image
from PIL import ImageFilter
katy = Image.open("katy_perry.jpg")
black_white = katy.convert("L")
black_white.show()
blur = katy.filter(ImageFilter.BLUR)
detail = katy.filter(ImageFilter.DETAIL)
edges = katy.filter(ImageFilter.FIND_EDGES)
blur.show()
detail.show()
edges.show()















