import pytube

def main_choice() :
    
    while True :
        print('''
    (1) Download a Youtube video
    (2) Download a Youtube playlist
             ''')
        choice = input("Choice : ")
        if choice == "1" or choice == "2":
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

def quality_choice() :
    qualities = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "4320p"]
    while True:
        choice = input("Choose the quality (360p, 720p, 1080p, ..., max) : ")
        if choice in qualities or choice == "max":
            return choice
        else:
            print("Input a valid quality (144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, 4320p)")
            continue
    
def get_urls() :
    print("Enter the links of the videos (end by entering 'STOP'):")

    urls = []
    url = "t"
    while url != "STOP" :
        url = input()
        if url in urls :
            choice = input("This url has already been added. Do you still wish to continue ? (y/n)")
            if choice != "y":
                continue
        urls.append(url)
        print(f"{url} added !")
        print(f" current list : {urls}")
    return urls
        
def main():
    while True :
        choice = main_choice()
        if choice == "1" :
            video_choice()
            if choice == "4":
                continue
            elif choice == "1":
                quality = quality_choice()
                urls = get_urls()
                
        elif choice == "2" :
            playlist_choice()
        
main()
    