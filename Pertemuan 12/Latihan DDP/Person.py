class person:
    nama = ""
    gender = ""
    umur = ""
    
    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
        
    def cetak(self):
        print("Nama \t\t : ", self.nama,
              "\nJenis Kelamin \t : ", self.gender,
              "\nUmur \t\t : ", self.umur)
