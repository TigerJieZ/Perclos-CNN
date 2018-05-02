import cv2

class DataProducer:
    eye_cascade = cv2.CascadeClassifier('../opencv_data/haarcascade_eye.xml')
    eyeglasses_cascade = cv2.CascadeClassifier('../opencv_data/haarcascade_eye_tree_eyeglasses.xml')

    def cutEyeFromImage(self, image):
        # image: gray image

        # cut the eyes from gray image by the CascadeClassifier
        rect = self.eye_cascade.detectMultiScale(image)
        pass

if __name__ == '__main__':
    im=cv2.imread('../test_image/180.jpg')
    dataProducer=DataProducer()
    dataProducer.cutEyeFromImage(im)
