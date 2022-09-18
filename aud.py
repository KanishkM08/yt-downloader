from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)  

yd = yt.streams.filter(only_audio=True).first()

print("Enter file destination in 'yt-downloader'")
destination = str(input()) or 'Downloaded-Audios'

out_file = yd.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title, "Audio file has successfully been downloaded in", destination)
os.startfile(destination)