import threading
import requests
import sseclient
import json


class ScoreStreamThread(threading.Thread):

    def __init__(self, db, url):
        threading.Thread.__init__(self, target=self._stream_threader)
        self._kill = threading.Event()
        self._url = url
        self._db = db

    def _stream_and_collect_scores(self, sse_client_events):
        """
        Streams and collects data from the SSE stream sse_client_events.

        :param sse_client_events: SSEClient iterator for SSE events.
        """
        for json_event in sse_client_events:
            if self._kill.is_set():
                break
            self._db.store(json_event.data)

    def _stream_threader(self):
        """Function to run on each new ScoreStreamThread."""
        client_events = sseclient.SSEClient(self._url)
        self._stream_and_collect_scores(client_events)

    def stop(self):
        """Stops ScoreStreamThread by setting kill Event flag."""
        if not self._kill.is_set():
            self._kill.set()
