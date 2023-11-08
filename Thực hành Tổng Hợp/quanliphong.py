import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Phong:
    def __init__(self, so_phong, suc_chua, tinh_trang, gia, thoi_gian_dat_phong, nhan_xet, ten_khach_hang, cccd, thoi_gian_vao, thoi_gian_thue, san_pham_yeu_cau):
        self.so_phong = so_phong
        self.suc_chua = suc_chua
        self.tinh_trang = tinh_trang
        self.gia = gia
        self.thoi_gian_dat_phong = thoi_gian_dat_phong
        self.nhan_xet = nhan_xet
        self.ten_khach_hang = ten_khach_hang
        self.cccd = cccd
        self.thoi_gian_vao = thoi_gian_vao
        self.thoi_gian_thue = thoi_gian_thue
        self.san_pham_yeu_cau = san_pham_yeu_cau

class QuanLyPhong:
    def __init__(self):
        self.phong = []

    def them_phong(self, phong):
        self.phong.append(phong)

    def xoa_phong(self, phong):
        self.phong.remove(phong)

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("QUẢN LÍ ĐẶT PHÒNG")
root.geometry("1000x600")
quan_ly_phong = QuanLyPhong()

# Hàm để thêm phòng
def them_phong():
    so_phong = entry_so_phong.get()
    suc_chua = entry_suc_chua.get()
    tinh_trang = entry_tinh_trang.get()
    gia = entry_gia.get()
    thoi_gian_dat_phong = entry_thoi_gian_dat_phong.get()
    nhan_xet = entry_nhan_xet.get()
    ten_khach_hang = entry_ten_khach_hang.get()
    cccd = entry_cccd.get()
    thoi_gian_vao = entry_thoi_gian_vao.get()
    thoi_gian_thue = entry_thoi_gian_thue.get()
    san_pham_yeu_cau = entry_san_pham_yeu_cau.get()

    phong_moi = Phong(so_phong, suc_chua, tinh_trang, gia, thoi_gian_dat_phong, nhan_xet, ten_khach_hang, cccd, thoi_gian_vao, thoi_gian_thue, san_pham_yeu_cau)
    quan_ly_phong.them_phong(phong_moi)
    cap_nhat_treeview()

def xoa_phong():
    item_duoc_chon = tree.selection()
    if item_duoc_chon:
        text_cua_item = tree.item(item_duoc_chon, "values")
        so_phong = text_cua_item[0]

        for phong in quan_ly_phong.phong:
            if phong.so_phong == so_phong:
                quan_ly_phong.xoa_phong(phong)
                cap_nhat_treeview()
                break

def cap_nhat_treeview():
    tree.delete(*tree.get_children())
    for phong in quan_ly_phong.phong:
        tree.insert("", "end", values=(phong.so_phong, phong.suc_chua, phong.tinh_trang, phong.gia, phong.thoi_gian_dat_phong, phong.nhan_xet, phong.ten_khach_hang, phong.cccd, phong.thoi_gian_vao, phong.thoi_gian_thue, phong.san_pham_yeu_cau))

# Tạo các widget
label_so_phong = ttk.Label(root, text="Số phòng:", foreground="blue")
label_so_phong.grid(row=0, column=0)

entry_so_phong = ttk.Entry(root)
entry_so_phong.grid(row=0, column=1)

label_suc_chua = ttk.Label(root, text="Sức chứa:", foreground="blue")
label_suc_chua.grid(row=1, column=0)

entry_suc_chua = ttk.Entry(root)
entry_suc_chua.grid(row=1, column=1)

label_tinh_trang = ttk.Label(root, text="Tình trạng:", foreground="blue")
label_tinh_trang.grid(row=2, column=0)

entry_tinh_trang = ttk.Entry(root)
entry_tinh_trang.grid(row=2, column=1)

label_gia = ttk.Label(root, text="Giá phòng:", foreground="blue")
label_gia.grid(row=3, column=0)

entry_gia = ttk.Entry(root)
entry_gia.grid(row=3, column=1)

label_thoi_gian_dat_phong = ttk.Label(root, text="Thời gian đặt phòng:", foreground="blue")
label_thoi_gian_dat_phong.grid(row=4, column=0)

entry_thoi_gian_dat_phong = ttk.Entry(root)
entry_thoi_gian_dat_phong.grid(row=4, column=1)

label_nhan_xet = ttk.Label(root, text="Nhận xét khách:", foreground="blue")
label_nhan_xet.grid(row=5, column=0)

entry_nhan_xet = ttk.Entry(root)
entry_nhan_xet.grid(row=5, column=1)

label_ten_khach_hang = ttk.Label(root, text= "Tên khách hàng:", foreground="blue")
label_ten_khach_hang.grid(row=6, column=0)

entry_ten_khach_hang = ttk.Entry(root)
entry_ten_khach_hang.grid(row=6, column=1)

label_cccd = ttk.Label(root, text="Số CCCD:", foreground="blue")
label_cccd.grid(row=7, column=0)

entry_cccd = ttk.Entry(root)
entry_cccd.grid(row=7, column=1)

