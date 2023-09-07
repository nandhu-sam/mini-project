import cv2, glob

# Nandhu: Probably for resizing this particular font

images = glob.glob('/Users/saeedeh/Desktop/Alphabet pics/Franklin Gothic-09/Small/*.jpg')

for image in images:
    img = cv2.imread(image)
    re = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    
    cv2.imshow("checking",re)
    
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    filename = image
    filename = filename[0:-4]
    
    cv2.imwrite(filename+"_32X32.jpg", re)

exit()