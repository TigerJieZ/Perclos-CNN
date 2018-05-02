import cv2


class DataProducer:
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eyeglasses_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    def cutEyeFromImage(self, image):
        # image: gray image

        # cut the eyes from gray image by the CascadeClassifier
        self.eye_cascade.detectMultiScale(image)
        pass

if __name__ == '__main__':
    im=cv2.imread()
    dataProducer=DataProducer()
    dataProducer.cutEyeFromImage(im)
