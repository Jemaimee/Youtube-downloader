import yt_dlp
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os



def download_video(url, resolution, path):
    height = resolution.replace("p","")
    print(height)
    ydl_opt = {
        "format": f"bestvide[height={height}]+bestaudio/best",
        "outtmpl" : os.path.join(path,"%(title)s.%(ext)s")
    }
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download([url])

        

def download_videos(resolution, urls, path):
    for url in urls :
        video = "z"
        
download_video("https://www.youtube.com/watch?v=0fw5Cyh21TE", "1080p", "videos")