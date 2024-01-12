def tinh_A(n, x):
    A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    return A


n = float(input("Nhập n :"))
x = float(input("Nhập x :"))
result = tinh_A(n, x)
print(f'Giá trị của A với n={n} và x={x} là: {result}')
