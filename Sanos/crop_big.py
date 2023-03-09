from PIL import Image

# Load the image
photo = 1782
image = Image.open('Sanos\IMG_{}.jpeg'.format(photo))

left = 680
upper = 650
margin = -400

right = left + 1370 + margin
lower = upper + 550 + margin / 1370 * 550
bbox = (left, upper, right, lower)
# Crop the sub-image
new_size = (1370, 550)
image = image.crop(bbox).resize(new_size)
image.save('Sanos\{}.png'.format(photo))