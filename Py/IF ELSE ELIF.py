""" 
kita gunakan iF statement untuk menulis code yang beradaptasi
sesuai situasi.
kita mengenali dengan kata kunci if.
if hanya mau jalan kalau setelahnya True
"""
if True:
    print("kebaca kan")
#dia akan ngeprint 

if False :
    print("ngak kebaca dong")

penguna = "kevin"
lampu_nyala = True

#praktek
if lampu_nyala:
    print(f"{penguna} sudah menyalakan lampu")
if lampu_nyala == False:
    print(f"{penguna} sudah mematikan lampu ")

#(>=, <=, >, <, ==, != ) ini semua kita bisa gunakan untuk if statement
a = 88
b = 86
if a>b :
    print("angka juga bisa ")

cuaca = "hujan"
warna_awan = "terang"
sediakan = "skatebord"

if cuaca == "hujan" :
  warna_awan ="mendung"
  sediakan = "payung"
  cuaca = "berawan" # kolo kita apus if kedua hilang 
  print(f"wah {warna_awan} nih ")
  print(f" pake {sediakan} biar  aman ")
if cuaca == "berawan" :
  print(" ini gak kebaca ")

""" daripada buat dua if berkali kali kita gunakan else kalau 
kondisi if false semua else kan run """

stock = "tersedia"

if stock == "habis":
  print("barang kosong gans")
else : 
    print("barang aman gans")
#else harus dibawah if

folowers = 991
one_k = 1000

if folowers >= one_k :
  print("selamat pengikut anda mencapai seribu !")
else :
  folowers_left = one_k - folowers
  print(f"{folowers_left} folowers lagi semangat !")

""" ELIF """

hour = 24 # 15.oo 
ucapan = "selamat malam"
if hour < 9:
    ucapan = "selamat pagi"
    print(ucapan)
elif hour < 14 :
    ucapan = "selamat siang"
    print(ucapan)
elif hour < 18:
    ucapan = "selamat sore"
    print(ucapan)
else :
    print(ucapan)
    
print("____bagian 2____")

''' and operator'''
""" saat kita mau run berdasar dua keputusan atau lebih kita gunakan and"""
#semua harus TRUE
umur = 16
punya_ijin = True 
mengaransikan = True
pesan = "ditolak"
if umur > 18 and punya_ijin and mengaransikan :
  pesan = "diterima"
  print(pesan)
else : 
    print(pesan)




''' or operator '''
""" kalau and semua harus true kalau or minimal satu aja dia akan ran"""
#minimal satu aja

nilai = 70
kehadiran = 70
pesan = "anda tidak lulus"

if nilai > 90 and kehadiran > 90:
    pesan = "kriteria nilai terbaik"
    print(pesan)
elif nilai >= 75 or kehadiran >= 75 :
    pesan = "kriteria lulus"
    print(pesan)
else : 
    print (pesan)



print("___project___")
#projek
warna = "putih"
diskon = 4

parkir = 0
total = 0

if warna == "putih":
    parkir = 20
elif warna == "hitam":
    parkir = 15  
else :
    parkir = 25

print("harga parkir :")
print(parkir)

if diskon > 0 :
    total = parkir - diskon
else :
    total = parkir
print ("harga total :")
print(total)
