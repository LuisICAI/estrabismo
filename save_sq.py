import os
from PIL import Image

# Ruta del directorio a leer
path_inputs = r"C:\Users\luisz\Master\NoEstructurados\estrabismo\Ojos pitu"
path_outputs = r"C:\Users\luisz\Master\NoEstructurados\estrabismo\photos\negative"
i = int(os.listdir(path_outputs)[-1].split('.')[0]) + 1

# Recorre el directorio y obtiene los elementos
bbox_left = (0, 0, 685, 550)
bbox_right = (685, 0, 1370, 550)
new_size = (600, 600)

# two eyes
for filename in os.listdir(path_inputs):
    path_photo = os.path.join(path_inputs, filename)
    image = Image.open(path_photo).resize((1370,550))
    image.crop(bbox_left).resize(new_size).save(r'{}\{:03d}.png'.format(path_outputs, i))
    print(i)
    i += 1
    image.crop(bbox_right).resize(new_size).save(r'{}\{:03d}.png'.format(path_outputs, i))
    print(i)
    i += 1

# one eye
# for filename in os.listdir(path_inputs):
#     path_photo = os.path.join(path_inputs, filename)
#     image = Image.open(path_photo).resize(new_size)
#     image.transpose(Image.FLIP_LEFT_RIGHT).save('prueba2.png')
#     image.save(r'{}\{:03d}.png'.format(path_outputs, i))
#     print(i)
#     i += 1
#     image.transpose(Image.FLIP_LEFT_RIGHT).save(r'{}\{:03d}.png'.format(path_outputs, i))
#     print(i)
#     i += 1


# data augmentation
# path_outputs = r"C:\Users\luisz\Master\NoEstructurados\estrabismo\photos\negative"
# for filename in os.listdir(path_outputs):
#     path_photo = os.path.join(path_outputs, filename)
#     image = Image.open(path_photo)
#     image.rotate(5, Image.NEAREST, expand = 0).crop((25,25,575,575)).transpose(Image.FLIP_LEFT_RIGHT) \
#         .resize(new_size).save(path_photo[:-4] + '_b.png')