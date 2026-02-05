#Thực hiện các phép toán cơ bản với hai số. Nhập hai số nguyên từ người dùng. Tính và in ra tổng, hiệu, tích và thương của chúng

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
tong = a + b
hieu = a - b
tich = a * b
print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
if b != 0:
    thuong = a / b
    print("Thương:", thuong)
else:
    print("Không thể chia cho 0")
