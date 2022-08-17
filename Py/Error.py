"""
Sometime we want to raise an exception when a condition we hav defineded is not met
"""

age = 3
if not age >= 0:
  raise ValueError('age cannot be negative') # we can use ValueError, TypeError, KeyError
# the raise keyword is used to raise an exception

'''
we often don't want a program to terminate when exception is occured
'''

details = {
    "name" : "asep",
    "Job" : "Data Analysts",
    "age" : 23
}

i = input("Masukan data yang ingin anda cari ? ")
try :
    age = details[i]

except :
    raise NameError("Data yang anda masukan salah") # or you can put print instead of

else :
    print(f'Ini adalah data yang anda cari {details[i]}') # this will only do this job when try True

finally :
    print("Terimaksih") # this will print even try occured False
