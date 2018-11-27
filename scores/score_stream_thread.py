import threading
#import time
class ScoreStreamThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.kill = threading.Event()

    def start_stream(self):
        print_lock = threading.Lock()
        i = 0
        with print_lock:
            while not self.kill.is_set():
                print(i)
                i += 1

    #t = threading.Thread(target = function_for_thread)
    # ensures thread dies with main thread dies.
    # Set t.daemon = False if you want it to keep running
    #t.daemon = True
    #t.start()