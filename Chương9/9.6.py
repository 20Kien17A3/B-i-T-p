def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False  

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False  # Nếu x chia hết cho một số từ 2 đến căn bậc hai của x, thì không phải là số nguyên tố

    return True  # Nếu không chia hết cho bất kỳ số nào, x là số nguyên tố


so_can_kiem_tra = 20
ket_qua = kiem_tra_so_nguyen_to(so_can_kiem_tra)

if ket_qua:
    print(f'{so_can_kiem_tra} là số nguyên tố.')
else:
    print(f'{so_can_kiem_tra} không phải là số nguyên tố.')
