import cv2
import glob

# Nandhu: creates new rotated images and give names to them

images=glob.glob('Train/**/*.jpg', recursive=True)

for image in images:
    img=cv2.imread(image)
   
    rows = img.shape[0]
    cols = img.shape[1]

    img_center = (cols / 2, rows / 2)
    M1 = cv2.getRotationMatrix2D(img_center, 5, 1)
    M2 = cv2.getRotationMatrix2D(img_center, -5, 1)
    M3 = cv2.getRotationMatrix2D(img_center, 10, 1)
    M4 = cv2.getRotationMatrix2D(img_center, -10, 1)
    M5 = cv2.getRotationMatrix2D(img_center, 15, 1)
    M6 = cv2.getRotationMatrix2D(img_center, -15, 1)


    rotated1 = cv2.warpAffine(img, M1, (cols, rows), borderValue=(255,255,255))
    rotated2 = cv2.warpAffine(img, M2, (cols, rows), borderValue=(255,255,255))
    rotated3 = cv2.warpAffine(img, M3, (cols, rows), borderValue=(255,255,255))
    rotated4 = cv2.warpAffine(img, M4, (cols, rows), borderValue=(255,255,255))
    rotated5 = cv2.warpAffine(img, M5, (cols, rows), borderValue=(255,255,255))
    rotated6 = cv2.warpAffine(img, M6, (cols, rows), borderValue=(255,255,255))


   
    filename = image
    filename = filename[0:-4]
    cv2.imwrite(filename+"_R5.jpg",rotated1)
    cv2.imwrite(filename+"_R-5.jpg",rotated2)
    cv2.imwrite(filename+"_R10.jpg",rotated3)
    cv2.imwrite(filename+"_R-10.jpg",rotated4)
    cv2.imwrite(filename+"_R15.jpg",rotated5)
    cv2.imwrite(filename+"_R-15.jpg",rotated6)

exit()
