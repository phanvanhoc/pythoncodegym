import random
dem = 0
chon = random.randint(0, 1)
while True: 
    try:
        if chon == 0:
            nguoi = int(input("mời bạn nhập số nguyên từ 1 đến 3: "))
            may = random.randint(1, 3)
            dem = dem + nguoi + may
            print("dem hien tai la :", dem)
            if dem == 21:
                print(f"tong dem la {dem} bạn là người chiến thắng")
                game = input("bạn có muốn chơi tiếp không nếu chơi nhập (y), không nhập (k)")
                if game == "k":
                    print("kết thúc trò chơi")
                    break
                elif game == "y":
                    print("trò chơi tiếp tục")
                    dem = 0
                    chon = random.randint(0, 1)
                    continue
        if chon == 1:
            may = random.randint(1, 3)
            nguoi = int(input("mời bạn nhập số nguyên từ 1 đến 3: "))
            dem = dem + nguoi + may
            print("dem hien tai là :", dem)
            if dem > 21:
                print(f"tong dem la {dem} bạn là người thua")
                game = input("bạn có muốn chơi tiếp không nếu chơi nhập (y), không nhập (k)")
                if game == "k":
                    print("kết thúc trò chơi")
                    break
                elif game == "y":
                    print("trò chơi tiếp tục: ")
                    dem = 0
                    chon = random.randint(0, 1)              
                    continue
    except:
        print("dữ liệu đầu vào đã sai: ")
