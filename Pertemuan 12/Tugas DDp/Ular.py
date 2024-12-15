from animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, Habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.habitat = Habitat
        
    def info_ular(self):
        super().info_animal(),
        print("Berbisa \t\t : ", self.berbisa,
              "\nHabitat \t\t : ", self.habitat)
        
ular_kobra = Ular ("Kobra", "Tikus","Darat", "Bertelur","Berbisa","Hutan Perawan")
ular_kobra.info_ular()
print("===============================================")
ular_piton = Ular ("Piton", "Rakun", "Darat", "Bertelur", "Tidak Berbisa", "Rawa")
ular_piton.info_ular()