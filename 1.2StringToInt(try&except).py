#simple conversion
#num = "1000"
#print(int(num))

alpha_int = "Thousand"
try:
    print(int(alpha_int))  #"Thousand" can't be converted to int -> raises a value error
except ValueError as alpha_int:
    print("Error:", alpha_int)
print(alpha_int)

# alpha_int = "Thousand"
# try:
#     print(int(alpha_int))  #"Thousand" can't be converted to int -> raises a value error
# except ValueError as e:
#     print("Error:", e)
# print(alpha_int)