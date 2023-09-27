try: 
    x = int(input("mời bạn nhập số nguyên 1: "))
    y = int(input("mời nhập nhập số nguyên thứ 2: "))
    if x < y :
        for i in range(x, y + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)
    else:
        print(f"bạn cần nhập lại {y} phải lớn hơn {x}")
except:
    print("dữ liệu đầu vào không đúng")
