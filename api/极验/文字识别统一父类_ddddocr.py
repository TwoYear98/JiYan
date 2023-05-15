# @author: 文字识别统一父类_ddddocr
# @file: 2023/4/3
# time: 2023-04-03 12:39
import ddddocr
import cv2
with open('1.jpg', 'rb') as f:
    img = f.read()


class Ddddocr:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr(det=True)
        poses = self.ocr.detection(img)
        im = cv2.imread("1.jpg")

        for box in poses:
            x1, y1, x2, y2 = box
            im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

        cv2.imwrite("result.jpg", im)


if __name__ == '__main__':
   d = Ddddocr()