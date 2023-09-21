n = float(input("nhập số tiền bạn đã chi tiêu ở của hàng : "))
if 75 <= n < 100:
      s = n - 15
      print(f"sô tiền bạn chi tiêu là {n} đô la, bạn được giảm giá là 15 đô la và tiền bạn phải thanh toán là {s}")
elif 100 <= n < 150:
      s = n -25
      print(f"sô tiền bạn chi tiêu là {n} đô la, bạn được giảm giá là 25 đô la và tiền bạn phải thanh toán là {s}")
elif n >= 150:
      s = n - 50
      print(f"sô tiền bạn chi tiêu là {n} đô la, bạn được giảm giá là 50 đô la và tiền bạn phải thanh toán là {s}")
else:
      print(f"sô tiền bạn chi tiêu là {n} đô la, bạn được giảm giá là 0 đô la và tiền bạn phải thanh toán là {s}")
