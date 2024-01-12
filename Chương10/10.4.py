import math 
def tinh_A(x,n):
    A = (math.pow(math.pow(x,2)+x+1),n) + (math.pow(math.pow(x,2)-x+1),n)
    return A

x = float(input("Nhập x cần tính :"))
n = float(input("Nhập n cần tính :"))
print("Kết quả :", tinh_A(x,n))
