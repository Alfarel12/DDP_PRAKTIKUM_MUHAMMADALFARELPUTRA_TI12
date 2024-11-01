#variablelist
kendaraan = ['bmw f30','mobil', 3500, 'hitam', 4]
print(kendaraan)

kendaraan.append('500 jt')
kendaraan.append('manual')
print(kendaraan)

kendaraan.insert(2, 'bmw')
print(kendaraan)



#matchcase
hitung_luas = int(input("""Pilih salah
satu:
1. Hitung luas persegi
2. Hitung luas lingkaran
3. Hitung luas segitiga
"""))
match hitung_luas:
     case 1:
          print('Menghitung Luas Persegi')
          sisi=int(input('masukan nilai sisi: '))
          hitung_luas_persegi = sisi**2
          print(f'jadi luas persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi}cm^2')
     case 2:
          print('Menghitung Luas Lingkaran')
          jari_jari=int(input('masukan nilai jari jari:'))
          hitung_luas_lingkaran = 3.14 * jari_jari * jari_jari
          print(f'jadi luas lingkaran dengan jari jari {jari_jari} cm adalah {hitung_luas_lingkaran}cm^2')
     case 3:
          print('Menghitung Luas Segitiga')
          alas=int(input('masukan nilai alas:'))
          tinggi=int(input('masukan nilai tinggi:'))
          hitung_luas_segitiga = 0.5 * alas * tinggi
          print(f'jadi luas segitiga dengan alas dan tinggi {alas} dan {tinggi} cm adalah {hitung_luas_segitiga}cm^2')

     case _:
          print('pilihan tidak valid')
