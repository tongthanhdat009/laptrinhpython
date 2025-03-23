import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DAL.DALQuanLyDanhSachPhatHeThong import DALQuanLyDanhSachPhatHeThong
class BLLQuanLyDanhSachPhatHeThong:
    def __init__(self):
        super().__init__()
        self.dal = DALQuanLyDanhSachPhatHeThong()
    def lay_danh_sach_phat_he_thong(self):
        return self.dal.lay_danh_sach_phat_he_thong()
    
    def lay_danh_sach_phat_he_thong_theo_ma(self, ma_danh_sach_phat):
        return self.dal.lay_danh_sach_phat_he_thong_bang_id(ma_danh_sach_phat)
    
    def lay_danh_sach_bai_hat_theo_ma_danh_sach(self, ma_danh_sach_phat):
        return self.dal.lay_bai_hat_theo_danh_sach_he_thong(ma_danh_sach_phat)
    
    def xoa_bai_hat_khoi_danh_sach(self, id_danh_sach_phat: int, id_bai_hat: int):
        if not id_danh_sach_phat or not id_bai_hat:
            print("ID danh sách phát hoặc ID bài hát không hợp lệ")
            return False
            
        danh_sach = self.dal.lay_danh_sach_phat_he_thong_bang_id(id_danh_sach_phat)
        if not danh_sach:
            print(f"Không tìm thấy danh sách phát có ID = {id_danh_sach_phat}")
            return False
        
        # Gọi hàm xóa bài hát từ DAL
        result = self.dal.xoa_bai_hat_trong_danh_sach(id_danh_sach_phat, id_bai_hat)
        
        return result
    
    def lay_bai_hat_chua_co_trong_danh_sach(self, ma_danh_sach_phat):
        return self.dal.lay_bai_hat_chua_co_trong_danh_sach(ma_danh_sach_phat)

    def them_bai_hat_vao_danh_sach(self, ma_danh_sach_phat, ma_bai_hat_list):
        # Kiểm tra tham số đầu vào
        if not ma_danh_sach_phat:
            print("Mã danh sách phát không hợp lệ")
            return 0, 0
        
        # Kiểm tra danh sách mã bài hát
        if not ma_bai_hat_list:
            print("Không có bài hát nào để thêm")
            return 0, 0
        
        # Chuyển về dạng list nếu là số đơn lẻ
        if isinstance(ma_bai_hat_list, int):
            ma_bai_hat_list = [ma_bai_hat_list]
        
        # Gọi DAL để thêm bài hát
        return self.dal.them_nhac_chi_tiet_danh_sach_phat(ma_danh_sach_phat, ma_bai_hat_list)
    
    def cap_nhat_danh_sach_phat(self, update_data: list):
        return self.dal.cap_nhat_danh_sach_phat(update_data)
    
    def xoa_danh_sach_phat(self, ma_danh_sach_phat):
        return self.dal.xoa_danh_sach_phat_he_thong(ma_danh_sach_phat)
    
    def lay_id_danh_sach_phat_moi(self):
        return self.dal.lay_id_max_danh_sach_phat_he_thong()
    
    def them_danh_sach_phat(self, data):
        return self.dal.them_danh_sach_phat_he_thong_moi(data)