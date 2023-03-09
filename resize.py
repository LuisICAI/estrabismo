from PIL import Image

photo = 1418 # 1647, 1651, 1665, 1705, 1709, 1712, 1713

new_size = (1370, 550)

for photo in [1705, 1709, 1712, 1713]:
    print(photo)
    for row in range(3):
        print(row, end=': ')
        for col in range(3):
            print(col, end=' ')
            # Load the image
            image = Image.open('Con estrabismo\crop\{}_{}_{}.png'.format(photo, row, col))
            # resize the image
            resized_image = image.resize(new_size)

            # save the resized image
            resized_image.save('Con estrabismo\crop\{}_{}_{}.png'.format(photo, row, col))

