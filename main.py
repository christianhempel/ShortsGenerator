import Crop
import TextImages
import prawToturial
import re
import TextToSpeech
from operator import itemgetter
import string
def retrieveVidContent(myDict, submission_id):
    MsgArray=[]
    x = myDict.get(submission_id)
    title = x[0][0]
    title = remove_emojis(title)
    wordcount = sum([i.strip(string.punctuation).isalpha() for i in title.split()])
    x=x[0][1:]
    x= (sorted(x, key=itemgetter(0), reverse=True))
    for comment in range(0,len(x)):
        wordcount += sum([i.strip(string.punctuation).isalpha() for i in x[comment][1].split()])

        if wordcount < 150:
            commentNoEmoji = remove_emojis(x[comment][1])
            MsgArray.append(commentNoEmoji)
        if wordcount > 150:
            return title, MsgArray
    if wordcount < 150:
        print("not enough comments to make vid")
        return 0, 0


def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d" 
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


def main():
    count=1
    myDict = prawToturial.RetrieveComments()[0]
    submissionIdArray = prawToturial.RetrieveComments()[1]
    
    for submission_id in submissionIdArray:
        title, Msgarray = retrieveVidContent(myDict, submission_id)
        if title != 0:
            TextToSpeech.CommentsToSpeech(title, "title")
            for Msg in Msgarray:
                TextToSpeech.CommentsToSpeech(Msg, str(count))
                count+=1

            
        
  
    #print(title)
    #print(message)
    #o=(str(MsgArray))
    #o = remove_emojis(o)
    #print(title)
    
    #with open("Output.txt", "w") as text_file:
    #    text_file.write("Purchase Amount: %s" % o)

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
    print("hey")
    main()
    
    