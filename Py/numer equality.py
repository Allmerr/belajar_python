""" (==) untuk membandingkan sesuatu  apakah sama ?
saat membandingkan hanya ada dua jawabaan True/False"""
print( 9 == 10 )# hasilnya false

pendukung = 9
target_pendukung = 10
print(pendukung == target_pendukung)# hasilnya false

"""(!=) untuk mengecek apakah itu tidak setara 
"""
hasil = 10 != 11
print(hasil)# hasilnya false

today = 12
birthday = 13
apakah_hari_ini_bukan_hari_ulang_tahun_saya = today != birthday
print("apakah hari ini bukan hari ulang tahun saya ?")
print(apakah_hari_ini_bukan_hari_ulang_tahun_saya)

""" ini semua bisa kita gunakan dengan huruf/string juga"""
#contoh
saldo = 1000
saldo_keluar = 700
target = 750

target_tercapai = saldo_keluar == target
print ("Targat Tercapai :")
print(target_tercapai)

saldo_saat_ini = saldo - saldo_keluar
stok_habis = saldo_saat_ini != 0
print ("Stok Tersedia :")
print (stok_habis)

#contoh 
nama_1 = "kevin"
rata_rata_1 = "b"
nilai_ulangan_1 = 88

nama_2 = "kerin"
rata_rata_2 = "A"
nilai_ulangan_2 = 80

print("nama sama ?")
print(nama_1 == nama_2)

print("rata rata kevin sama dengan kerin ?")
print(nama_1 == nama_2)

print("nilai ulangan kevin lebih besar dari kerin")
print(nilai_ulangan_1 > nilai_ulangan_2)


print("----------------")

""" kita bisa gunakan perbandingan untuk mengecek apakah 
sebuah angka lebih besar atau kecil"""

#(<) kurang dari
#(>) lebih besar dari
nilai_a = 85
nilai_b = 75
print("apakah nilai asep lebih kecil dari bagong ?")
print (nilai_a < nilai_b)
print ("apakah nilai asep lebih besar dari bagong :")
print (nilai_a > nilai_b )


#(<=) kurang dari atau sama
#(>=) lebih besar dari atau sama
# praktek
nilai_a = 8
nilai_b = 10
nilai_maksimal = 10
nilai_terendah = 8

nilai_tinggi = nilai_a >= nilai_maksimal
print("apakah a nilai tertinggi ? ")
print(nilai_tinggi)

print ("apakah  b nilai tertinggi ?")
nilai_rendah = nilai_b >= nilai_terendah
print(nilai_rendah)


# 'is' sebagai komparasi object identity
print('======== object identity(is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print('======== object identity(is not)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil) 












