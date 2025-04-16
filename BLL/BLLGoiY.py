from DAL.DALGoiY import DALGoiY
from BLL.BLLQuanLy import BLLQuanLy
from datetime import datetime
class BLLGoiY:
    def __init__(self):
        self.goiY = DALGoiY()
        self.bllQuanLy = BLLQuanLy()


    def layDanhSachNhacGoiY(self, idnguoidung: int):
        diem_the_loai = self.goiY.layDiemTheLoai(idnguoidung)
        diem_xuat_xu = self.goiY.layDiemXuatXu(idnguoidung)
        diem_ca_si = self.goiY.layDiemCaSi(idnguoidung)

        danhSachBaiHat = self.bllQuanLy.layDanhSachBaiHat()
        danh_sach_goi_y = []

        
        for bai_hat in danhSachBaiHat:
            tl = diem_the_loai.get(bai_hat.getMaTheLoai(), 0)
            xx = diem_xuat_xu.get(bai_hat.getMaXuatXu(), 0)
            cs = 0
            ca_si_list = bai_hat.getCaSi()
            for ma_ca_si_str in ca_si_list:
                ma_ca_si_id = int(ma_ca_si_str.split('-')[0])
                cs += diem_ca_si.get(ma_ca_si_id, 0)

            cs = cs / len(ca_si_list)
            try:
                now = datetime.now()
                # Chuyển đổi phat_hanh sang datetime nếu là datetime.date
                phat_hanh = datetime.strptime(bai_hat.getNgayPhatHanh(), "%Y-%m-%d") \
                    if isinstance(bai_hat.getNgayPhatHanh(), str) else bai_hat.getNgayPhatHanh()

                if isinstance(phat_hanh, datetime):
                    days_since = max((now - phat_hanh).days, 1)  # Tránh chia cho 0
                else:
                    # Nếu phat_hanh là datetime.date, chuyển sang datetime
                    phat_hanh = datetime.combine(phat_hanh, datetime.min.time())
                    days_since = max((now - phat_hanh).days / 10, 1)


                diem = (cs * 2 + tl + xx + 1) / days_since
                print(f"Điểm bài {bai_hat.getTieuDe()}: {diem} (Thể loại: {tl}, Xuất xứ: {xx}, Ca sĩ: {cs})")
            except Exception as e:
                print(f"Lỗi tính điểm bài {bai_hat.maBaiHat}: {e}")
                diem = 0

            bai_hat.diem = diem  # Gán điểm cho bài hát
            danh_sach_goi_y.append(bai_hat)

        # Sắp xếp theo điểm giảm dần và lấy 6 bài đầu
        danh_sach_goi_y.sort(key=lambda x: x.diem, reverse=True)
        return danh_sach_goi_y[:6]  # Trả về 6 bài hát có điểm cao nhất

    