import math

# Deklarasi fungsi
def l_persegi(sisi):
    hitung = sisi * sisi
    print(f'Luas Persegi adalah {hitung}')
    
def l_persegi_panjang(p, l):
    hitung = p * l
    print(f'Luas Persegi Panjang adalah {hitung}')
    
def l_segitiga(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'Luas Segitiga adalah {hitung}')
    
def l_lingkaran(r):
    hitung = math.pi * r * r
    print(f'Luas Lingkaran adalah {hitung}')
    
def l_jajar_genjang(a, t):
    hitung = a * t
    print(f'Luas Jajar Genjang adalah {hitung}')
    