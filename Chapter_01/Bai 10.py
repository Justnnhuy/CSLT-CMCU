#Đếm số lần xuất hiện của ký tự ‘a’. Nhập một chuỗi và đếm số lần chữ cái ‘a’ xuất hiện.
s = input("Nhập một chuỗi: ")
count = 0
for ch in s:
    if ch == 'a':
        count += 1
print("Số lần ký tự 'a' xuất hiện là:", count)
