import math 
def tinh_S(x,n):
    S = (math.pow(x,2)+1)*n
    return S 

x = float(input("Nhập x cần tính :"))
n = float(input("Nhập n cần tính :"))
print("Kết quả :", tinh_S(x,n))