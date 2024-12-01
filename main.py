from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("enter video url: ")

yt = YouTube(url, on_progress_callback=on_progress)

path = ""
#By default, it downloads to the working directory.

print(yt.title)
yt.streams.get_highest_resolution().download(path)