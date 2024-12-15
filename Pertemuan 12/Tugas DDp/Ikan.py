from animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, pernapasan, jenis_air):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.pernapasan = pernapasan
        self.jenis_air = jenis_air
        
    def info_ikan(self):
        super().info_animal(),
        print("Pernapasan \t\t : ", self.pernapasan,
              "\nJenis Air \t\t : ", self.jenis_air)
        
ikan_lele = Ikan ("Lele", "Ikan kecil", "Air", "Bertelur", "Paru-paru", "Air Tawar")
ikan_lele.info_ikan()
print("==========================================")
ikan_cupang = Ikan("Cupang", "Pelet", "Air", "Bertelur", "Insang", "Air PAM")
ikan_cupang.info_ikan()