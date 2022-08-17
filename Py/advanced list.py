'''
min()max() can be used again in variable
.sort()    cannt be used again
sum()      can be used in variable
+          can be used in variable
len        can be used in variable
in ---     can be used in variable
.count()   can be used in variable
'''
z = ["ap","bang"]
le = len(z)
print(le)

a = [10 , 5]
mi = min(a)
print(mi)

b = [12,6]
ma = max(b)
print(ma)

c = ["so","and"]
c.sort()
print(c)

c = ["aba","aad"]
d = c.sort()
print(c)
print(d)

d = [10,8]
su = sum(d)
print(su)

e = ["z","c"]
f = [10,"w"]
g = e + f 
print(g)

e = ["z","c"]
coun = e.count("z")
print(coun)

f = [10,"w"]
counz = 10 in f
print(counz)



print (' _______EXTREME DATA-----')

sizes = [96, 78, 45, 56, 80]
largest = max(sizes)
smallest = min(sizes)
diffrence = largest - smallest

print("largest grade :")
print(largest)

print("smallest grade :")
print(smallest)

print(f"diffrence between largest and smallest :{diffrence}")


print(' ___________SORTING DATA ----')

pelanggan = ["ujang", "asep", "kusuma"]
kursi_kosong = [10,3,6]

pelanggan.sort()
kursi_kosong.sort()

p = pelanggan[0]
k = kursi_kosong[0]

print(f"{p} silah duduk di kursi {k}")


print('_________SUMMING DATA')

pendapatan_1 = [10,23,45,-6,10]
pendapatan_2 = [12,34,24,-20,24]
a = sum(pendapatan_1)
b = sum(pendapatan_2)
diffrence = a-b
if a > b :
  print(f"Pendapatan minggu pertama unggul ${diffrence}")
else: 
  print(f"Pendapatan minggu kedua unggul ${diffrence}")


print('______________JOINING LISTS---')
#using + for combine lists containing diffrent types of values

a = ["ana", "bagus", "ade"]
b = ["anjay"]
print(a + b)


print("________________COUNTING ELEMENTS")
rattings = [5,4,3,4,2,4,5,1,1,3,5]
i = 5 in rattings
if i :
  five = rattings.count(5)
  print(f'Five star rattings for today :{five}')
y = 1 in rattings
if y :
  one = rattings.count(1)
  print(f'One star rattings for today :{one}')



