from pytube import YouTube
import os

#url input
yt = YouTube(str(input("enter URL: \n")))

#extract audio
video = yt.streams.filter(only_audio=True).first()

#destination to save file
print("enter destination to save file (leave blank for current directory:\n")
dest = str(input(">>")) or '.'

#download the file
out_file = video.download(output_path=dest)

#save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

#output message
print(yt.title + "has been downloaded and converted successfully")

#adapted from clcoding.com
