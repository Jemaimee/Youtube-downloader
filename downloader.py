import pytube
import os 

videos_path = os.path.join(os.path.expanduser("~"), "Videos")


def download_video(resolution, urls):
    for url in urls :
        video = "z"