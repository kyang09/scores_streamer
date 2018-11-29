import threading
#import time
class ScoreStreamThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, target=self.stream_threader)
        self.kill = threading.Event()
        self._i = 0.00

    def stream_and_collect_scores(self):
        while not self.kill.is_set():
            self._i += 0.01

    def stream_threader(self):
        self.stream_and_collect_scores()

    def stop(self):
        if not self.kill.is_set():
            self.kill.set()
