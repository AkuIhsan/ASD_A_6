from collections import deque # Menggunakan class deque dari pustaka collections dikarenakan peforma deque lebih cepat daripada list biasa

# Inisiasi class Queue
class Queue :
    """Data Stuktur Queue"""
    def __init__(self):    
        self.data = deque()

    def enqueue(self, item) :
        """ Menambahkan elemen ke dalam antrian"""
        self.data.append(item)

    def dequeue(self) :
        """ Mengeluarkan elemen dalam antrian"""
        self.data.popleft()

    def peek(self):
        """ Melihat elemen dengan posisi pertama masuk"""
        self.data[0]

    def isEmpty(self) :
        """ Melihat apakah antrian dalam kondisi kosong atau tidak"""
        return len(self.data) == 0
    
    def size(self) :
        """ Melihat ukuran dari antiran """
        return len(self.data)
    