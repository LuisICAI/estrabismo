from PIL import Image

# Load the image
photo = r'C:\Users\luisz\Master\NoEstructurados\estrabismo\nuevas fotos\estrab1.jpeg'
image = Image.open(photo)

h = 0.15
v = 0.15
left = image.width*(h)
right = image.width*(1-h)
top = image.height*(v)
bottom = image.height*(1-v)

bbox = (left, top, right, bottom)
# Crop the sub-image
new_size = (1370, 550)
image2 = image.crop(bbox).resize(new_size)
image2.save('.tmp\{}.png'.format(0))