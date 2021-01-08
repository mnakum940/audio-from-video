import moviepy.editor

video = moviepy.editor.VideoFileClip("E:\\video.mp4")
#path of video, \\ is neccesory.

audio = video.audio

audio.write_audiofile("E:\\video.mp3")
#path to situate audio file

