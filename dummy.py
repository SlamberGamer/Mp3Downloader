from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt5.QtCore import Qt, QIODevice
from PyQt5.QtCore import QRunnable, Qt, QThreadPool, QThread, pyqtSignal
import Mp3Gui2
import sys
import qdarkstyle
from pytube import Playlist
from pytube import YouTube
import time
import os
import os.path
start_time = time.time()


class ExampleApp(QtWidgets.QMainWindow, Mp3Gui2.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.textEdit_2.setText("Put Your Link Here")

    def run(self):
        link = self.textEdit_2.toPlainText()
        urll = link
        # urll = 'https://www.youtube.com/playlist?list=PL01HnmhM53wblIquVlQZ94WzKFDmArCQv'
        yt = Playlist(urll)
        ytname = yt.title
        yttname = str(ytname)
        status = "Downloaded.. " + yt.title
        print(status)
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
                dash = str(" # ")
                tajukk = str(tajuk)
                sepa = str("/")
                prog = "Downloaded :" + tajukk + dash + countt + sepa + listt
                print(prog)
                self.label_5.setText(yttname)
                self.label_3.setText(prog)

            else:
                print("Siap Dah Download .. Selamat Berpuasa hehe",
                      "time elapsed: {:.2f}s".format(time.time() - start_time))

        except:
            print("Please Delete Folder Files in the Directory")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()