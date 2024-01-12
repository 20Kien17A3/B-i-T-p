def phan_nguyen_chia(a, b):
    if b == 0:
        print("Không thể chia cho 0.")
        return None
    
    phan_nguyen = a // b
    return phan_nguyen


so_chia = 10
so_bi_chia = 3
ket_qua = phan_nguyen_chia(so_chia, so_bi_chia)

if ket_qua is not None:
    print(f'Phần nguyên của {so_chia} chia {so_bi_chia} là: {ket_qua}')
