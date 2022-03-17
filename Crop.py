import cv2

def cropImage(filename, img):
    img =cv2.imread(img)
    height, width, _ = img.shape
    """print("Height", height)
    print("Width", width)"""

    if height > 1280 and width > 720:
        width_mid = int(width/2)
        
        
        cut_image = img[0:1280,  width_mid-360:width_mid+360]
    elif height > 1024 and width > 576:
        width_mid = int(width/2)
        
        
        cut_image = img[0:1024,  width_mid-288:width_mid+288]
    elif height > 960 and width > 540:
        width_mid = int(width/2)
        
        
        cut_image = img[0:960,  width_mid-270:width_mid+270]
    elif height > 854 and width > 480:
        width_mid = int(width/2)
        
        
        cut_image = img[0:854,  width_mid-240:width_mid+240]
    elif height > 640 and width > 360:
        width_mid = int(width/2)
        
        
        cut_image = img[0:640,  width_mid-180:width_mid+180]
    elif height > 512 and width > 288:
        width_mid = int(width/2)
        
        
        cut_image = img[0:512,  width_mid-144:width_mid+144]
    elif height > 384 and width > 216:
        width_mid = int(width/2)
        
        
        cut_image = img[0:384,  width_mid-72:width_mid+72]


    height, width, _ = cut_image.shape
    cv2.imshow("image",cut_image)
    cv2.imwrite(filename, cut_image)
"""
    print("Height", height)
    print("Width", width)

    cv2.imshow("image",cut_image)
    cv2.waitKey(0)"""