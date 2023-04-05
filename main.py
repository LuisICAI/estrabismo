import sys
import os
from keras import models
from keras import optimizers
from keras.models import load_model
from keras_preprocessing import image
import json

def main():
    
    # photos given
    if len(sys.argv) >= 2:
        paths = sys.argv[1:]

    # reading photos from path
    else:
        print('No photos given. Reading photos from path.')
        path_photos = input('Path to photos: ')
        paths = [os.path.join(path_photos, p) for p in os.listdir(path_photos)]
    
    # load model
    try:
        model = load_model('Version1.h5')
    except:
        print('Model not found. Please, provide the path to the model.')
        model = load_model(input('Path to model: '))

    output = []
    for path in paths:
        img = image.load_img(path, target_size=(300,300))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = img_array.reshape((1,300,300,3))
        positive_prob = float(model.predict(img_array))
        output_ = {'path': path,
                   'positive_prob': positive_prob,
                   'positive': positive_prob > 0.5}
        output.append(output_)
    with open('output.json', 'w') as f:
        json.dump(output, f)
    print('output.json saved')
            
    return

if __name__ == '__main__':
    main()
