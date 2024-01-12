# Xây dựng phương thức tính tinh_S(n, x)
def tinh_S(n, x):
    S = (x**2 + 1)**n
    return S

n = float(input("Nhập n :"))
x = float(input("Nhập x :"))
result = tinh_S(n, x)
print(f'Giá trị của S với n={n} và x={x} là: {result}')
