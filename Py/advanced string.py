#khusus string pengunaan harus disimpan dalam variable berbeda dengan .pop()
'''                        USING STRING                                                          '''
'''
we are able to split up strings and store the individual values inside a list by coding
.split()
'''
sales = "12k 13k 34k"
keuntungan = sales.split() 
print(sales) # khusus string semua pake variable yang ada .split() nya
print(keuntungan)

kode_pos = "16154, 21342, 13423"
kode_pos = kode_pos.split(",") # bisa (*,&,$,!,etc)
print(kode_pos)

'''
we can replace a part of a string stored inside a variable by 
.replace(i,v)
'''
day = 'today\'s my boring'
day = day.replace("boring","birtday")
print(day)
 

#praktek
sequences = "tatgctttcc#tataggtctg#ctattcaatg"
dna_list = sequences.split("#")
print(dna_list)

for dna in dna_list:
  rna = dna.replace("t", "u")
  print(f"DNA: {dna} -> RNA: {rna}")

# for list to string
a = ['kevin' 'almer']
a = "".join(a)
print(a)