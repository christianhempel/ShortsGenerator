import Crop
import TextImages
import prawToturial
def checkComments():
    conversedict = prawToturial.RetrieveComments()
    
    for post_id in conversedict:
        title = conversedict[post_id][0]
        message = conversedict[post_id][1]
        replies = conversedict[post_id][2]
        print('Original Message: {}'.format(message))

def main():
    conversedict = prawToturial.RetrieveComments()
    MsgArray=[]
    for comment_id in conversedict:
        
        #title = conversedict[submission_id][0]
        message = conversedict[comment_id][1]
        MsgArray.append(message)
    print(MsgArray[0])
    #if len(MsgArray) <
        #print('Original Message: {}'.format(message))

"""
    for i in range(1,4):
        img = str(i)+".jpg"
        imgName=str(i)+"newimage.png"
        Crop.cropImage(imgName, img)
    for i in range(1,4):
        img = str(i)+"newimage.png"
        TextImgName=str(i)+"textimage.png"
        TextImages.OverlayText(TextImgName,img)
"""


if __name__ == "__main__":
    
    main()
    