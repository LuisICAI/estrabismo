from PIL import Image

# Load the image
photo = 1713
image = Image.open('Con estrabismo\IMG_{}.JPG'.format(photo))
bbox = (34, 34, 1642, 1633)
# Crop the sub-image
image = image.crop(bbox)

# Define the size of each sub-image
sub_image_width = image.width // 3
sub_image_height = image.height // 3

# Loop over each row and column in the grid
for row in range(3):
    for col in range(3):
        # Calculate the bounding box for the sub-image
        left = col * sub_image_width
        upper = row * sub_image_height
        right = (col + 1) * sub_image_width
        lower = (row + 1) * sub_image_height
        bbox = (left, upper, right, lower)
        
        # Crop the sub-image
        sub_image = image.crop(bbox)
        
        # Save the sub-image with a unique filename
        filename = f'Con estrabismo\crop\{photo}_{row}_{col}.jpg'
        sub_image.save(filename)
