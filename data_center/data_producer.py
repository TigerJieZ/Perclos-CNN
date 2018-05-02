import cv2


class DataProducer:
    eye_cascade = cv2.CascadeClassifier('../opencv_data/haarcascade_eye.xml')
    eyeglasses_cascade = cv2.CascadeClassifier('../opencv_data/haarcascade_eye_tree_eyeglasses.xml')

    def cutEyeFromImage(self, image):
        # image: gray image

        # cut the eyes from gray image by the CascadeClassifier
        rects = self.eyeglasses_cascade.detectMultiScale(image)
        eyes = []
        i=0
        for rect in rects:
            temp = image[rect[0]:rect[0]+rect[2], rect[1]:rect[1]+rect[3]]
            cv2.imwrite('../output_image/eye'+str(i)+'.jpg',temp)
            eyes.append(temp)
            cv2.imshow('test', temp)
            cv2.waitKey(10000)
            i+=1


if __name__ == '__main__':
    im = cv2.imread('../test_image/181.jpg')
    dataProducer = DataProducer()
    dataProducer.cutEyeFromImage(im)
