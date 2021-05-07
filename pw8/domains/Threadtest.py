import threading
import time


class BackgroundThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(2)


def create_background_thread():
    thread = BackgroundThread()
    thread.start()
    thread.join()