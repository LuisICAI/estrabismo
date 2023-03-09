from PIL import Image

# Load the image
photo = 'istockphoto-1164678540-170667a.jpg'
image = Image.open('Sanos\{}'.format(photo))

left = 30
upper = 80
margin = 40
prop = 0.3

right = left + 1370*prop + margin*prop + 100
lower = upper + 550*prop + margin*prop / 1370 * 550
bbox = (left, upper, right, lower)
# Crop the sub-image
new_size = (1370, 550)
image = image.crop(bbox).resize(new_size)
image.save('Sanos\{}.png'.format(1003))