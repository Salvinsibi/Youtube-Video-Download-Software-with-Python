from pytube import YouTube

link = ""
Youtube_1 = YouTube(link)

print(Youtube_1.title)
#print(Youtube_1.thumbnail_url)
videos = Youtube_1.streams.all()
vid = list(enumerate(videos))

for i in vid:
    print(i)
strm = int(input("enter : "))
videos[strm].download()
print("succesfull")