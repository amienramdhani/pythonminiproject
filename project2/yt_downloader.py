from pytube import YouTube

link = input("Enter your Youtube URL :  ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("enter the desired option to download the format")
dn_option = int(input("Enter the Option  : "))

dn_video = videos[dn_option]
dn_video.download()

print("download succesfully")
