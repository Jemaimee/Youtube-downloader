import pytube
import downloader
import json

with open("settings.json", "r") as file:
    settings = json.load(file)

def main_choice() :
    choices = ["1", "2", "3", "4"]
    while True :
        print('''
    (1) Download a Youtube video
    (2) Download a Youtube playlist
    (3) Settings
    (4) EXIT
             ''')
        choice = input("Choice : ")
        if choice in choices:
            return choice
        else :
            print("Please enter a valid choice")
            continue

def video_choice() :
    print('''
    (1) Download video
    (2) Download audio 
    (3) Download thumbnail
    (4) BACK
          ''')
    choice = input("Choice : ")
    return choice

def playlist_choice () :
    print('''
    (1) Download videos
    (2) Download audios 
    (3) Download Thumbnails
    (4) BACK
          ''')
    choice = input("Choice : ")
    return choice

    
def get_urls() :
    print("Enter the links of the videos (end by entering 'STOP'):")

    urls = []
    url = "t"
    while url != "STOP" :
        url = input("\nURL : ")
        if url in urls :
            choice = input("This url has already been added. Do you still wish to continue ? (y/n) ")
            if choice != "y":
                continue
        elif not url.startswith("https://www.youtube.com/"):
            print("Enter a valid url")
            continue
        urls.append(url)
        print(f"{url} added !")
        print(f"\ncurrent list : {urls}")
    return urls
        
def change_settings() :
    choices = ["1","2","3"]
    while True:
        print('''
    (1) Change resolution 
    (2) Change Download path
    (3) BACK
              ''')
        choice = input("Choice : ")
        if choice == "1":
            change_resolution()
        elif choice == "2":
            pass
        elif choice == "3":
            break
def change_resolution():
    print(f"Current resolution : {settings["resolution"]}")
    resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "4320p"]
    while True:
        new_resolution = input("Choose the new resolution (360p, 720p, 1080p, ..., max) : ")
        if new_resolution in resolutions or new_resolution == "max":
            settings["resolution"] = new_resolution
            with open("settings.json", "w") as file:
                json.dump(settings, file, indent=4)
            print(f"{new_resolution} set as current resolution")
            break
        else:
            print("Input a valid resolution (144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, 4320p)")
            continue
def change_path():
    pass

def main():
    while True :
        choice = main_choice()
        if choice == "1" :
            video_choice()
            if choice == "4":
                continue
            elif choice == "1":
                urls = get_urls()
                
        elif choice == "2" :
            playlist_choice()
        elif choice == "3":
            change_settings()
        elif choice == "4":
            break
        
main()

    