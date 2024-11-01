import cv2 as cv

import tkinter as tk
from tkinter import simpledialog

import os

import PIL.Image, PIL.ImageTk

import cam

from models import model_linearsvc as model


### gui interface

class App:
    def __init__(self, window=tk.Tk(), window_title="Object Classifier"):
        self.window = window
        self.window_title = window_title

        # for image counting
        # tipp: use dictionaries
        self.objs = [1,2] 
        self.counters = [1,1]

        # ai model
        self.model = model.Model()
        self.life_predict = False

        # camera and gui
        self.camera = cam.Camera()

        # self functions
        self.init_gui()

        self.delay = 15
        self.update()

        self.window.attributes('-topmost', True)
        self.window.mainloop()


    def init_gui(self):
        '''main gui function'''
        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(self.window, text="Auto Prediction", width=50, command=self.life_predict_btn)
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)

        self.classname_one = simpledialog.askstring("Classname One", "Enter the name of the first class:", parent=self.window)
        self.classname_two = simpledialog.askstring("Classname Two", "Enter the name of the second class:", parent=self.window)

        self.btn_class_one = tk.Button(self.window, text=self.classname_one, width=50, command=lambda: self.save_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.window, text=self.classname_two, width=50, command=lambda: self.save_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.window, text="Train Model", width=50, command=lambda: self.model.train(self.counters))
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_predict = tk.Button(self.window, text="Predcit", width=50, command=self.predict)
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(self.window, text="Reset", width=50, command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.class_label = tk.Label(self.window, text="CLASS")
        self.class_label.config(font=("Arial", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)


    def predict(self):
        '''predicts the shown object with ai model'''
        
        picture = self.camera.picture()

        prediction = self.model.predict(picture)
        if prediction == 1:
            self.class_label.config(text=self.classname_one)
            return self.classname_one
        if prediction == 2:
            self.class_label.config(text=self.classname_two)
            return self.classname_two


    def life_predict_btn(self):
        '''changes lifepredict value to stop lifepredict'''
        self.life_predict = not self.life_predict


    def save_class(self, class_num):
        '''saves the class'''

        ret, frame = self.camera.picture()

        # making sure directories for pictures will be there
        for dir in self.objs:
            if not os.path.exists(f'{dir}'):
                os.mkdir(f'{dir}') 

        # making the image gray 
        cv.imwrite(f'{class_num}/frame{self.counters[class_num - 1]}.jpg', cv.cvtColor(frame, cv.COLOR_RGB2GRAY))

        # counting the image
        img = PIL.Image.open(f'{class_num}/frame{self.counters[class_num - 1]}.jpg')
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)
        img.save(f'{class_num}/frame{self.counters[class_num - 1]}.jpg')

        self.counters[class_num - 1] += 1


    def reset(self):
        '''deletes all the files in current directories'''

        for dir in self.objs:
            for file in os.listdir(dir):
                file_path = os.path.join(dir, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

        self.counters = [1,1]
        #self.model = model.Model()

        self.class_label.config(text="class")

    
    def update(self):
        '''updating the camera pictures'''

        if self.life_predict:
            self.predict()

        ret, frame = self.camera.picture()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)


    

    
