#Nhập thông tin 3 sinh viên (Tên và điểm 3 môn - Toán, Lý, Hóa). In ra tên sinh viên, và điểm trung bình tương ứng.
# Sinh viên 1
name1 = input("Nhập tên sinh viên 1: ")
toan1 = float(input("Nhập điểm Toán: "))
ly1 = float(input("Nhập điểm Lý: "))
hoa1 = float(input("Nhập điểm Hóa: "))
dtb1 = (toan1 + ly1 + hoa1) / 3
# Sinh viên 2
name2 = input("\nNhập tên sinh viên 2: ")
toan2 = float(input("Nhập điểm Toán: "))
ly2 = float(input("Nhập điểm Lý: "))
hoa2 = float(input("Nhập điểm Hóa: "))
dtb2 = (toan2 + ly2 + hoa2) / 3
# Sinh viên 3
name3 = input("\nNhập tên sinh viên 3: ")
toan3 = float(input("Nhập điểm Toán: "))
ly3 = float(input("Nhập điểm Lý: "))
hoa3 = float(input("Nhập điểm Hóa: "))
dtb3 = (toan3 + ly3 + hoa3) / 3
print("--- KẾT QUẢ ---")
print(name1, "- Điểm trung bình:", dtb1)
print(name2, "- Điểm trung bình:", dtb2)
print(name3, "- Điểm trung bình:", dtb3)
