#-*- coding: utf-8 -*-
from durus.persistent_list import PersistentList

class VolatileList(PersistentList):
    """
    Unterschied zur PersistentList ist, dass sie nie _p_note_changed() aufruft sowie beim __getstate__ eine leere Liste zurückliefert.
    """
    
    def __init__(self, *args, **kwargs):
        PersistentList.__init__(self, *args, **kwargs)
        
    def __setitem__(self, i, item):
        self.data[i] = item

    def __delitem__(self, i):
        del self.data[i]
        
    def __setslice__(self, i, j, other):
        if isinstance(other, PersistentList):
            self.data[i:j] = other.data
        elif isinstance(other, type(self.data)):
            self.data[i:j] = other
        else:
            self.data[i:j] = list(other)
            
    def __delslice__(self, i, j):
        del self.data[i:j]
        
    def __iadd__(self, other):
        if isinstance(other, PersistentList):
            self.data += other.data
        else:
            self.data += list(other)
        return self
    
    def __imul__(self, n):
        self._p_note_change()
        self.data *= n
        return self

    def append(self, item):
        self.data.append(item)

    def insert(self, i, item):
        self.data.insert(i, item)

    def pop(self, i=-1):
        return self.data.pop(i)

    def remove(self, item):
        self.data.remove(item)

    def reverse(self):
        self.data.reverse()

    def sort(self, *args, **kwargs):
        self.data.sort(*args, **kwargs)

    def extend(self, other):
        if isinstance(other, PersistentList):
            self.data.extend(other.data)
        else:
            self.data.extend(other)
        
    def __getstate__(self):
        return dict(data=[])
        
    def __str__(self):
        return str(self.data)
