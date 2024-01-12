def kiem_tra_so_hoan_hao(n):
    if n <= 0:
        return False  # Số hoàn hảo phải là số nguyên dương

    tong_uoc_so = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc_so += i

    return tong_uoc_so == n


so_can_kiem_tra = 28
ket_qua = kiem_tra_so_hoan_hao(so_can_kiem_tra)

if ket_qua:
    print(f'{so_can_kiem_tra} là số hoàn hảo.')
else:
    print(f'{so_can_kiem_tra} không phải là số hoàn hảo.')
