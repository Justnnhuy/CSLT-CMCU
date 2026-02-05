#Hàm tính tổng hai số. Viết một hàm sum_two_numbers(a, b) trả về tổng của hai số nguyên. Gọi hàm và in ra kết quả

def sum_two_numbers(a, b):
    return a + b
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
ket_qua = sum_two_numbers(x, y)
print("Tổng của hai số là:", ket_qua)
