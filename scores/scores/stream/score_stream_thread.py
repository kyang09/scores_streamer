import threading
import requests
import sseclient
import json


class ScoreStreamThread(threading.Thread):
    
    def __init__(self, db, url):
        threading.Thread.__init__(self, target=self.stream_threader)
        self.kill = threading.Event()
        self._url = url
        self._db = db

    def stream_and_collect_scores(self, sse_client_events):
        for json_event in sse_client_events:
            if self.kill.is_set():
                break
            self._db.store(json_event.data)

    def stream_threader(self):
        # response = requests.get(self._url, stream=True)
        # client = sseclient.SSEClient(response)
        client_events = sseclient.SSEClient(self._url)
        self.stream_and_collect_scores(client_events)

    def stop(self):
        if not self.kill.is_set():
            self.kill.set()
