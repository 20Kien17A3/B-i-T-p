def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# Thử nghiệm hàm sign
number = float(input("Nhập một số: "))
result = sign(number)
print(f"Kết quả của sign({number}) là: {result}")
