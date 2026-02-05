#Nhập một số và tính căn bậc hai của nó. Nếu số nhập vào âm, hiển thị thông báo lỗi.
n = float(input("Nhập một số: "))
if n < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm")
else:
    can_bac_hai = n ** 0.5
    print("Căn bậc hai của số đã nhập là:", can_bac_hai)
