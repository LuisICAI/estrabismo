import os
from PIL import Image

# Ruta del directorio a leer
path_inputs = r"C:\Users\luisz\Master\NoEstructurados\estrabismo\.tmp"
path_outputs = r"C:\Users\luisz\Master\NoEstructurados\estrabismo\FotosDefinitivas\positive"
i = 186

# Recorre el directorio y obtiene los elementos
bbox_left = (0, 0, 685, 550)
bbox_right = (685, 0, 1370, 550)
new_size = (600, 600)

for filename in os.listdir(path_inputs):
    path_photo = os.path.join(path_inputs, filename)
    image = Image.open(path_photo)
    image.crop(bbox_left).resize(new_size).save(r'{}\{:03d}.png'.format(path_outputs, i))
    print(i)
    i += 1
    image.crop(bbox_right).resize(new_size).save(r'{}\{:03d}.png'.format(path_outputs, i))
    print(i)
    i += 1