label_thoi_gian_vao = ttk.Label(root, text="Thời gian vào:", foreground="blue")
label_thoi_gian_vao.grid(row=8, column=0)

entry_thoi_gian_vao = ttk.Entry(root)
entry_thoi_gian_vao.grid(row=8, column=1)

label_thoi_gian_thue = ttk.Label(root, text="Thời gian thuê phòng:", foreground="blue")
label_thoi_gian_thue.grid(row=9, column=0)

entry_thoi_gian_thue = ttk.Entry(root)
entry_thoi_gian_thue.grid(row=9, column=1)

label_san_pham_yeu_cau = ttk.Label(root, text="Sản phẩm yêu cầu:", foreground="blue")
label_san_pham_yeu_cau.grid(row=10, column=0)

entry_san_pham_yeu_cau = ttk.Entry(root)
entry_san_pham_yeu_cau.grid(row=10, column=1)

button_them = ttk.Button(root, text="Thêm phòng", command=them_phong)
button_them.grid(row=11, column=0)

button_xoa = ttk.Button(root, text="Xóa phòng", command=xoa_phong)
button_xoa.grid(row=11, column=1)

# Tạo TreeView để hiển thị thông tin
cot = ("Số phòng", "Sức chứa", "Tình trạng", "Giá", "Thời gian đặt phòng", "Nhận xét", "Tên khách hàng", "Số CCCD", "Thời gian vào", "Thời gian thuê phòng", "Sản phẩm yêu cầu")
tree = ttk.Treeview(root, columns=cot, show="headings")
for col in cot:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.grid(row=12, column=0, columnspan=2)

# Hàm lưu thông tin vào file
def luu_vao_file():
    with open("thong_tin_phong.txt", "w", encoding="utf-8") as file:

        for phong in quan_ly_phong.phong:
            file.write(f"Số phòng: {phong.so_phong}\n")
            file.write(f"Sức chứa: {phong.suc_chua}\n")
            file.write(f"Tình trạng: {phong.tinh_trang}\n")
            file.write(f"Giá: {phong.gia}\n")
            file.write(f"Thời gian đặt phòng: {phong.thoi_gian_dat_phong}\n")
            file.write(f"Nhận xét: {phong.nhan_xet}\n")
            file.write(f"Tên khách hàng: {phong.ten_khach_hang}\n")
            file.write(f"Số CCCD: {phong.cccd}\n")
            file.write(f"Thời gian vào: {phong.thoi_gian_vao}\n")
            file.write(f"Thời gian thuê phòng: {phong.thoi_gian_thue}\n")
            file.write(f"Sản phẩm yêu cầu: {phong.san_pham_yeu_cau}\n\n")

# Hàm in hóa đơn
def in_hoa_don():
    noi_dung_hoa_don = ""
    for phong in quan_ly_phong.phong:
        noi_dung_hoa_don += f"Số phòng: {phong.so_phong}\n"
        noi_dung_hoa_don += f"Sức chứa: {phong.suc_chua}\n"
        noi_dung_hoa_don += f"Tình trạng: {phong.tinh_trang}\n"
        noi_dung_hoa_don += f"Giá: {phong.gia}\n"
        noi_dung_hoa_don += f"Thời gian đặt phòng: {phong.thoi_gian_dat_phong}\n"
        noi_dung_hoa_don += f"Nhận xét: {phong.nhan_xet}\n"
        noi_dung_hoa_don += f"Tên khách hàng: {phong.ten_khach_hang}\n"
        noi_dung_hoa_don += f"Số CCCD: {phong.cccd}\n"
        noi_dung_hoa_don += f"Thời gian vào: {phong.thoi_gian_vao}\n"
        noi_dung_hoa_don += f"Thời gian thuê phòng: {phong.thoi_gian_thue}\n"
        noi_dung_hoa_don += f"Sản phẩm yêu cầu: {phong.san_pham_yeu_cau}\n\n"

    # In hóa đơn
    print(noi_dung_hoa_don)

# Hàm hiển thị thông tin
def hien_thi_thong_tin():
    tk.messagebox.showinfo("Thông tin", "Ứng dụng quản lý đặt phòng\nPhiên bản 1.0\nTác giả: Học viên - Phan Văn Học/ SDT: 09998999999")

# Khởi tạo QuanLyPhong
quan_ly_phong = QuanLyPhong()

# Tạo Menu
menu = tk.Menu(root)
root.config(menu=menu)

menu_tap_tin = tk.Menu(menu)
menu.add_cascade(label="menu", menu=menu_tap_tin)
menu_tap_tin.add_command(label="Lưu", command=luu_vao_file)
menu_tap_tin.add_command(label="In hóa đơn", command=in_hoa_don)
menu_tap_tin.add_separator()
menu_tap_tin.add_command(label="Thoát", command=root.quit)

menu_tro_giup = tk.Menu(menu)
menu.add_cascade(label="trợ giúp", menu=menu_tro_giup)
menu_tro_giup.add_command(label="Thông tin", command=hien_thi_thong_tin)

# Chạy chương trình
root.mainloop()