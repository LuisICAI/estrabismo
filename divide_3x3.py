from PIL import Image

# Load the image
image = Image.open(r'C:\Users\luisz\Master\NoEstructurados\estrabismo\nuevas fotos\estrab4.JPG')
bbox = (10, 0, image.width-10, image.height-10)
# Crop the sub-image
image = image.crop(bbox)
image.save('prueba.jpg')

# Define the size of each sub-image
sub_image_width = image.width // 3
sub_image_height = image.height // 3

margin = 10
# Loop over each row and column in the grid
for row in range(3):
    for col in range(3):
        # Calculate the bounding box for the sub-image
        left = col * sub_image_width
        upper = row * sub_image_height
        right = (col + 1) * sub_image_width
        lower = (row + 1) * sub_image_height
        bbox = (left+margin, upper+margin, right-margin, lower-margin)
        
        # Crop the sub-image
        sub_image = image.crop(bbox).resize((1370, 550))
        
        # Save the sub-image with a unique filename
        filename = f'.tmp\{2}{row}{col}.jpg'
        sub_image.save(filename)
