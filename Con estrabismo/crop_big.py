from PIL import Image

# Load the image
photo = 1711
image = Image.open('Con estrabismo\IMG_{}.jpeg'.format(photo))

left = 480
upper = 600
margin = -40

right = left + 1370 + margin
lower = upper + 550 + margin
bbox = (left, upper, right, lower)
# Crop the sub-image
new_size = (1370, 550)
image = image.crop(bbox).resize(new_size)
image.save('Con estrabismo\{}.png'.format(photo))