"""Data store

This data structure will help build a scalable solution
to handle multiple concurrent users. 

We will need to be able to lock the data store
when we're writing to it.
"""

from threading import Lock
import datetime


class DataStore:
    """Creates an instance of Data Store,
    the core data structure of Redis.

    This class wraps the Python dictionary and
    provides a similar interface."""

    def __init__(self):
        self._data = dict()
        self._expiry = datetime.timestamp()
        self._lock = Lock()

    def __getitem__(self, key):
        item = self._data[key]
        return item

    def __setitem__(self, key, value):
        self._data[key] = value

    def set_with_expiry(key, value, time):
        
