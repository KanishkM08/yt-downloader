from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)  

print("Enter file destination in 'yt-downloader'")
destination = str(input()) or 'Downloaded-Videos'

yd = yt.streams.get_highest_resolution()

yd.download(destination)

print(yt.title, "has successfully been downloaded in", destination)

os.startfile(destination)