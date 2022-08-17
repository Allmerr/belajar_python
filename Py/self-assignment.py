''' self-assignment '''
"""self-assignament is when we set a variable to its own value"""
#example
wallet = 6
wallet = wallet
print(wallet)

wallet = wallet + 3
wallet = wallet - 5
print(wallet)

name = "penguna :"
name = name + " kevin"
name = name + " almer"
print(name)

""" 
rather tham rewriting the variable's name, we can use (+=,-=) operator
to add a number with
"""

name = "asep" 
name += " ganteng"
print(name)

tujuan = 4000
tabungan = 3200

print(f"{tujuan-tabungan} RP away from goal")


gajian = 200
tabungan += gajian
print(f"{tujuan-tabungan} RP away from goal")

pengeluaran = 180
tabungan -= pengeluaran
print(f"{tujuan-tabungan} RP away from goal")

""" we can do with (*=,/=,+=,-=) """ 