### linearsvc model 

from sklearn.svm import LinearSVC
import numpy as np 

import cv2 as cv

import PIL


class Model:
    def __init__(self):
        self.model = LinearSVC()


    def train(self, objs, counters):
        '''trains the model'''

        img_l = np.array([])
        class_l = np.array([])

        # putting images from every directory in a list
        allcounters = None
        for i in objs:    
            for j in range(1, counters[i]):
                img = cv.imread(f'1/frame{j}.jpg')[:,:,0]
                img = img.reshape(16800) # resolution (example: 200x160=passedvalue)

                img_l = np.append(img_l, [img])

                class_l = np.append(class_l, i)

            # for further image reshaping 
            allcounters += counters[i] - 1 

        img_l = img_l.reshape(allcounters, 16800)
        self.model.fit(img_l, class_l)
        print("Model trained!")

    
    def predict(self, picture):
        picture = picture[1]
        cv.imwrite('frame.jpg', cv.cvtColor(cv.COLOR_RGB2GRAY))

        img = PIL.Image.open(f'{class_num}/frame{self.counters[class_num - 1]}.jpg')
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)
        img.save(f'{class_num}/frame{self.counters[class_num - 1]}.jpg')

        img = cv.mread('frame.jpg')[:,:,0]
        img = img.reshape(16800)

        prediction = self.model.predict([img])

        return prediction[0]
