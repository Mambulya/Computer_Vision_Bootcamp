from PIL import Image
import pylab    # Numpy + Matplotlib

# Задание 3 из lab05

src_pic = "../pics/dog_and_flowers.webp"
img = Image.open(src_pic)
im = pylab.array(img)
pylab.imshow(im)

print("Plese, click 3 points")
points = pylab.ginput(1)
print(points)