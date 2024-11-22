print()
print('## nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    konversi=(celcius*9/5)+32
    return konversi

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


print()
print('## nomor 2 ##')
def ganjil_genap(bilangan):
    penentu=bilangan % 2 == 0
    return penentu

print(ganjil_genap(4)) #true
print(ganjil_genap(7)) #true

print()
print('## nomor3 ##')
def nilai(keterangan):
    if keterangan >= 80:
        print("lulus")
    elif keterangan <= 60:
        print("gagal")
    else:
        print("tidak valid")

nilai (80)
nilai (60)

print()
print('## nomor4 ##')
def bilangan_ganjil(bilangan):
    return[i for i in range(1,bilangan,2)]
print(bilangan_ganjil(20))