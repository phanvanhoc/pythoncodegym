n = int(input("nhập 1 số:"))
if 1 <= n <= 7:
    if n == 1:
        print("chủ nhật")
    elif n == 2:
        print("thứ 2")
    elif n == 3:
        print("thứ 3")
    elif n == 4:
        print("thứ 4")
    elif n == 5:
        print("thứ 5")
    elif n == 6:
        print("thứ 6")
    else:
        print("thứ 7")
else:
    print(f"bạn nhâp {n} đã sai dữ liệu")
