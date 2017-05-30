"""
Implementation of map abatract data type - hashing
"""


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    """
    key : position to be given in slots list based on this key.
    data : data to be assigned at an index in data list and that 
           will be same as that of in slots
    """
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and \
                    self.slots[nextslot] != key
                    nextslot = rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data


    """
    generate the hash function or you can say index in slots and data list
    """
    def hashfunction(self, key, size):
        return key % size


    """
    rehashing in case of collosion
    """
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
