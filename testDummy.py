from pytube import Playlist
from pytube import YouTube
import time
import os
import os.path
start_time = time.time()

urll = 'https://music.youtube.com/playlist?list=OLAK5uy_nqzWv4aFRNiymgpQ6uFhYya3TwLh1ksHg'
yt = Playlist(urll)
ytname = yt.title
status = "Downloading.. " + yt.title
print(Status)
folderlink = 'C:/Users/binmuham/PycharmProjects/YoutubeMp3Downloader/venv/PycharmProjects/'
folder = ytname
# folder = folderlink+ytname
list = yt.length
count = 0

try:
    for url in yt:
        count += 1
        tajuk = YouTube(url).title
        downloaded_file = YouTube(url).streams.filter(only_audio=True).first().download(folder)
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)
        countt = str(count)
        listt = str(list)
        dash = str(" # " )
        tajukk = str(tajuk)
        sepa = str("/")
        prog = "Downloaded :" + tajukk + dash + countt + sepa + listt
        print(prog)

    else:
        print("Siap Dah Download .. Selamat Berpuasa hehe" , "time elapsed: {:.2f}s".format(time.time() - start_time))

except:
    print("Please Delete Folder Files in the Directory")