### camera access  

import cv2 as cv


class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camer.isOpened():
            raise ValueError("Camera unavailable")
        
    def __del__(self):
        if self.camer.isOpened():
            self.camera.release()

    def picture(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret: return(ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))

            else: return(ret, None)
        
        else: return None