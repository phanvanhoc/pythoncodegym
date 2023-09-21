cao = float(input("nhập chiều cao bằng cm: "))/100
nang = float(input("nhập cân năng bằng kg: "))
BMI = nang/(cao**2)
if BMI > 40:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu béo phì cấp độ 3:")
elif 35 <= BMI < 40:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu béo phì cấp độ 2:")
elif 25 <= BMI < 35:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu thừa cân:")
elif 18.5 <= BMI < 25:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu bình thường:")
elif 17 <= BMI <18.5:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu gầy cấp độ 1:")
elif 16 <= BMI < 17:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu gầy cấp độ 2:")
else:
    print(f"BMI của bạn là {BMI}, bạn thuộc kiểu gầy cấp độ 3:")
