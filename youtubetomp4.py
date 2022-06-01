from pytube import YouTube
from datetime import date

link = input("YouTube link: ")

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "F:/", 
filename = input("Filename: "))
except:
    print("Some Error!")
    
print('Task Completed!')







































