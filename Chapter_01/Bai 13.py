#Nhập hai số nguyên từ bàn phím và in ra kết quả phép chia của chúng. Xử lý chia cho 0 và dữ liệu không hợp lệ.
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if b == 0:
    print("Không thể chia cho 0")
else:
    ket_qua = a / b
    print("Kết quả phép chia là:", ket_qua)
