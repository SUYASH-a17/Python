import cv2, glob

images = glob.glob('imgs/*.jpg')

for image in images:
    img = cv2.imread(image,0)
    re = cv2.resize(img,(200,200))
    cv2.imshow('new', re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows
    cv2.imwrite('resized_'+image,re)