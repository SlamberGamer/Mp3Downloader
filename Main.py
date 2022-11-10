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

#upgrade pytube through the official github
#python -m pip install git+https://github.com/pytube/pytube


class ExampleApp(QtWidgets.QMainWindow, Mp3Gui2.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.textEdit_2.setText("utube playlist only")
        self.textEdit_3.setText("C:/Users/User/Desktop/")

    def process_all_gui_events():
       QCoreApplication.processEvents()

    def run(self):

        link = self.textEdit_2.toPlainText()
        link2 = self.textEdit_3.toPlainText()
        urll = link
        # urll = 'https://www.youtube.com/playlist?list=PL01HnmhM53wblIquVlQZ94WzKFDmArCQv'
        yt = Playlist(urll)
        ytname = yt.title
        yttname = str(ytname)
        status = " ---->  " + yt.title
        print(status)
        folderlink = link2
        # folder = ytname
        folder = folderlink+ytname
        list = yt.length
        count = 0
        self.label_5.setText(status)
        # siap = str("Siap Dah Download .. Selamat Berpuasa hehe")
        # time = "time elapsed: {:.2f}s".format(time.time() - start_time)
        # timee = str(time)
        # final = str(siap + timee)
        try:
            for url in yt:
                QtWidgets.QApplication.processEvents()
                try:
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
                    thread = DummyThread(self)
                    thread.start()
                    thread.finished.connect(self.label_3.setText(prog))
                except:
                    pass

            else:
                print("Siap Dah Download .. Selamat Berpuasa hehe" , "time elapsed: {:.2f}s".format(time.time() - start_time))

        except:
            print("Please Delete Folder Files in the Directory")

class DummyThread(QThread):
    finished = pyqtSignal()
    def run(self):
        self.finished.emit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()