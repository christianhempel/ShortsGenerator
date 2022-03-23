###CONVERT IMAGES TO VIDEO###

im_clip = ImageClip("final_output.png")
def picToVid(mp3):
    clips = []
    clip1 =  ImageClip('im_clip').set_duration(2)
    clip2 =  ImageClip('im_clip').set_duration(3)
    clip3 =  ImageClip('im_clip').set_duration(4)
    clips.append(clip1)
    clips.append(clip2)
    clips.append(clip3)

    video_clip = concatenate_videoclips(clips, method='compose')
    video_clip.write_videofile("video-output.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")

