# Tính chỉ số BMI
import math
def tinh_BMI(chieu_cao,can_nang):
    BMI = can_nang/math.pow(chieu_cao,2)
    if BMI < 18.5:
        print("Bảng đánh giá: Gầy")
    elif BMI < 25.0:
        print("Bảng đánh giá : Bình thường")
    else:
        BMI >= 25.0
        print("Bảng đánh giá: Thừa cân")

    return BMI
    
chieu_cao = float(input("Nhập chiều cao :"))
can_nang = float(input("Nhập cân nặng:"))
print("Chỉ số BMI của bạn là :", tinh_BMI(chieu_cao,can_nang))

