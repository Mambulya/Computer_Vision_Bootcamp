from PIL import Image
import pylab    # Numpy + Matplotlib

# Задание 4 из lab05

src_pic = "../pics/dog_and_flowers.webp"
img = Image.open(src_pic)
im = pylab.array(img)
pylab.imshow(im)

# зададим изначальные точки
x = [500, 500, 800, 800]
y = [1100, 800, 1100, 800]

# plotting points
pylab.plot(x, y, "y*")

# getting points
print("Plese, click 2 points")
points = pylab.ginput(2)
print(points)


# plotting lines
pylab.axis("off")
pylab.title("Plotting lines")
pylab.plot(x, y, "y-")
pylab.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], "w--")
pylab.show()
