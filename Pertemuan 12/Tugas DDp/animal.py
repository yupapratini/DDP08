class Animal :
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info_animal(self):
        print("Nama \t\t\t : ", self.nama,
              "\nMakanan \t\t : ", self.makanan,
              "\nHidup \t\t\t : ", self.hidup,
              "\nBerkembang biak \t : ", self.berkembang_biak)
        
        
        
# binatang = Animal("Puyuh", "biji", "Udara", "bertelur")
# binatang.info_animal()