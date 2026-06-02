from collections import deque # Menggunakan class deque dari pustaka collections dikarenakan peforma deque lebih cepat daripada list biasa

# Inisiasi class Stack
class Stack :
    """Data Stuktur Stack"""
    def __init__(self):    
        self.data = deque()
        self.size = 0

    
    def push(self, item) : 
        """ Method untuk memasukkan elemen ke dalam Stack """
        if not self.isFull():       
            self.data.append(item) 
            return True
        
        return False
    
    def pop(self) :
        """ Method untuk menghapus elemen dari dalam Stack """
        if not self.isEmpty() :
            item = self.data.pop()
            return item
        
        return False
    
    def peek(self) :
        """ Method untuk melihat elemen dengan posisi paling terakhir dari dalam Stack """
        item = self.data[-1]
        return item

    def isEmpty(self) :
        """ Method untuk melihat apakah stack masih kosong atau belum"""
        if not len(self.data) : return True
        return False
     
    def SeeSize(self) :
        """ Method untuk melihat ukuran dari Stack """ 
        return len(self.data)

    def SetSize(self, size = 0) :
        """ Method untuk mengatur ukuran dari Stack """
        self.size = size
    
    def isFull(self) :
        """ Method untuk melihat apakah Stack sudah penuh atau belum """
        if self.SeeSize() == self.size : return True
        return False

    def reset(self) :
        """ Method untuk mereset isi stack"""
        self.data = deque()



    
