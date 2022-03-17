from moviepy.editor import *
import cv2


###OVERLAY TEXT ON IMAGE###
def OverlayText(filename, img):
    img =cv2.imread(img)
    height, width, _ = img.shape
    text_clip= TextClip(txt="Python is Awesome!", fontsize=40, size = (int(width/2),0), font="Lane",color="white")
    text_clip = text_clip.set_position('center')
    tc_width, tc_height = text_clip.size #(width,height)
    color_clip = ColorClip(size=(tc_width+(int(width/4)), tc_height+(int(width/4))), color=(100, 0, 0))
    color_clip = color_clip.set_opacity(.4)
    #color_clip.save_frame("color_clip.png")
    final_clip = CompositeVideoClip([color_clip, text_clip])
    final_clip.save_frame("final.png")
    im_clip = ImageClip(img)
    final_clip = final_clip.set_position('center')

    final_output = CompositeVideoClip([im_clip, final_clip])
    final_output.save_frame(filename)


"""
###OVERLAY TEXT ON IMAGE###
def OverlayText(img):
    
    text_clip= TextClip(txt="Python is Awesome!", fontsize=40, size = (800,0), font="Lane",color="white")
    text_clip = text_clip.set_position('center')
    tc_width, tc_height = text_clip.size #(width,height)
    color_clip = ColorClip(size=(tc_width+100, tc_height+50), color=(100, 0, 0))
    color_clip = color_clip.set_opacity(.4)
    #color_clip.save_frame("color_clip.png")
    final_clip = CompositeVideoClip([color_clip, text_clip])
    final_clip.save_frame("final.png")
    im_clip = ImageClip("1.jpg")
    final_clip = final_clip.set_position('center')

    final_output = CompositeVideoClip([im_clip, final_clip])
    final_output.save_frame("final_output.png")

    text_clip.save_frame("out.png")

###CONVERT IMAGES TO VIDEO###
im_clip = ImageClip("1.jpg", size=(720, 1280))

clips = []
clip1 =  ImageClip('im_clip').set_duration(2)
clip2 =  ImageClip('im_clip').set_duration(3)
clip3 =  ImageClip('im_clip').set_duration(4)
clips.append(clip1)
clips.append(clip2)
clips.append(clip3)

video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile("video-output.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")

"""

