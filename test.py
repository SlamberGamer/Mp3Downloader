import time
start_time = time.time()

siap = str("Siap Dah Download .. Selamat Berpuasa hehe")
                print(siap + "time elapsed: {:.2f}s".format(time.time() - start_time))
                QtWidgets.QApplication.processEvents()
                self.label_3.setText("Siap Dah Download .. Selamat Berpuasa hehe",
                      "time elapsed: {:.2f}s".format(time.time() - start_time))